@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  py -3 -m venv .venv 2>nul
  if not exist ".venv\Scripts\python.exe" python -m venv .venv
  if not exist ".venv\Scripts\python.exe" (
    echo Python 3.10+ is required. Install from https://www.python.org/downloads/
    echo Python 3.10+ wird benoetigt. Installation: https://www.python.org/downloads/
    pause
    exit /b 1
  )
  ".venv\Scripts\python.exe" -m pip install --upgrade pip
  ".venv\Scripts\python.exe" -m pip install -r "%~dp0requirements.txt"
)
if exist ".venv\Scripts\pythonw.exe" (
  start "" ".venv\Scripts\pythonw.exe" -u "%~dp0src\gui.py"
) else (
  start "" ".venv\Scripts\python.exe" -u "%~dp0src\gui.py"
)
endlocal
