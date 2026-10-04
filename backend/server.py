
from __future__ import annotations

import io
import os
import sys
import traceback
import threading
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sklearn.model_selection import train_test_split

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "module_a"))
sys.path.insert(0, str(BASE))

from data_generator import LABEL_COLUMN, GeneratorConfig, generate_burn_in_data
from explainability import OutlierExplainer
from model_isolation_forest import DynamicOutlierDetector
from preprocessing import FEATURE_COLUMNS, RAW_COLUMNS, preprocess
from qa_reporter import QAReporter

from ess_predictor.data.synthetic_data import generate_synthetic_dataset
from ess_predictor.pipeline import train_all_parameters, predict_component
from ess_predictor.safety.decision import overall_component_decision

app = FastAPI(title="SIH PS170 Integrated Screening", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "module_b_ready": MODEL_B_READY,
        "module_b_training": MODEL_B_TRAINING_IN_PROGRESS,
        "module_b_error": MODEL_B_ERROR
    }

MODEL_B_SYSTEM = None
MODEL_B_TRAINING = None
STARTUP_ERROR = None

# Module B status
MODEL_B_READY = False
MODEL_B_TRAINING_IN_PROGRESS = False
MODEL_B_ERROR = None


def train_module_b():
    global MODEL_B_SYSTEM
    global MODEL_B_TRAINING
    global STARTUP_ERROR
    global MODEL_B_READY
    global MODEL_B_TRAINING_IN_PROGRESS
    global MODEL_B_ERROR

    MODEL_B_TRAINING_IN_PROGRESS = True
    MODEL_B_READY = False
    MODEL_B_ERROR = None

    try:
        print("Module B: background training started...")

        MODEL_B_TRAINING = generate_synthetic_dataset(
            n_components=80,
            n_lots=4,
            seed=42,
            profile="balanced"
        )

        print("Module B: synthetic training data generated.")

        MODEL_B_SYSTEM = train_all_parameters(
            MODEL_B_TRAINING,
            n_folds=3,
            verbose=False
        )

        MODEL_B_READY = True
        MODEL_B_TRAINING_IN_PROGRESS = False

        print("Module B: training completed successfully.")

    except Exception as exc:
        MODEL_B_READY = False
        MODEL_B_TRAINING_IN_PROGRESS = False
        MODEL_B_ERROR = str(exc)
        STARTUP_ERROR = f"Module B startup training failed: {exc}"

        print(f"Module B training failed: {exc}")
        traceback.print_exc()


@app.on_event("startup")
def startup():
    print("FastAPI startup: starting server immediately.")

    training_thread = threading.Thread(
        target=train_module_b,
        daemon=True
    )

    training_thread.start()

    print("FastAPI startup: Module B training launched in background.")


def _native(v):
    if isinstance(v, dict):
        return {str(k): _native(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_native(x) for x in v]
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        return None if not np.isfinite(v) else float(v)
    if isinstance(v, float):
        return None if not np.isfinite(v) else v
    if pd.isna(v):
        return None
    return v


def _json_records(df: pd.DataFrame):
    records = []
    for row in df.to_dict(orient="records"):
        records.append(_native(row))
    return records


def _run_module_a(raw: pd.DataFrame):
    required = {"serial_number", "lot_id", *RAW_COLUMNS}
    missing = sorted(required - set(raw.columns))
    if missing:
        raise ValueError(
            "The uploaded CSV is missing Module A columns: " + ", ".join(missing)
        )

    df = preprocess(raw)
    X = df[FEATURE_COLUMNS]

    y = (
        df[LABEL_COLUMN].to_numpy(dtype=int)
        if LABEL_COLUMN in df.columns
        else None
    )

    detector = DynamicOutlierDetector(random_state=42)
    detector.fit(X)

    if y is not None and y.sum() > 1 and (y == 0).sum() > 1:
        idx = np.arange(len(df))
        cal_idx, _ = train_test_split(
            idx, train_size=0.5, stratify=y, random_state=42
        )
        detector.calibrate_threshold(
            X.iloc[cal_idx],
            y[cal_idx],
            df["dpat_flag"].to_numpy()[cal_idx],
        )
    else:
        detector.set_threshold_by_contamination(X, 0.08)

    pred = detector.predict(
        X,
        df["dpat_flag"].to_numpy(),
        df["dpat_max_abs_z"].to_numpy(),
    )
    results = pd.concat([df, pred], axis=1)

    explainer = OutlierExplainer(detector)
    attributions = explainer.explain(X)
    contributions = explainer.parameter_contributions(attributions)
    contributions.index = results.index
    results = pd.concat([results, contributions], axis=1)

    reporter = QAReporter()
    results = reporter.classify(results)

    metrics = {}
    if y is not None:
        metrics["full_population"] = detector.evaluate(
            y, results["flagged"].to_numpy()
        )

    return results, metrics, detector.threshold_


def _module_a_to_b(row_df: pd.DataFrame) -> pd.DataFrame:
    """Translate Module A's schema into Module B's early-readout schema."""
    out = pd.DataFrame(index=row_df.index)
    out["Component_ID"] = row_df["serial_number"].astype(str)
    out["Lot_ID"] = row_df["lot_id"].astype(str)
    out["Device_Type"] = "SIH-PS170"
    out["Temperature"] = 125.0

    mapping = {
        "Iddq": "Iddq",
        "Leakage": "leakage",
        "PropagationDelay": "delay",
    }
    for bparam, acol in mapping.items():
        out[f"{bparam}_0h"] = pd.to_numeric(row_df[f"{acol}_0h"], errors="coerce")
        out[f"{bparam}_24h"] = pd.to_numeric(row_df[f"{acol}_24h"], errors="coerce")
    return out.reset_index(drop=True)


def _run_module_b(mapped: pd.DataFrame, a_results: pd.DataFrame):
    if MODEL_B_SYSTEM is None:
        raise RuntimeError(
            STARTUP_ERROR or "Module B is still training. Try again in a few seconds."
        )

    # Use the uploaded lot data as the reference population for Module B's
    # 24h lot-z-score check. No future 96h/168h values are supplied at inference.
    reference = mapped.copy()
    rows = []
    for i in range(len(mapped)):
        component = mapped.iloc[[i]]
        try:
            per_param = predict_component(
                MODEL_B_SYSTEM,
                component,
                lot_reference_df=reference,
                include_explanations=bool(a_results.iloc[i]["flagged"]),
            )
        except Exception as exc:
            per_param = {"_error": str(exc)}

        param_rows = {}
        decisions = {}
        for pname, result in per_param.items():
            if pname == "_error":
                continue
            d = result["decision"]
            decisions[pname] = d
            param_rows[pname] = {
                "value_0h": result["value_0h"],
                "value_24h": result["value_24h"],
                "prediction": result["prediction"],
                "interval_low": result["interval"][0],
                "interval_high": result["interval"][1],
                "lot_z_24h": result["lot_z_24h"],
                "decision": d.decision,
                "reasons": d.reasons,
                "model_used": result["model_used"],
                "physically_implausible": result["physically_implausible"],
                "contributions": [
                    {
                        "feature": c.feature,
                        "value": c.value,
                        "contribution": c.contribution,
                        "method": c.method,
                    }
                    for c in (result.get("contributions") or [])
                ],
            }

        overall = overall_component_decision(decisions) if decisions else "UNAVAILABLE"
        rows.append(
            {
                "Component_ID": component.iloc[0]["Component_ID"],
                "module_b_overall": overall,
                "parameters": param_rows,
            }
        )
    return rows


def _joint_label(a_flagged: bool, b_overall: str) -> str:
    if a_flagged and b_overall == "REJECT":
        return "A anomaly + B future-risk"
    if a_flagged and b_overall == "REVIEW":
        return "A anomaly + B review"
    if a_flagged and b_overall == "SAFE":
        return "A anomaly; B below threshold"
    if (not a_flagged) and b_overall == "REJECT":
        return "B future-risk"
    if (not a_flagged) and b_overall == "REVIEW":
        return "B review"
    if (not a_flagged) and b_overall == "SAFE":
        return "No finding"
    return "Unavailable"


@app.get("/api/health")
def health():
    return {
        "ok": True,
        "module_a": True,
        "module_b_ready": MODEL_B_SYSTEM is not None,
        "module_b_error": STARTUP_ERROR,
    }


@app.get("/api/sample")
def sample():
    path = BASE / "sample_data.csv"
    return FileResponse(path, filename="sample_data.csv", media_type="text/csv")


@app.post("/api/screen")
async def screen(file: UploadFile = File(...)):

    if not MODEL_B_READY:
        if MODEL_B_TRAINING_IN_PROGRESS:
            raise HTTPException(
                status_code=503,
                detail="Module B is still training. Please try again shortly."
            )

        if MODEL_B_ERROR:
            raise HTTPException(
                status_code=500,
                detail=f"Module B training failed: {MODEL_B_ERROR}"
            )

        raise HTTPException(
            status_code=503,
            detail="Module B is not ready yet. Please try again shortly."
        )

    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a CSV file."
        )

    try:
        content = await file.read()
        raw = pd.read_csv(io.BytesIO(content))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Could not read CSV: {exc}")

    try:
        a_results, a_metrics, threshold = _run_module_a(raw)
        b_input = _module_a_to_b(a_results)
        b_results = _run_module_b(b_input, a_results)
    except Exception as exc:
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(exc))

    b_by_id = {r["Component_ID"]: r for r in b_results}

    records = []
    for _, row in a_results.iterrows():
        cid = str(row["serial_number"])
        b = b_by_id.get(cid, {"module_b_overall": "UNAVAILABLE", "parameters": {}})
        records.append(
            {
                "component_id": cid,
                "lot_id": str(row["lot_id"]),
                "module_a_flagged": bool(row["flagged"]),
                "module_a_confidence": row.get("rejection_confidence"),
                "module_a_risk": row.get("risk_level"),
                "module_a_root_cause": row.get("root_cause"),
                "module_a_driver": row.get("dpat_driver"),
                "module_a_max_abs_z": row.get("dpat_max_abs_z"),
                "module_a_static_breach": bool(row.get("static_breach", False)),
                "module_a_parameters": {
                    "Iddq": {
                        "v0": row.get("Iddq_0h"),
                        "v24": row.get("Iddq_24h"),
                        "drift_pct": row.get("drift_pct_Iddq"),
                        "z0": row.get("z_Iddq_0h"),
                        "z24": row.get("z_Iddq_24h"),
                        "zdrift": row.get("zdrift_Iddq"),
                    },
                    "Leakage": {
                        "v0": row.get("leakage_0h"),
                        "v24": row.get("leakage_24h"),
                        "drift_pct": row.get("drift_pct_leakage"),
                        "z0": row.get("z_leakage_0h"),
                        "z24": row.get("z_leakage_24h"),
                        "zdrift": row.get("zdrift_leakage"),
                    },
                    "PropagationDelay": {
                        "v0": row.get("delay_0h"),
                        "v24": row.get("delay_24h"),
                        "drift_pct": row.get("drift_pct_delay"),
                        "z0": row.get("z_delay_0h"),
                        "z24": row.get("z_delay_24h"),
                        "zdrift": row.get("zdrift_delay"),
                    },
                },
                "module_b_overall": b["module_b_overall"],
                "module_b_parameters": b["parameters"],
                "joint_status": _joint_label(
                    bool(row["flagged"]), b["module_b_overall"]
                ),
            }
        )

    a_flagged = int(a_results["flagged"].sum())
    b_counts = {}
    for r in b_results:
        key = r["module_b_overall"]
        b_counts[key] = b_counts.get(key, 0) + 1

    return _native(
        {
            "filename": file.filename,
            "rows": len(a_results),
            "lots": int(a_results["lot_id"].nunique()),
            "module_a": {
                "flagged": a_flagged,
                "clear": len(a_results) - a_flagged,
                "rejection_rate": 100 * a_flagged / max(len(a_results), 1),
                "threshold": threshold,
                "metrics": a_metrics,
            },
            "module_b": {
                "decisions": b_counts,
                "training_source": "Module B synthetic development data",
                "training_rows": len(MODEL_B_TRAINING) if MODEL_B_TRAINING is not None else 0,
            },
            "records": records,
        }
    )


# Serve the simple frontend without Node.
app.mount("/", StaticFiles(directory=str(BASE / "static"), html=True), name="static")
