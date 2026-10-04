"""Aerospace QA Inspection Certificate - dedicated QA report viewer for Module A.

Runs the existing backend pipeline once (cached) and renders only the QA
inspection report that identifies the rejected chips.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, Optional

import matplotlib

matplotlib.use("Agg")  # prevent GUI-backend threading errors under Streamlit

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402
from sklearn.model_selection import train_test_split  # noqa: E402

from data_generator import LABEL_COLUMN, GeneratorConfig, generate_burn_in_data  # noqa: E402
from explainability import OutlierExplainer  # noqa: E402
from model_isolation_forest import DynamicOutlierDetector  # noqa: E402
from preprocessing import FEATURE_COLUMNS, RAW_COLUMNS, preprocess  # noqa: E402
from qa_reporter import QAReporter  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s")
logger = logging.getLogger("module_a_app")

BASE_DIR = Path(__file__).resolve().parent
CANDIDATE_FILES = ("burn_in_lot_data.csv", "Hackathon(SIH).csv")
SEED = 42


def _load_or_generate() -> tuple[pd.DataFrame, str]:
    """Auto-detect a dataset next to the app; otherwise synthesise one."""
    required = {"serial_number", "lot_id", *RAW_COLUMNS}
    for name in CANDIDATE_FILES:
        path = BASE_DIR / name
        if not path.exists():
            continue
        df = pd.read_csv(path)
        if required.issubset(df.columns):
            logger.info("Loaded %d rows from %s", len(df), path)
            return df, name
        logger.warning("%s is missing required columns %s; skipping.", name, sorted(required - set(df.columns)))

    logger.info("No usable dataset found; generating synthetic burn-in data.")
    cfg = GeneratorConfig(seed=SEED, output_path=str(BASE_DIR / CANDIDATE_FILES[0]))
    return generate_burn_in_data(cfg, save=True), f"{CANDIDATE_FILES[0]} (generated)"


@st.cache_resource(show_spinner="Running burn-in screening pipeline...")
def run_pipeline() -> Dict[str, object]:
    """Execute preprocessing, detection, explanation and QA reporting once."""
    raw, source = _load_or_generate()
    df = preprocess(raw)
    X = df[FEATURE_COLUMNS]

    y: Optional[np.ndarray] = df[LABEL_COLUMN].to_numpy(dtype=int) if LABEL_COLUMN in df.columns else None
    detector = DynamicOutlierDetector(random_state=SEED)
    detector.fit(X)

    cal_mask = np.ones(len(df), dtype=bool)
    if y is not None and y.sum() > 1 and (y == 0).sum() > 1:
        cal_idx, _ = train_test_split(np.arange(len(df)), train_size=0.5, stratify=y, random_state=SEED)
        cal_mask = np.zeros(len(df), dtype=bool)
        cal_mask[cal_idx] = True
        detector.calibrate_threshold(X.iloc[cal_idx], y[cal_idx], df["dpat_flag"].to_numpy()[cal_idx])
    else:
        detector.set_threshold_by_contamination(X, 0.08)

    pred = detector.predict(X, df["dpat_flag"].to_numpy(), df["dpat_max_abs_z"].to_numpy())
    results = pd.concat([df, pred], axis=1)

    metrics: Dict[str, object] = {}
    if y is not None:
        flagged = results["flagged"].to_numpy()
        metrics["Full population"] = detector.evaluate(y, flagged)
        if (~cal_mask).any():
            metrics["Held-out split"] = detector.evaluate(y[~cal_mask], flagged[~cal_mask])

    explainer = OutlierExplainer(detector)
    attributions = explainer.explain(X)
    contributions = explainer.parameter_contributions(attributions)
    contributions.index = results.index
    results = pd.concat([results, contributions], axis=1)

    reporter = QAReporter()
    results = reporter.classify(results)
    report_md = reporter.to_markdown(
        results,
        attributions,
        metrics=metrics or None,
        attribution_method=explainer.method_,
    )

    n_total = len(results)
    n_rejected = int(results["flagged"].sum())
    return {
        "report_md": report_md,
        "results_csv": results.to_csv(index=False).encode("utf-8"),
        "n_chips": n_total,
        "n_lots": int(results["lot_id"].nunique()),
        "n_rejected": n_rejected,
        "rejection_rate": 100.0 * n_rejected / max(n_total, 1),
        "source": source,
    }


def main() -> None:
    st.set_page_config(page_title="Aerospace QA Inspection Certificate", page_icon="🛰️", layout="wide")
    st.title("Aerospace QA Inspection Certificate")
    st.caption("Module A - Dynamic outlier detection for ESS burn-in screening (SIH PS-170)")

    try:
        out = run_pipeline()
    except Exception as exc:  # surface a readable error instead of a stack trace
        logger.exception("Pipeline failed.")
        st.error(f"The screening pipeline failed: {exc}")
        st.stop()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Chips Evaluated", f"{out['n_chips']:,}")
    c2.metric("Lots Evaluated", f"{out['n_lots']:,}")
    c3.metric("Total Rejected", f"{out['n_rejected']:,}")
    c4.metric("Rejection Rate", f"{out['rejection_rate']:.2f}%")
    st.caption(f"Data source: {out['source']}")

    d1, d2, _ = st.columns([1, 1, 3])
    d1.download_button(
        "Download QA Report (.md)",
        data=str(out["report_md"]).encode("utf-8"),
        file_name="qa_inspection_report.md",
        mime="text/markdown",
    )
    d2.download_button(
        "Download Results (.csv)",
        data=out["results_csv"],
        file_name="screening_results.csv",
        mime="text/csv",
    )

    st.divider()
    st.markdown(str(out["report_md"]))


if __name__ == "__main__":
    main()

