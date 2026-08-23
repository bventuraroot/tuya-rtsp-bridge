@echo off
setlocal
cd /d "%~dp0"
title Tuya RTSP Bridge
set "PATH=%~dp0bin;%~dp0vlc;%PATH%"
if exist "%~dp0vlc\plugins" set "VLC_PLUGIN_PATH=%~dp0vlc\plugins"
set "TUYA_BRIDGE_ROOT=%~dp0"

set "PYW="
if exist "%~dp0runtime\pythonw.exe" set "PYW=%~dp0runtime\pythonw.exe"
if not defined PYW if exist "%~dp0.venv\Scripts\pythonw.exe" set "PYW=%~dp0.venv\Scripts\pythonw.exe"
if not defined PYW if exist "%~dp0runtime\python.exe" set "PYW=%~dp0runtime\python.exe"
if not defined PYW if exist "%~dp0.venv\Scripts\python.exe" set "PYW=%~dp0.venv\Scripts\python.exe"

if not defined PYW (
  echo.
  echo  Creating a local Python environment...
  py -3 -m venv .venv 2>nul
  if not exist ".venv\Scripts\python.exe" python -m venv .venv
  if not exist ".venv\Scripts\python.exe" (
    echo.
    echo  This folder has no bundled runtime and no system Python.
    echo  Use TuyaRtspBridge-Setup.exe from GitHub Releases — it includes everything.
    echo.
    echo  Oder: Python 3.10+ von https://www.python.org/downloads/  ^(Haken bei Add to PATH^)
    echo.
    pause
    exit /b 1
  )
  ".venv\Scripts\python.exe" -m pip install --upgrade pip
  ".venv\Scripts\python.exe" -m pip install -r "%~dp0requirements.txt"
  if exist ".venv\Scripts\pythonw.exe" set "PYW=%~dp0.venv\Scripts\pythonw.exe"
  if not defined PYW set "PYW=%~dp0.venv\Scripts\python.exe"
)

start "" "%PYW%" -u "%~dp0src\gui.py"
endlocal
