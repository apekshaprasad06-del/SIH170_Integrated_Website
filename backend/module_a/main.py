"""CLI entry point for Module A: Dynamic Outlier Detection System.

Pipeline: data synthesis -> DPAT preprocessing -> Isolation Forest + DPAT
union detection -> SHAP explainability -> metrics -> artifact export.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Dict, Optional

import matplotlib

matplotlib.use("Agg")
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from sklearn.model_selection import train_test_split  # noqa: E402

from data_generator import DEFAULT_OUTPUT_PATH, LABEL_COLUMN, GeneratorConfig, generate_burn_in_data  # noqa: E402
from explainability import OutlierExplainer  # noqa: E402
from model_isolation_forest import DynamicOutlierDetector  # noqa: E402
from preprocessing import FEATURE_COLUMNS, PARAMS, RAW_COLUMNS, preprocess  # noqa: E402
from qa_reporter import QAReporter  # noqa: E402

logger = logging.getLogger("module_a")


def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="SIH PS-170 Module A: dynamic outlier detection")
    parser.add_argument("--data-path", default=DEFAULT_OUTPUT_PATH, help="burn-in CSV (generated if absent)")
    parser.add_argument("--output-dir", default="output", help="directory for exported artifacts")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--regenerate", action="store_true", help="force regeneration of the synthetic data")
    parser.add_argument("--n-estimators", type=int, default=200)
    parser.add_argument("--max-samples", type=int, default=256)
    parser.add_argument("--target-recall", type=float, default=0.98)
    parser.add_argument("--dpat-sigma", type=float, default=4.5)
    parser.add_argument("--calibration-fraction", type=float, default=0.5,
                        help="fraction of labelled chips used for threshold calibration")
    parser.add_argument("--max-waterfalls", type=int, default=10, help="waterfall plots to export")
    parser.add_argument("--max-certificates", type=int, default=None, help="cap on certificates in the report")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args(argv)


def load_or_generate(path: Path, seed: int, regenerate: bool) -> pd.DataFrame:
    """Load an existing dataset or synthesise a new one."""
    if path.exists() and not regenerate:
        df = pd.read_csv(path)
        required = {"serial_number", "lot_id", *RAW_COLUMNS}
        if required.issubset(df.columns):
            logger.info("Loaded %d rows from %s", len(df), path)
            return df
        logger.warning("%s lacks required columns; regenerating.", path)
    return generate_burn_in_data(GeneratorConfig(seed=seed, output_path=str(path)), save=True)


def _native(obj: object) -> object:
    if isinstance(obj, dict):
        return {k: _native(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_native(v) for v in obj]
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    return obj


def run_pipeline(args: argparse.Namespace) -> int:
    out_dir = Path(args.output_dir)
    plot_dir = out_dir / "plots"
    plot_dir.mkdir(parents=True, exist_ok=True)

    # 1. Data ---------------------------------------------------------------
    raw = load_or_generate(Path(args.data_path), args.seed, args.regenerate)
    df = preprocess(raw, dpat_sigma=args.dpat_sigma)
    X = df[FEATURE_COLUMNS]
    has_labels = LABEL_COLUMN in df.columns
    y = df[LABEL_COLUMN].to_numpy(dtype=int) if has_labels else None

    # 2. Detection ------------------------------------------------------------
    detector = DynamicOutlierDetector(
        n_estimators=args.n_estimators,
        max_samples=args.max_samples,
        random_state=args.seed,
        target_recall=args.target_recall,
        dpat_sigma=args.dpat_sigma,
    )
    detector.fit(X)

    cal_mask = np.ones(len(df), dtype=bool)
    if has_labels and y is not None and y.sum() > 1:
        idx = np.arange(len(df))
        cal_idx, _ = train_test_split(
            idx, train_size=args.calibration_fraction, stratify=y, random_state=args.seed
        )
        cal_mask = np.zeros(len(df), dtype=bool)
        cal_mask[cal_idx] = True
        detector.calibrate_threshold(X.iloc[cal_idx], y[cal_idx], df["dpat_flag"].to_numpy()[cal_idx])
    else:
        logger.warning("No usable ground-truth labels; using a 8%% contamination threshold.")
        detector.set_threshold_by_contamination(X, 0.08)

    pred = detector.predict(X, df["dpat_flag"].to_numpy(), df["dpat_max_abs_z"].to_numpy())
    results = pd.concat([df, pred], axis=1)

    # 3. Metrics ------------------------------------------------------------------
    metrics: Dict[str, object] = {}
    if has_labels and y is not None:
        flagged = results["flagged"].to_numpy()
        metrics["Full population"] = detector.evaluate(y, flagged)
        metrics["Calibration split"] = detector.evaluate(y[cal_mask], flagged[cal_mask])
        if (~cal_mask).any():
            metrics["Held-out split"] = detector.evaluate(y[~cal_mask], flagged[~cal_mask])
        metrics["Static-limit screening (baseline)"] = detector.evaluate(y, results["static_breach"].to_numpy())
        metrics["Isolation Forest only"] = detector.evaluate(y, results["if_flag"].to_numpy())
        metrics["DPAT rule only"] = detector.evaluate(y, results["dpat_flag"].to_numpy())
        for scope, m in metrics.items():
            logger.info(
                "%-34s recall=%.3f precision=%.3f F2=%.3f FN=%d FP=%d",
                scope, m["recall"], m["precision"], m["f2"], m["fn"], m["fp"],
            )
        if metrics["Full population"]["recall"] < args.target_recall:  # type: ignore[index]
            logger.warning("Recall on the full population is below the %.2f target.", args.target_recall)

    # 4. Explainability -------------------------------------------------------------
    explainer = OutlierExplainer(detector)
    attributions = explainer.explain(X)
    contributions = explainer.parameter_contributions(attributions)
    contributions.index = results.index
    results = pd.concat([results, contributions], axis=1)

    # 5. QA classification --------------------------------------------------------------
    reporter = QAReporter()
    results = reporter.classify(results)

    flagged_rows = results[results["flagged"]].sort_values("rejection_confidence", ascending=False)
    waterfall_files: Dict[str, str] = {}
    for idx, row in flagged_rows.head(max(args.max_waterfalls, 0)).iterrows():
        serial = str(row["serial_number"])
        title = f"{serial} ({row['lot_id']}) - {row['root_cause']} - confidence {row['rejection_confidence']:.2f}"
        path = explainer.waterfall_plot(X.loc[idx], plot_dir / f"waterfall_{serial}.png", title=title)
        waterfall_files[serial] = f"plots/{path.name}"
    explainer.summary_plot(contributions, plot_dir / "parameter_contribution_summary.png",
                           mask=results["flagged"].to_numpy())

    # 6. Export --------------------------------------------------------------------------------
    results.to_csv(out_dir / "screening_results.csv", index=False)
    markdown = reporter.to_markdown(
        results, attributions, metrics=metrics or None, waterfall_files=waterfall_files,
        attribution_method=explainer.method_, max_certificates=args.max_certificates,
    )
    reporter.write_markdown(out_dir / "qa_inspection_report.md", markdown)
    with open(out_dir / "metrics.json", "w", encoding="utf-8") as fh:
        json.dump(_native({"attribution_method": explainer.method_, "threshold": detector.threshold_,
                           "metrics": metrics}), fh, indent=2)

    logger.info("Done: %d / %d chips rejected. Artifacts in %s", int(results["flagged"].sum()),
                len(results), out_dir.resolve())
    return 0


def main(argv: Optional[list] = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s")
    try:
        return run_pipeline(args)
    except Exception:
        logger.exception("Pipeline failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
