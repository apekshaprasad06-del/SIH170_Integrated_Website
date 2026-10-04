"""Physically motivated, non-symmetric burn-in telemetry generator.

Design notes
------------
* Iddq and leakage are log-normal (sub-threshold conduction is exponential in
  the threshold-voltage shift), with an occasional Weibull heavy-tail boost.
* Propagation delay is right-skewed: log-normal Vth coupling plus a Weibull
  tail term (slow-corner devices).  A shared Vth factor makes leakage and
  delay anti-correlated in the healthy population.
* Every lot has its own nominal centroid, spread, drift amplitude and defect
  rate (3 % - 12 %).  Some lots carry a wafer-edge effect that both elevates
  edge-die currents and concentrates defects at large radius.
* Healthy 0h -> 24h drift is positive, saturating (1 - exp(-t/tau)) and
  right-skewed; latent defects show accelerated, compounding current drift
  with a non-linearly coupled delay degradation.
* Every injected defect is clamped below ``ceiling * STATIC_LIMIT`` with
  ``ceiling`` in [0.92, 0.96], so static 1-D screening can never catch it.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd

from preprocessing import PARAMS, STATIC_LIMITS

logger = logging.getLogger(__name__)

DEFAULT_OUTPUT_PATH = "burn_in_lot_data.csv"
LABEL_COLUMN = "is_latent_defect"
DEFECT_TYPE_COLUMN = "defect_type"
DEFECT_HEALTHY = "healthy"
DEFECT_SINGLE = "single_parameter_outlier"
DEFECT_MULTI = "multivariate_latent"


@dataclass(frozen=True)
class GeneratorConfig:
    """Configuration for :func:`generate_burn_in_data`."""

    seed: int = 42
    n_lots_range: Tuple[int, int] = (8, 12)
    chips_per_lot_range: Tuple[int, int] = (200, 300)
    defect_rate_range: Tuple[float, float] = (0.03, 0.12)
    single_param_fraction: float = 0.5
    safety_ceiling_range: Tuple[float, float] = (0.92, 0.96)
    healthy_ceiling_range: Tuple[float, float] = (0.80, 0.88)
    burn_in_hours: float = 24.0
    output_path: str = DEFAULT_OUTPUT_PATH

    def __post_init__(self) -> None:
        if not 1 <= self.n_lots_range[0] <= self.n_lots_range[1]:
            raise ValueError("n_lots_range must satisfy 1 <= low <= high")
        if not 2 <= self.chips_per_lot_range[0] <= self.chips_per_lot_range[1]:
            raise ValueError("chips_per_lot_range must satisfy 2 <= low <= high")
        lo, hi = self.defect_rate_range
        if not 0.0 <= lo <= hi < 1.0:
            raise ValueError("defect_rate_range must satisfy 0 <= low <= high < 1")
        c_lo, c_hi = self.safety_ceiling_range
        if not 0.0 < c_lo <= c_hi < 1.0:
            raise ValueError("safety_ceiling_range must lie inside (0, 1)")
        if not 0.0 <= self.single_param_fraction <= 1.0:
            raise ValueError("single_param_fraction must be within [0, 1]")


@dataclass(frozen=True)
class LotProfile:
    """Lot-specific nominal operating point and process behaviour."""

    lot_id: str
    n_chips: int
    defect_rate: float
    median: Dict[str, float]
    sigma: Dict[str, float]
    drift_amp: Dict[str, float]
    edge_effect: bool


def _draw_lot_profiles(cfg: GeneratorConfig, rng: np.random.Generator) -> List[LotProfile]:
    n_lots = int(rng.integers(cfg.n_lots_range[0], cfg.n_lots_range[1] + 1))
    profiles: List[LotProfile] = []
    for idx in range(n_lots):
        lot_id = f"LOT-{chr(ord('A') + idx)}" if idx < 26 else f"LOT-{idx + 1:02d}"
        profiles.append(
            LotProfile(
                lot_id=lot_id,
                n_chips=int(rng.integers(cfg.chips_per_lot_range[0], cfg.chips_per_lot_range[1] + 1)),
                defect_rate=float(rng.uniform(*cfg.defect_rate_range)),
                median={
                    "Iddq": float(rng.uniform(9.0, 26.0)),
                    "leakage": float(rng.uniform(4.5, 11.0)),
                    "delay": float(rng.uniform(8.0, 10.8)),
                },
                sigma={
                    "Iddq": float(rng.uniform(0.28, 0.42)),
                    "leakage": float(rng.uniform(0.30, 0.45)),
                    "delay": float(rng.uniform(0.04, 0.07)),
                },
                drift_amp={
                    "Iddq": float(rng.uniform(0.03, 0.07)),
                    "leakage": float(rng.uniform(0.03, 0.07)),
                    "delay": float(rng.uniform(0.006, 0.015)),
                },
                edge_effect=bool(rng.random() < 0.4),
            )
        )
    return profiles


def _healthy_population(
    lot: LotProfile, cfg: GeneratorConfig, rng: np.random.Generator
) -> Tuple[Dict[str, np.ndarray], Dict[str, np.ndarray], np.ndarray]:
    """Draw healthy 0h / 24h measurements and wafer radius for one lot."""
    n = lot.n_chips
    vth = rng.standard_normal(n)  # shared threshold-voltage shift
    radius = np.clip(rng.beta(4.0, 2.0, n), 0.0, 1.0)

    def tail_boost(prob: float, scale: float) -> np.ndarray:
        hit = rng.random(n) < prob
        return 1.0 + scale * rng.weibull(1.1, n) * hit

    edge = np.ones(n)
    if lot.edge_effect:
        edge = 1.0 + rng.uniform(0.08, 0.20) * np.clip((radius - 0.75) / 0.25, 0.0, 1.0)

    z_i = 0.70 * (-vth) + 0.71 * rng.standard_normal(n)
    z_l = 0.75 * (-vth) + 0.66 * rng.standard_normal(n)
    z_d = 0.60 * vth + 0.80 * rng.standard_normal(n)

    v0 = {
        "Iddq": lot.median["Iddq"] * np.exp(lot.sigma["Iddq"] * z_i) * tail_boost(0.06, 0.25) * edge,
        "leakage": lot.median["leakage"] * np.exp(lot.sigma["leakage"] * z_l) * tail_boost(0.06, 0.25) * edge,
        "delay": lot.median["delay"]
        * np.exp(lot.sigma["delay"] * z_d)
        * (1.0 + 0.012 * rng.weibull(1.3, n))
        * (1.0 + 0.5 * (edge - 1.0)),
    }

    # Saturating, right-skewed thermal drift.
    tau = np.exp(rng.normal(np.log(36.0), 0.35, n))
    saturation = (1.0 - np.exp(-cfg.burn_in_hours / tau)) / (1.0 - np.exp(-cfg.burn_in_hours / 36.0))
    drift_i = lot.drift_amp["Iddq"] * np.exp(rng.normal(0.0, 0.5, n)) * saturation
    drift_l = lot.drift_amp["leakage"] * np.exp(rng.normal(0.0, 0.5, n)) * saturation
    drift_d = (
        lot.drift_amp["delay"] * np.exp(rng.normal(0.0, 0.45, n)) * saturation * (1.0 + 0.5 * drift_l)
    )
    if lot.edge_effect:  # thermal non-uniformity in the burn-in oven
        drift_i = drift_i * (1.0 + 0.5 * (edge - 1.0) * 5.0)
        drift_l = drift_l * (1.0 + 0.5 * (edge - 1.0) * 5.0)

    drift = {"Iddq": drift_i, "leakage": drift_l, "delay": drift_d}
    v24 = {p: v0[p] * (1.0 + drift[p]) * np.exp(rng.normal(0.0, 0.004, n)) for p in PARAMS}

    # Healthy chips are kept comfortably inside the datasheet.
    for p in PARAMS:
        cap = STATIC_LIMITS[p] * rng.uniform(*cfg.healthy_ceiling_range, size=n)
        v24[p] = np.minimum(v24[p], cap)
        v0[p] = np.minimum(v0[p], v24[p] / 1.004)
    return v0, v24, radius


def _inject_defects(
    lot: LotProfile,
    cfg: GeneratorConfig,
    rng: np.random.Generator,
    v0: Dict[str, np.ndarray],
    v24: Dict[str, np.ndarray],
    radius: np.ndarray,
) -> np.ndarray:
    """Inject defects in-place and return the per-chip defect-type labels."""
    n = lot.n_chips
    labels = np.full(n, DEFECT_HEALTHY, dtype=object)
    n_defects = int(round(lot.defect_rate * n))
    if lot.defect_rate > 0:
        n_defects = max(n_defects, 1)
    n_defects = min(n_defects, n)

    weights = 1.0 + (3.0 if lot.edge_effect else 1.0) * radius ** 2
    chosen = rng.choice(n, size=n_defects, replace=False, p=weights / weights.sum())

    for i in chosen:
        ceiling = rng.uniform(*cfg.safety_ceiling_range)
        cap = {p: ceiling * STATIC_LIMITS[p] for p in PARAMS}

        # A defect deviates from its *lot*, so a chip whose healthy draw fell
        # in the low tail is re-based to the lot median before degradation.
        for p in PARAMS:
            ratio = v24[p][i] / v0[p][i]
            v0[p][i] = max(v0[p][i], lot.median[p])
            v24[p][i] = v0[p][i] * ratio

        if rng.random() < cfg.single_param_fraction:
            labels[i] = DEFECT_SINGLE
            param = str(rng.choice(PARAMS, p=[0.35, 0.45, 0.20]))
            if param == "delay":
                mult0 = 1.25 + rng.gamma(2.0, 0.05)
            else:
                mult0 = 3.0 + rng.gamma(2.0, 0.6)
            extra_drift = rng.uniform(0.0, 0.15)
            v0[param][i] *= mult0
            v24[param][i] *= mult0 * (1.0 + extra_drift)
        else:
            labels[i] = DEFECT_MULTI
            c = 0.75 + rng.gamma(2.5, 0.25)  # latent-defect severity (right-skewed)
            jitter = lambda: float(np.exp(rng.normal(0.0, 0.2)))  # noqa: E731
            m0_l = 1.0 + 0.40 * c * jitter()
            m0_i = 1.0 + 0.35 * c * jitter()
            m0_d = 1.0 + 0.012 * c * jitter()
            extra_l = 0.20 * c ** 1.3 * jitter()
            extra_i = 0.18 * c ** 1.3 * jitter()
            extra_d = 0.012 * (extra_l / 0.20) ** 1.3 * jitter()  # non-linear coupling
            v0["leakage"][i] *= m0_l
            v0["Iddq"][i] *= m0_i
            v0["delay"][i] *= m0_d
            v24["leakage"][i] *= m0_l * (1.0 + extra_l)
            v24["Iddq"][i] *= m0_i * (1.0 + extra_i)
            v24["delay"][i] *= m0_d * (1.0 + extra_d)

        # Static ceiling clipping guardrail: defects must pass 1-D screening.
        for p in PARAMS:
            v24[p][i] = min(v24[p][i], cap[p])
            v0[p][i] = min(v0[p][i], v24[p][i] / 1.004)
    return labels


def generate_burn_in_data(config: GeneratorConfig | None = None, save: bool = True) -> pd.DataFrame:
    """Generate the multi-lot burn-in dataset (and optionally save it to CSV)."""
    cfg = config or GeneratorConfig()
    rng = np.random.default_rng(cfg.seed)
    profiles = _draw_lot_profiles(cfg, rng)

    frames: List[pd.DataFrame] = []
    for lot_idx, lot in enumerate(profiles):
        v0, v24, radius = _healthy_population(lot, cfg, rng)
        labels = _inject_defects(lot, cfg, rng, v0, v24, radius)
        frame = pd.DataFrame(
            {
                "serial_number": [f"SN{lot_idx + 1:02d}-{k + 1:04d}" for k in range(lot.n_chips)],
                "lot_id": lot.lot_id,
                **{f"{p}_0h": v0[p] for p in PARAMS},
                **{f"{p}_24h": v24[p] for p in PARAMS},
                "wafer_radius_norm": radius,
                DEFECT_TYPE_COLUMN: labels,
            }
        )
        frame[LABEL_COLUMN] = (frame[DEFECT_TYPE_COLUMN] != DEFECT_HEALTHY).astype(int)
        frames.append(frame)
        logger.info(
            "%s: %d chips, target defect rate %.1f%%, actual %d, edge effect=%s",
            lot.lot_id,
            lot.n_chips,
            100 * lot.defect_rate,
            int(frame[LABEL_COLUMN].sum()),
            lot.edge_effect,
        )

    data = pd.concat(frames, ignore_index=True)
    ordered = [
        "serial_number",
        "lot_id",
        *[f"{p}_0h" for p in PARAMS],
        *[f"{p}_24h" for p in PARAMS],
        "wafer_radius_norm",
        LABEL_COLUMN,
        DEFECT_TYPE_COLUMN,
    ]
    data = data[ordered]

    escaped = verify_static_guardrail(data)
    if escaped:
        raise RuntimeError(f"{escaped} injected defect(s) violate the static-limit guardrail.")

    if save:
        path = Path(cfg.output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data.to_csv(path, index=False)
        logger.info("Saved %d chips (%d lots) to %s", len(data), len(profiles), path)
    return data


def verify_static_guardrail(data: pd.DataFrame) -> int:
    """Return how many labelled defects would be caught by static 1-D limits."""
    defects = data[data[LABEL_COLUMN] == 1]
    breach = np.zeros(len(defects), dtype=bool)
    for p in PARAMS:
        for cp in ("0h", "24h"):
            breach |= defects[f"{p}_{cp}"].to_numpy() > STATIC_LIMITS[p]
    return int(breach.sum())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    generate_burn_in_data()
