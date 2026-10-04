# PS170 Screening Workbench

A single local website that connects the two supplied SIH Problem Statement 170 repositories.

## What is connected

### Module A — Dynamic Outlier Detection
Uses the supplied Module A pipeline:
- robust lot-relative preprocessing / DPAT
- Isolation Forest
- static-limit screening
- SHAP / attribution-based explanation
- root-cause and risk classification

### Module B — Time-Series Drift Predictor
Uses the supplied Module B package:
- early 0h / 24h feature engineering
- model comparison
- 168h drift prediction
- conformal prediction interval
- SAFE / REVIEW / REJECT safety logic
- explanation of contributing early features

## Website flow

```text
CSV
 │
 ▼
Module A
0h + 24h dynamic screening
 │
 ├───────────────┐
 │               │
 ▼               ▼
A finding     A clear
 │               │
 └───────┬───────┘
         ▼
Module B
168h forecast for the same component
         │
         ▼
Inspection workbench
```

The frontend is intentionally plain and engineering-oriented rather than using a generic AI-dashboard style.

## Run locally

Python 3.10+ is recommended.

```bash
cd SIH170_Integrated_Website
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn backend.server:app --host 127.0.0.1 --port 8000
```

Then open:

```text
http://127.0.0.1:8000
```

The first server start trains Module B on its repository's synthetic development generator. This takes some time because the original repository compares several regression models.

## Test data

The supplied Module A `burn_in_lot_data.csv` has been copied to:

```text
backend/sample_data.csv
```

The website's **Download sample CSV** link downloads it.

Its required Module A columns are:

```text
serial_number
lot_id
Iddq_0h
leakage_0h
delay_0h
Iddq_24h
leakage_24h
delay_24h
```

Optional labels such as `is_latent_defect` can be present and allow Module A to calculate validation metrics.

## Important model-data note

The supplied Module B repository does not contain a trained production model artifact. Its README explicitly describes its current dataset as synthetic development data. Therefore this integration trains Module B once at startup using that generator.

For an SIH demonstration, this lets the complete workflow run end-to-end. For a real engineering deployment, replace that startup training data with validated measured burn-in data and replace the provisional safety thresholds with approved limits.

## Quantile Forest dependency

The original Module B package imports `quantile-forest`. The environment used to assemble this project did not have that package and could not download it, so `backend/ess_predictor/models/zoo.py` includes a compatibility fallback based on scikit-learn Random Forest tree predictions.

If `quantile-forest` is installed, the original QRF implementation is used automatically.

## Main files

```text
backend/
  server.py                  # integration API
  sample_data.csv
  module_a/                  # supplied Module A source
  ess_predictor/             # supplied Module B source + small QRF compatibility patch
  static/
    index.html
    styles.css
    app.js

requirements.txt
README.md
```
