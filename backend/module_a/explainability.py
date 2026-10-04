"""SHAP-based root-cause attribution for the Isolation Forest.

Positive attributions always mean "pushes the chip toward rejection".  The 9
model features are aggregated back into the 3 physical parameters (Iddq,
leakage, delay) as percentage contributions.  If SHAP is unavailable or fails
at runtime, a normalised parameter-deviation attribution is used instead.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Optional, Sequence, Tuple, Union

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from model_isolation_forest import DynamicOutlierDetector  # noqa: E402
from preprocessing import (  # noqa: E402
    DISPLAY_LABELS,
    EPSILON,
    FEATURE_COLUMNS,
    FEATURE_DISPLAY,
    FEATURE_TO_PARAM,
    PARAMS,
)

try:  # SHAP is optional at import time so the fallback path stays usable.
    import shap  # type: ignore

    SHAP_IMPORTED = True
except Exception as _exc:  # pragma: no cover - depends on environment
    shap = None  # type: ignore
    SHAP_IMPORTED = False
    logging.getLogger(__name__).warning("SHAP import failed (%s); fallback attribution will be used.", _exc)

logger = logging.getLogger(__name__)

PARAM_COLORS = {"Iddq": "#d62728", "leakage": "#ff7f0e", "delay": "#1f77b4"}


class OutlierExplainer:
    """Explain Isolation Forest rejections in physical terms."""

    def __init__(self, detector: DynamicOutlierDetector, feature_names: Optional[Sequence[str]] = None) -> None:
        self.detector = detector
        self.feature_names: List[str] = list(feature_names or FEATURE_COLUMNS)
        self.method_: str = "fallback"
        self._explainer = None
        self._sign: float = -1.0  # SHAP explains "normality"; invert for rejection
        self._sign_resolved: bool = False
        self._base_value: float = 0.0

        if not SHAP_IMPORTED:
            logger.warning("SHAP unavailable; using normalised-deviation fallback attribution.")
            return
        try:
            self._explainer = shap.TreeExplainer(detector.model_)
            expected = float(np.ravel(np.asarray(self._explainer.expected_value, dtype=float))[0])
            self._base_value = self._sign * expected
            self.method_ = "shap"
            logger.info("SHAP TreeExplainer initialised.")
        except Exception as exc:
            logger.warning("SHAP TreeExplainer failed (%s); using fallback attribution.", exc)
            self._explainer = None

    # ------------------------------------------------------------------ #
    def _matrix(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        if isinstance(X, pd.DataFrame):
            arr = X[self.feature_names].to_numpy(dtype=float)
        else:
            arr = np.asarray(X, dtype=float)
        return np.nan_to_num(arr, nan=0.0, posinf=1e3, neginf=-1e3)

    def _resolve_sign(self, raw: np.ndarray, X_arr: np.ndarray) -> None:
        """Verify the SHAP sign convention against the detector's own scores."""
        if self._sign_resolved or raw.shape[0] < 20:
            return
        summed = raw.sum(axis=1)
        scores = self.detector.anomaly_scores(X_arr)
        if np.std(summed) < EPSILON or np.std(scores) < EPSILON:
            return
        corr = float(np.corrcoef(summed, scores)[0, 1])
        expected_sign = -1.0 if corr < 0 else 1.0
        if expected_sign != self._sign:
            logger.warning("SHAP sign convention differs from expectation (corr=%.2f); adjusting.", corr)
            self._sign = expected_sign
            self._base_value = -self._base_value
        self._sign_resolved = True

    def _fallback(self, X_arr: np.ndarray) -> np.ndarray:
        """Normalised parameter deviation: |z| of each feature (>= 0)."""
        return np.abs(X_arr)

    # ------------------------------------------------------------------ #
    def explain(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Return an ``(n, 9)`` attribution matrix (positive = toward rejection)."""
        X_arr = self._matrix(X)
        if self._explainer is not None:
            try:
                raw = self._explainer.shap_values(X_arr)
                if isinstance(raw, list):
                    raw = raw[0]
                raw = np.asarray(raw, dtype=float)
                if raw.shape != X_arr.shape:
                    raise ValueError(f"Unexpected SHAP output shape {raw.shape}")
                self._resolve_sign(raw, X_arr)
                self.method_ = "shap"
                return self._sign * raw
            except Exception as exc:
                logger.warning("SHAP evaluation failed (%s); switching to fallback attribution.", exc)
                self._explainer = None
        self.method_ = "fallback"
        self._base_value = 0.0
        return self._fallback(X_arr)

    def parameter_contributions(self, attributions: np.ndarray) -> pd.DataFrame:
        """Aggregate feature attributions into % contribution per physical parameter."""
        attr = np.asarray(attributions, dtype=float)
        n = attr.shape[0]

        def aggregate(matrix: np.ndarray) -> np.ndarray:
            out = np.zeros((n, len(PARAMS)))
            for j, name in enumerate(self.feature_names):
                out[:, PARAMS.index(FEATURE_TO_PARAM[name])] += matrix[:, j]
            return out

        per_param = aggregate(np.clip(attr, 0.0, None))
        totals = per_param.sum(axis=1)
        weak = totals <= EPSILON
        if weak.any():  # nothing pushes toward rejection: use magnitudes instead
            per_param[weak] = aggregate(np.abs(attr))[weak]
            totals = per_param.sum(axis=1)
        pct = np.full((n, len(PARAMS)), 100.0 / len(PARAMS))
        ok = totals > EPSILON
        pct[ok] = per_param[ok] / totals[ok, None] * 100.0
        return pd.DataFrame(pct, columns=[f"pct_{p}" for p in PARAMS])

    def top_features(self, attribution_row: np.ndarray, k: int = 3) -> List[Tuple[str, float]]:
        """Top-``k`` features pushing toward rejection as ``(feature, value)``."""
        order = np.argsort(attribution_row)[::-1][:k]
        return [(self.feature_names[i], float(attribution_row[i])) for i in order]

    # ------------------------------------------------------------------ #
    def waterfall_plot(self, x_row: pd.Series, path: Union[str, Path], title: Optional[str] = None) -> Path:
        """Save a waterfall plot for one chip and return the file path."""
        out = Path(path)
        out.parent.mkdir(parents=True, exist_ok=True)
        x_df = x_row[self.feature_names].to_frame().T.astype(float)
        attr = self.explain(x_df)[0]
        values = x_df.to_numpy(dtype=float)[0]
        names = [FEATURE_DISPLAY[f] for f in self.feature_names]
        heading = title or "Rejection attribution"

        if self.method_ == "shap" and shap is not None:
            try:
                explanation = shap.Explanation(
                    values=attr, base_values=self._base_value, data=values, feature_names=names
                )
                plt.figure(figsize=(9, 6))
                shap.plots.waterfall(explanation, max_display=9, show=False)
                fig = plt.gcf()
                fig.suptitle(heading, fontsize=11, y=1.0)
                fig.savefig(out, dpi=150, bbox_inches="tight")
                plt.close(fig)
                return out
            except Exception as exc:
                logger.warning("SHAP waterfall failed (%s); drawing manual waterfall.", exc)
                plt.close("all")
        return self._manual_waterfall(attr, values, names, heading, out)

    def _manual_waterfall(
        self, attr: np.ndarray, values: np.ndarray, names: List[str], heading: str, out: Path
    ) -> Path:
        order = np.argsort(np.abs(attr))
        fig, ax = plt.subplots(figsize=(9, 6))
        running = self._base_value
        for pos, i in enumerate(order):
            colour = "#d62728" if attr[i] >= 0 else "#1f77b4"
            ax.barh(pos, attr[i], left=running, color=colour, alpha=0.85)
            running += attr[i]
        ax.set_yticks(range(len(order)))
        ax.set_yticklabels([f"{names[i]} = {values[i]:+.2f}" for i in order])
        ax.axvline(self._base_value, color="grey", linestyle="--", linewidth=0.8)
        ax.set_xlabel("Cumulative attribution toward rejection")
        ax.set_title(heading)
        fig.tight_layout()
        fig.savefig(out, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return out

    def summary_plot(
        self,
        contributions: pd.DataFrame,
        path: Union[str, Path],
        mask: Optional[Sequence[bool]] = None,
        title: str = "Mean parameter contribution for rejected chips",
    ) -> Path:
        """Bar plot of the mean % contribution per physical parameter."""
        out = Path(path)
        out.parent.mkdir(parents=True, exist_ok=True)
        subset = contributions if mask is None else contributions.loc[np.asarray(mask, dtype=bool)]
        if subset.empty:
            subset = contributions
        means = [float(subset[f"pct_{p}"].mean()) for p in PARAMS]
        fig, ax = plt.subplots(figsize=(8, 4))
        bars = ax.barh([DISPLAY_LABELS[p] for p in PARAMS], means, color=[PARAM_COLORS[p] for p in PARAMS])
        for bar, val in zip(bars, means):
            ax.text(val + 0.8, bar.get_y() + bar.get_height() / 2, f"{val:.1f}%", va="center")
        ax.set_xlim(0, max(100.0, max(means) + 10.0))
        ax.set_xlabel("Mean contribution to rejection (%)")
        ax.set_title(title)
        ax.invert_yaxis()
        fig.tight_layout()
        fig.savefig(out, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return out
