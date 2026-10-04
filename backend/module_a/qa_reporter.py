"""Root-cause classification, risk assignment and QA inspection certificates."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence, Union

import numpy as np
import pandas as pd

from preprocessing import DISPLAY_LABELS, FEATURE_COLUMNS, FEATURE_DISPLAY, PARAMS, STATIC_LIMITS, UNITS

logger = logging.getLogger(__name__)

STATIC_BREACH = "STATIC_BREACH"
SINGLE_PARAMETER = "SINGLE_PARAMETER_PEER_OUTLIER"
MULTIVARIATE = "MULTIVARIATE_LATENT_DRIFT"

CRITICAL = "CRITICAL"
HIGH = "HIGH"
ELEVATED = "ELEVATED"

ELEVATED_PARAM_Z = 3.0
CRITICAL_CONFIDENCE = 0.85
HIGH_CONFIDENCE = 0.65
CRITICAL_Z = 8.0
HIGH_Z = 6.0


class QAReporter:
    """Turn detector output into classified findings and Markdown certificates."""

    def __init__(self, feature_names: Optional[Sequence[str]] = None, top_k: int = 3) -> None:
        self.feature_names: List[str] = list(feature_names or FEATURE_COLUMNS)
        self.top_k = top_k

    # ------------------------------------------------------------------ #
    @staticmethod
    def _peak_z(row: pd.Series, param: str) -> float:
        return float(
            max(abs(row[f"z_{param}_0h"]), abs(row[f"z_{param}_24h"]), abs(row[f"zdrift_{param}"]))
        )

    def classify_row(self, row: pd.Series) -> Dict[str, object]:
        """Classify one flagged chip and assign risk."""
        peaks = {p: self._peak_z(row, p) for p in PARAMS}
        elevated = [p for p in PARAMS if peaks[p] >= ELEVATED_PARAM_Z]
        dominant = max(peaks, key=peaks.get)
        pct = {p: float(row.get(f"pct_{p}", 0.0)) for p in PARAMS}
        if any(pct.values()):
            dominant = max(pct, key=pct.get)

        if bool(row.get("static_breach", False)):
            cause = STATIC_BREACH
        elif len(elevated) == 1:
            cause = SINGLE_PARAMETER
            dominant = elevated[0]
        else:
            cause = MULTIVARIATE  # >= 2 elevated parameters, or subtle IF-only compounding

        confidence = float(row.get("rejection_confidence", 0.0))
        max_z = max(peaks.values())
        if cause == STATIC_BREACH or confidence >= CRITICAL_CONFIDENCE or max_z >= CRITICAL_Z:
            risk = CRITICAL
        elif confidence >= HIGH_CONFIDENCE or max_z >= HIGH_Z:
            risk = HIGH
        else:
            risk = ELEVATED
        return {
            "root_cause": cause,
            "risk_level": risk,
            "dominant_parameter": dominant,
            "n_elevated_parameters": len(elevated),
        }

    def classify(self, results: pd.DataFrame) -> pd.DataFrame:
        """Add ``root_cause``, ``risk_level`` and ``dominant_parameter`` columns."""
        out = results.copy()
        out["root_cause"] = "NONE"
        out["risk_level"] = "NONE"
        out["dominant_parameter"] = ""
        out["n_elevated_parameters"] = 0
        flagged_idx = out.index[out["flagged"].astype(bool)]
        for idx in flagged_idx:
            info = self.classify_row(out.loc[idx])
            for key, value in info.items():
                out.loc[idx, key] = value
        counts = out.loc[flagged_idx, "root_cause"].value_counts().to_dict()
        logger.info("Root-cause classification of %d flagged chips: %s", len(flagged_idx), counts)
        return out

    # ------------------------------------------------------------------ #
    def evidence(self, row: pd.Series) -> str:
        """Plain-language inspector evidence for one chip."""
        param = str(row["dominant_parameter"]) or PARAMS[0]
        unit = UNITS[param]
        v24 = float(row[f"{param}_24h"])
        med24 = float(row[f"lot_median_{param}_24h"])
        ratio = v24 / med24 if med24 > 0 else float("nan")
        limit = STATIC_LIMITS[param]
        drift = float(row[f"drift_pct_{param}"])
        med_drift = float(row[f"lot_median_drift_pct_{param}"])
        text = (
            f"{DISPLAY_LABELS[param]} reads {v24:.2f} {unit} at 24h against a lot median of {med24:.2f} {unit} "
            f"({ratio:.2f}x lot median) and uses {100 * v24 / limit:.0f}% of the {limit:g} {unit} datasheet limit. "
            f"Drift is {drift:+.1f}% versus a lot-median drift of {med_drift:+.1f}%."
        )
        if row["root_cause"] == MULTIVARIATE:
            others = [p for p in PARAMS if p != param and self._peak_z(row, p) >= 2.0]
            if others:
                text += " Coordinated shifts also appear in " + ", ".join(DISPLAY_LABELS[p] for p in others) + "."
        if row["root_cause"] == STATIC_BREACH:
            text += f" Static datasheet breach on: {row['static_breach_params']}."
        return text

    def to_markdown(
        self,
        results: pd.DataFrame,
        attributions: np.ndarray,
        metrics: Optional[Mapping[str, object]] = None,
        waterfall_files: Optional[Mapping[str, str]] = None,
        attribution_method: str = "shap",
        max_certificates: Optional[int] = None,
    ) -> str:
        """Render the QA report.  ``results`` must already be classified."""
        if "root_cause" not in results.columns:
            results = self.classify(results)
        attr = np.asarray(attributions, dtype=float)
        pos_of = {idx: i for i, idx in enumerate(results.index)}
        flagged = results[results["flagged"].astype(bool)].sort_values("rejection_confidence", ascending=False)
        waterfall_files = waterfall_files or {}

        lines: List[str] = [
            "# QA Inspection Report - Module A Dynamic Outlier Detection",
            "",
            f"_Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} | "
            f"attribution method: {attribution_method}_",
            "",
            "## Executive Summary",
            "",
            f"- Chips screened: **{len(results)}** across **{results['lot_id'].nunique()}** lots",
            f"- Chips rejected: **{len(flagged)}** ({100 * len(flagged) / max(len(results), 1):.2f}%)",
            f"- Static-limit breaches: **{int(results['static_breach'].sum())}**",
        ]
        if len(flagged):
            causes = flagged["root_cause"].value_counts()
            risks = flagged["risk_level"].value_counts()
            lines.append("- Root causes: " + ", ".join(f"{k}: {v}" for k, v in causes.items()))
            lines.append("- Risk levels: " + ", ".join(f"{k}: {v}" for k, v in risks.items()))
        if metrics:
            lines += ["", "### Detection Metrics (ground truth available)", ""]
            lines += ["| Scope | Recall | Precision | F2 | TN | FP | FN | TP |", "|---|---|---|---|---|---|---|---|"]
            for scope, m in metrics.items():
                if not isinstance(m, Mapping) or "recall" not in m:
                    continue
                lines.append(
                    f"| {scope} | {m['recall']:.3f} | {m['precision']:.3f} | {m['f2']:.3f} | "
                    f"{m['tn']} | {m['fp']} | {m['fn']} | {m['tp']} |"
                )

        lines += ["", "## Rejected Serial Numbers", ""]
        if flagged.empty:
            lines.append("No chips were rejected.")
        else:
            lines += [
                "| Serial | Lot | Root cause | Risk | Confidence |",
                "|---|---|---|---|---|",
            ]
            for _, r in flagged.iterrows():
                lines.append(
                    f"| {r['serial_number']} | {r['lot_id']} | {r['root_cause']} | {r['risk_level']} | "
                    f"{r['rejection_confidence']:.3f} |"
                )

        lines += ["", "## Inspection Certificates", ""]
        certs = flagged if max_certificates is None else flagged.head(max_certificates)
        for n, (idx, r) in enumerate(certs.iterrows(), start=1):
            row_attr = attr[pos_of[idx]]
            top = np.argsort(row_attr)[::-1][: self.top_k]
            lines += [
                f"### Certificate {n:03d} - {r['serial_number']} ({r['lot_id']})",
                "",
                f"**Verdict:** REJECT | **Risk:** {r['risk_level']} | **Root cause:** `{r['root_cause']}` | "
                f"**Confidence:** {r['rejection_confidence']:.3f}",
                "",
                "| Parameter | 0h | 24h | Lot median (24h) | Deviation ratio | Peak robust z | Static limit used |",
                "|---|---|---|---|---|---|---|",
            ]
            for p in PARAMS:
                med = float(r[f"lot_median_{p}_24h"])
                ratio = float(r[f"{p}_24h"]) / med if med > 0 else float("nan")
                lines.append(
                    f"| {DISPLAY_LABELS[p]} | {r[f'{p}_0h']:.2f} {UNITS[p]} | {r[f'{p}_24h']:.2f} {UNITS[p]} | "
                    f"{med:.2f} {UNITS[p]} | {ratio:.2f}x | {self._peak_z(r, p):.1f} | "
                    f"{100 * float(r[f'{p}_24h']) / STATIC_LIMITS[p]:.0f}% |"
                )
            lines += [
                "",
                f"**Parameter contribution:** "
                + ", ".join(f"{DISPLAY_LABELS[p]} {float(r[f'pct_{p}']):.0f}%" for p in PARAMS),
                "",
                "**Top attribution features:** "
                + "; ".join(f"{FEATURE_DISPLAY[self.feature_names[i]]} ({row_attr[i]:+.3f})" for i in top),
                "",
                f"**Evidence:** {self.evidence(r)}",
                "",
            ]
            wf = waterfall_files.get(str(r["serial_number"]))
            if wf:
                lines += [f"![Waterfall for {r['serial_number']}]({wf})", ""]
        if max_certificates is not None and len(flagged) > max_certificates:
            lines.append(f"_Certificates truncated to the top {max_certificates} of {len(flagged)} rejected chips._")
        return "\n".join(lines) + "\n"

    def write_markdown(self, path: Union[str, Path], markdown: str) -> Path:
        out = Path(path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(markdown, encoding="utf-8")
        logger.info("QA report written to %s", out)
        return out
