"""Dynamic Part Average Testing (DPAT) preprocessing for burn-in screening.

This module holds the shared constants for Module A and turns raw 0h/24h
burn-in measurements into the 9-feature, lot-relative feature space consumed
by the Isolation Forest.  All lot statistics are *robust* (median / MAD with
IQR, standard-deviation and epsilon fall-backs) so that latent defects cannot
bias their own baseline.
"""

from __future__ import annotations

import logging
from typing import Dict, List, Sequence, Tuple

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------- #
# Constants
# --------------------------------------------------------------------------- #
STATIC_LIMITS: Dict[str, float] = {"Iddq": 100.0, "leakage": 50.0, "delay": 15.0}
PARAMS: Tuple[str, ...] = ("Iddq", "leakage", "delay")
CHECKPOINTS: Tuple[str, ...] = ("0h", "24h")

UNITS: Dict[str, str] = {"Iddq": "µA", "leakage": "µA", "delay": "ns"}
DISPLAY_LABELS: Dict[str, str] = {
    "Iddq": "Standby Current (Iddq)",
    "leakage": "Leakage Current (Ileak)",
    "delay": "Propagation Delay (tpd)",
}

EPSILON: float = 1e-6
MAD_TO_SIGMA: float = 1.4826
IQR_TO_SIGMA: float = 1.35
DPAT_SIGMA_THRESHOLD: float = 4.5

ID_COLUMNS: Tuple[str, ...] = ("serial_number", "lot_id")
RAW_COLUMNS: List[str] = [f"{p}_{c}" for c in CHECKPOINTS for p in PARAMS]

Z_0H_COLUMNS: List[str] = [f"z_{p}_0h" for p in PARAMS]
Z_24H_COLUMNS: List[str] = [f"z_{p}_24h" for p in PARAMS]
Z_DRIFT_COLUMNS: List[str] = [f"zdrift_{p}" for p in PARAMS]
FEATURE_COLUMNS: List[str] = Z_0H_COLUMNS + Z_24H_COLUMNS + Z_DRIFT_COLUMNS

FEATURE_TO_PARAM: Dict[str, str] = {}
FEATURE_DISPLAY: Dict[str, str] = {}
for _p in PARAMS:
    FEATURE_TO_PARAM[f"z_{_p}_0h"] = _p
    FEATURE_TO_PARAM[f"z_{_p}_24h"] = _p
    FEATURE_TO_PARAM[f"zdrift_{_p}"] = _p
    FEATURE_DISPLAY[f"z_{_p}_0h"] = f"{_p} z-score @0h"
    FEATURE_DISPLAY[f"z_{_p}_24h"] = f"{_p} z-score @24h"
    FEATURE_DISPLAY[f"zdrift_{_p}"] = f"{_p} drift z-score"


# --------------------------------------------------------------------------- #
# Robust statistics
# --------------------------------------------------------------------------- #
def robust_location_scale(values: Sequence[float]) -> Tuple[float, float, str]:
    """Return ``(median, robust_sigma, method)`` for a 1-D sample.

    The scale fall-back chain is::

        1.4826 * MAD  ->  IQR / 1.35  ->  standard deviation  ->  1e-6

    A candidate scale is accepted only if it exceeds ``EPSILON``.
    """
    arr = np.asarray(values, dtype=float)
    arr = arr[np.isfinite(arr)]
    if arr.size == 0:
        return 0.0, EPSILON, "epsilon"

    median = float(np.median(arr))
    mad = float(np.median(np.abs(arr - median)))
    sigma = MAD_TO_SIGMA * mad
    if sigma > EPSILON:
        return median, sigma, "mad"

    q75, q25 = np.percentile(arr, [75, 25])
    sigma = float((q75 - q25) / IQR_TO_SIGMA)
    if sigma > EPSILON:
        return median, sigma, "iqr"

    sigma = float(np.std(arr))
    if sigma > EPSILON:
        return median, sigma, "std"

    return median, EPSILON, "epsilon"


def drift_percent(v0: np.ndarray, v24: np.ndarray) -> np.ndarray:
    """Drift velocity ``(V24 - V0) / V0 * 100`` with a zero-denominator guard."""
    v0 = np.asarray(v0, dtype=float)
    v24 = np.asarray(v24, dtype=float)
    denom = np.where(np.abs(v0) < EPSILON, EPSILON, v0)
    return (v24 - v0) / denom * 100.0


# --------------------------------------------------------------------------- #
# Validation
# --------------------------------------------------------------------------- #
def validate_input(df: pd.DataFrame) -> pd.DataFrame:
    """Check schema, coerce numerics and drop rows with unusable measurements."""
    missing = [c for c in (*ID_COLUMNS, *RAW_COLUMNS) if c not in df.columns]
    if missing:
        raise ValueError(f"Input data is missing required columns: {missing}")

    out = df.copy()
    for col in RAW_COLUMNS:
        out[col] = pd.to_numeric(out[col], errors="coerce")

    bad = out[RAW_COLUMNS].isna().any(axis=1) | out["lot_id"].isna()
    bad |= ~np.isfinite(out[RAW_COLUMNS].to_numpy(dtype=float)).all(axis=1)
    if bad.any():
        logger.warning("Dropping %d row(s) with missing/non-finite measurements.", int(bad.sum()))
        out = out.loc[~bad]
    if out.empty:
        raise ValueError("No valid rows remain after validation.")
    if out["serial_number"].duplicated().any():
        logger.warning("Duplicate serial numbers detected; keeping first occurrence.")
        out = out.drop_duplicates(subset="serial_number", keep="first")
    return out.reset_index(drop=True)


# --------------------------------------------------------------------------- #
# Main preprocessing
# --------------------------------------------------------------------------- #
def preprocess(df: pd.DataFrame, dpat_sigma: float = DPAT_SIGMA_THRESHOLD) -> pd.DataFrame:
    """Build lot-relative robust features and DPAT flags.

    Added columns
    -------------
    ``drift_pct_<p>``                 drift velocity in percent
    ``z_<p>_0h`` / ``z_<p>_24h`` / ``zdrift_<p>``   the 9 model features
    ``lot_median_<p>_0h`` / ``_24h``  lot medians of the raw measurements
    ``lot_median_drift_pct_<p>``      lot median of drift velocity
    ``dpat_max_abs_z``, ``dpat_driver``, ``dpat_flag_<p>``, ``dpat_flag``
    ``static_breach``, ``static_breach_params``
    """
    data = validate_input(df)

    for p in PARAMS:
        data[f"drift_pct_{p}"] = drift_percent(data[f"{p}_0h"].to_numpy(), data[f"{p}_24h"].to_numpy())

    # (source column, z-score column, lot-median column)
    plan: List[Tuple[str, str, str]] = []
    for p in PARAMS:
        plan.append((f"{p}_0h", f"z_{p}_0h", f"lot_median_{p}_0h"))
        plan.append((f"{p}_24h", f"z_{p}_24h", f"lot_median_{p}_24h"))
        plan.append((f"drift_pct_{p}", f"zdrift_{p}", f"lot_median_drift_pct_{p}"))

    for _, zcol, mcol in plan:
        data[zcol] = 0.0
        data[mcol] = 0.0

    fallback_counts: Dict[str, int] = {"mad": 0, "iqr": 0, "std": 0, "epsilon": 0}
    lot_positions = data.groupby("lot_id", sort=True).indices
    for lot_id, pos in lot_positions.items():
        for src, zcol, mcol in plan:
            values = data[src].to_numpy(dtype=float)[pos]
            median, sigma, method = robust_location_scale(values)
            fallback_counts[method] += 1
            data.loc[data.index[pos], zcol] = (values - median) / sigma
            data.loc[data.index[pos], mcol] = median
        if len(pos) < 20:
            logger.warning("Lot %s has only %d chips; robust baselines may be unreliable.", lot_id, len(pos))

    logger.info(
        "Robust scaling: %d lots, scale method usage %s",
        len(lot_positions),
        fallback_counts,
    )

    # --- 1-D DPAT rule -------------------------------------------------- #
    z_abs = data[FEATURE_COLUMNS].abs()
    data["dpat_max_abs_z"] = z_abs.max(axis=1)
    data["dpat_driver"] = z_abs.idxmax(axis=1)
    for p in PARAMS:
        cols = [f"z_{p}_0h", f"z_{p}_24h", f"zdrift_{p}"]
        data[f"dpat_flag_{p}"] = data[cols].abs().max(axis=1) >= dpat_sigma
    data["dpat_flag"] = data["dpat_max_abs_z"] >= dpat_sigma

    # --- Static datasheet screening -------------------------------------- #
    breach_cols = []
    for p in PARAMS:
        col = f"static_breach_{p}"
        data[col] = (data[f"{p}_0h"] > STATIC_LIMITS[p]) | (data[f"{p}_24h"] > STATIC_LIMITS[p])
        breach_cols.append(col)
    data["static_breach"] = data[breach_cols].any(axis=1)
    data["static_breach_params"] = data.apply(
        lambda r: ",".join(p for p in PARAMS if r[f"static_breach_{p}"]), axis=1
    )
    data = data.drop(columns=breach_cols)

    logger.info(
        "DPAT rule (max|z| >= %.1f) flagged %d / %d chips; static limits flagged %d.",
        dpat_sigma,
        int(data["dpat_flag"].sum()),
        len(data),
        int(data["static_breach"].sum()),
    )
    return data


def lot_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Per-lot robust summary table (median of each 24h parameter, chip count)."""
    rows = []
    for lot_id, grp in df.groupby("lot_id", sort=True):
        row: Dict[str, float] = {"lot_id": lot_id, "n_chips": float(len(grp))}
        for p in PARAMS:
            median, sigma, _ = robust_location_scale(grp[f"{p}_24h"].to_numpy())
            row[f"median_{p}_24h"] = median
            row[f"robust_sigma_{p}_24h"] = sigma
        rows.append(row)
    return pd.DataFrame(rows)
