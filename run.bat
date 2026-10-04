@echo off
echo Installing/using the PS170 Screening Workbench...
if not exist ".venv\Scripts\python.exe" (
  py -m venv .venv
  call .venv\Scripts\activate
  python -m pip install -r requirements.txt
) else (
  call .venv\Scripts\activate
)
python -m uvicorn backend.server:app --host 127.0.0.1 --port 8000
