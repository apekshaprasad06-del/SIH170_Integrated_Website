"""Isolation Forest detection engine with recall-biased threshold calibration."""

from __future__ import annotations

import logging
from typing import Dict, Optional, Sequence, Union

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix, fbeta_score, precision_score, recall_score

from preprocessing import DPAT_SIGMA_THRESHOLD, EPSILON, FEATURE_COLUMNS, MAD_TO_SIGMA

logger = logging.getLogger(__name__)

ArrayLike = Union[pd.DataFrame, np.ndarray]


class DynamicOutlierDetector:
    """Isolation Forest + DPAT union detector.

    ``Flagged = IF_Flag OR DPAT_Flag``.  The Isolation Forest threshold is
    calibrated (when labels are available) to reach ``target_recall`` on the
    *union* rule while maximising the F2-score, which penalises false
    negatives four times as much as false positives.
    """

    def __init__(
        self,
        n_estimators: int = 200,
        max_samples: int = 256,
        contamination: Union[str, float] = "auto",
        random_state: int = 42,
        target_recall: float = 0.98,
        beta: float = 2.0,
        dpat_sigma: float = DPAT_SIGMA_THRESHOLD,
        safety_margin: float = 0.005,
        n_jobs: int = -1,
    ) -> None:
        if not 0.0 < target_recall <= 1.0:
            raise ValueError("target_recall must lie in (0, 1].")
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.contamination = contamination
        self.random_state = random_state
        self.target_recall = target_recall
        self.beta = beta
        self.dpat_sigma = dpat_sigma
        self.safety_margin = safety_margin
        self.n_jobs = n_jobs

        self.model_: Optional[IsolationForest] = None
        self.feature_names_: list = list(FEATURE_COLUMNS)
        self.threshold_: float = 0.5
        self.default_threshold_: float = 0.5
        self.score_scale_: float = 0.05
        self.calibration_report_: Dict[str, float] = {}

    # ------------------------------------------------------------------ #
    def _as_array(self, X: ArrayLike) -> np.ndarray:
        arr = X[self.feature_names_].to_numpy(dtype=float) if isinstance(X, pd.DataFrame) else np.asarray(X, float)
        if arr.ndim != 2 or arr.shape[1] != len(self.feature_names_):
            raise ValueError(f"Expected {len(self.feature_names_)} feature columns, got shape {arr.shape}.")
        return np.nan_to_num(arr, nan=0.0, posinf=1e3, neginf=-1e3)

    def _require_fit(self) -> IsolationForest:
        if self.model_ is None:
            raise RuntimeError("Detector is not fitted; call fit() first.")
        return self.model_

    # ------------------------------------------------------------------ #
    def fit(self, X: ArrayLike) -> "DynamicOutlierDetector":
        """Fit the Isolation Forest (unsupervised) on the 9-feature matrix."""
        arr = self._as_array(X)
        if arr.shape[0] < 2:
            raise ValueError("At least two samples are required to fit the model.")
        self.model_ = IsolationForest(
            n_estimators=self.n_estimators,
            max_samples=min(self.max_samples, arr.shape[0]),
            contamination=self.contamination,
            random_state=self.random_state,
            n_jobs=self.n_jobs,
        )
        self.model_.fit(arr)
        scores = self.anomaly_scores(arr)
        _, sigma, _ = _robust_scale(scores)
        self.score_scale_ = max(sigma, 1e-3)
        self.threshold_ = float(-self.model_.offset_)
        self.default_threshold_ = self.threshold_
        logger.info(
            "Isolation Forest fitted on %d chips (%d trees); default threshold %.4f, score scale %.4f.",
            arr.shape[0],
            self.n_estimators,
            self.threshold_,
            self.score_scale_,
        )
        return self

    def anomaly_scores(self, X: ArrayLike) -> np.ndarray:
        """Anomaly score in (0, 1); larger means more anomalous."""
        model = self._require_fit()
        return -model.score_samples(self._as_array(X))

    # ------------------------------------------------------------------ #
    def calibrate_threshold(
        self,
        X: ArrayLike,
        y_true: Sequence[int],
        dpat_flags: Optional[Sequence[bool]] = None,
    ) -> float:
        """Choose the IF score threshold that reaches the recall target.

        Among all thresholds whose union-rule recall is at least
        ``target_recall`` the one with the highest F2-score is selected.  If
        the target is unreachable, the highest-recall (then highest-F2)
        threshold is used instead.  Candidates are capped at the stock Isolation
        Forest threshold (the IF is never made less sensitive than default).
        ``safety_margin`` is subtracted afterwards
        to bias the final threshold toward fewer false negatives.
        """
        scores = self.anomaly_scores(X)
        y = np.asarray(y_true).astype(bool)
        if y.shape[0] != scores.shape[0]:
            raise ValueError("X and y_true must have the same number of rows.")
        dpat = np.zeros_like(y) if dpat_flags is None else np.asarray(dpat_flags).astype(bool)

        if not y.any():
            logger.warning("No positive labels supplied; keeping default threshold %.4f.", self.threshold_)
            return self.threshold_

        # The IF must never be less sensitive than the stock model: without this
        # cap, F2 would happily disable the IF whenever DPAT alone hits the target.
        candidates = np.unique(scores[scores <= self.default_threshold_])
        if candidates.size == 0:
            candidates = np.array([self.default_threshold_])
        if candidates.size > 4000:
            candidates = np.unique(np.quantile(scores, np.linspace(0.0, 1.0, 4000)))

        n_pos = float(y.sum())
        b2 = self.beta ** 2
        recalls = np.empty(candidates.size)
        f_beta = np.empty(candidates.size)
        for k, thr in enumerate(candidates):
            flagged = (scores >= thr) | dpat
            tp = float(np.sum(flagged & y))
            fp = float(np.sum(flagged & ~y))
            fn = n_pos - tp
            recalls[k] = tp / n_pos
            denom = (1.0 + b2) * tp + b2 * fn + fp
            f_beta[k] = (1.0 + b2) * tp / denom if denom > 0 else 0.0

        eligible = np.flatnonzero(recalls >= self.target_recall)
        if eligible.size:
            best = eligible[np.lexsort((candidates[eligible], f_beta[eligible]))[-1]]
            reached = True
        else:
            order = np.lexsort((f_beta, recalls))
            best = order[-1]
            reached = False
            logger.warning(
                "Recall target %.2f unreachable on calibration set (best %.3f).",
                self.target_recall,
                recalls[best],
            )

        self.threshold_ = float(candidates[best] - self.safety_margin)
        self.calibration_report_ = {
            "threshold": self.threshold_,
            "calibration_recall": float(recalls[best]),
            "calibration_f2": float(f_beta[best]),
            "target_reached": float(reached),
            "n_positive": n_pos,
        }
        logger.info(
            "Calibrated threshold %.4f (union recall %.3f, F%.0f %.3f, margin %.3f).",
            self.threshold_,
            recalls[best],
            self.beta,
            f_beta[best],
            self.safety_margin,
        )
        return self.threshold_

    def set_threshold_by_contamination(self, X: ArrayLike, contamination: float) -> float:
        """Label-free fall-back: flag the top ``contamination`` fraction by score."""
        if not 0.0 < contamination < 1.0:
            raise ValueError("contamination must lie in (0, 1).")
        scores = self.anomaly_scores(X)
        self.threshold_ = float(np.quantile(scores, 1.0 - contamination))
        logger.info("Label-free threshold %.4f (top %.1f%%).", self.threshold_, 100 * contamination)
        return self.threshold_

    # ------------------------------------------------------------------ #
    def predict(
        self,
        X: ArrayLike,
        dpat_flags: Optional[Sequence[bool]] = None,
        dpat_max_z: Optional[Sequence[float]] = None,
    ) -> pd.DataFrame:
        """Return IF score, IF flag, DPAT flag, union flag and rejection confidence."""
        scores = self.anomaly_scores(X)
        index = X.index if isinstance(X, pd.DataFrame) else pd.RangeIndex(len(scores))
        dpat = np.zeros(scores.shape[0], bool) if dpat_flags is None else np.asarray(dpat_flags).astype(bool)
        zmax = np.zeros(scores.shape[0]) if dpat_max_z is None else np.asarray(dpat_max_z, dtype=float)

        if_flag = scores >= self.threshold_
        flagged = if_flag | dpat
        confidence = self.confidence(scores, zmax)
        return pd.DataFrame(
            {
                "if_score": scores,
                "if_flag": if_flag,
                "dpat_flag_rule": dpat,
                "flagged": flagged,
                "rejection_confidence": confidence,
            },
            index=index,
        )

    def confidence(self, scores: np.ndarray, dpat_max_z: Optional[np.ndarray] = None) -> np.ndarray:
        """Rejection confidence in [0, 1].

        IF component: logistic in the score margin over the threshold (0.5 at
        the threshold).  DPAT component: 0.5 at ``dpat_sigma`` rising
        asymptotically to 1.  The larger of the two is reported.
        """
        scores = np.asarray(scores, dtype=float)
        margin = (scores - self.threshold_) / (0.5 * self.score_scale_)
        conf_if = 1.0 / (1.0 + np.exp(-np.clip(margin, -50.0, 50.0)))
        if dpat_max_z is None:
            return np.clip(conf_if, 0.0, 1.0)
        z = np.abs(np.asarray(dpat_max_z, dtype=float))
        over = z >= self.dpat_sigma
        conf_dpat = np.where(
            over,
            0.5 + 0.5 * (1.0 - np.exp(-(z - self.dpat_sigma) / self.dpat_sigma)),
            0.5 * z / self.dpat_sigma,
        )
        return np.clip(np.maximum(conf_if, conf_dpat), 0.0, 1.0)

    # ------------------------------------------------------------------ #
    @staticmethod
    def evaluate(y_true: Sequence[int], y_pred: Sequence[bool]) -> Dict[str, object]:
        """Recall, precision, F1, F2 and the confusion matrix ``[[TN, FP], [FN, TP]]``."""
        yt = np.asarray(y_true).astype(int)
        yp = np.asarray(y_pred).astype(int)
        cm = confusion_matrix(yt, yp, labels=[0, 1])
        tn, fp, fn, tp = (int(v) for v in cm.ravel())
        return {
            "recall": float(recall_score(yt, yp, zero_division=0)),
            "precision": float(precision_score(yt, yp, zero_division=0)),
            "f1": float(fbeta_score(yt, yp, beta=1.0, zero_division=0)),
            "f2": float(fbeta_score(yt, yp, beta=2.0, zero_division=0)),
            "confusion_matrix": [[tn, fp], [fn, tp]],
            "tn": tn,
            "fp": fp,
            "fn": fn,
            "tp": tp,
            "n_samples": int(yt.size),
            "n_positive": int(yt.sum()),
        }


def _robust_scale(values: np.ndarray) -> tuple:
    """Median and MAD-based sigma with an epsilon floor (score-scale helper)."""
    arr = np.asarray(values, dtype=float)
    median = float(np.median(arr))
    sigma = MAD_TO_SIGMA * float(np.median(np.abs(arr - median)))
    if sigma <= EPSILON:
        sigma = float(np.std(arr))
    return median, max(sigma, EPSILON), "mad"
