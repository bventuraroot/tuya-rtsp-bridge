@echo off
setlocal
cd /d "%~dp0"
title Tuya RTSP Bridge
echo.
echo  Tuya RTSP Bridge
echo  ----------------
if not exist ".venv\Scripts\python.exe" (
  echo  Creating a local Python environment...
  py -3 -m venv .venv 2>nul
  if not exist ".venv\Scripts\python.exe" python -m venv .venv
  if not exist ".venv\Scripts\python.exe" (
    echo.
    echo  Python 3.10+ is missing.
    echo  Install from https://www.python.org/downloads/
    echo  Tick  "Add python.exe to PATH"  then run this again.
    echo.
    echo  Python 3.10+ fehlt.
    echo  Installation: https://www.python.org/downloads/
    echo  Haken bei  "Add python.exe to PATH"  setzen.
    echo.
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
