"""Start/stop optionaler Dienste. Keine Secrets."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from paths import install_root, tuya_data, user_data

DATA = tuya_data()
FLAGS = DATA / "ui_flags.json"
SRC = Path(__file__).resolve().parent
DEFAULTS = {
    "rtsp": True,
    "watchdog": True,
    "archive": False,
    "hls": False,
}


def _pythonw() -> Path:
    exe = Path(sys.executable)
    pw = exe.with_name("pythonw.exe")
    if pw.exists():
        return pw
    return exe


def _flags() -> int:
    return subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0


def load_flags() -> dict[str, bool]:
    out = dict(DEFAULTS)
    if FLAGS.exists():
        try:
            raw = json.loads(FLAGS.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                for k in DEFAULTS:
                    if k in raw:
                        out[k] = bool(raw[k])
        except (OSError, json.JSONDecodeError):
            pass
    return out


def save_flags(flags: dict[str, bool]) -> dict[str, bool]:
    merged = load_flags()
    for k in DEFAULTS:
        if k in flags:
            merged[k] = bool(flags[k])
    DATA.mkdir(parents=True, exist_ok=True)
    FLAGS.write_text(json.dumps(merged, indent=2), encoding="utf-8")
    return merged


def _pids_matching(needle: str) -> list[int]:
    try:
        raw = subprocess.check_output(
            [
                "powershell.exe",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_Process | "
                f"Where-Object {{ $_.CommandLine -like '*{needle}*' }} | "
                "Select-Object -ExpandProperty ProcessId",
            ],
            text=True,
            timeout=12,
            creationflags=_flags(),
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        return []
    out: list[int] = []
    for part in raw.split():
        if part.isdigit():
            pid = int(part)
            if pid > 4:
                out.append(pid)
    return out


def _kill_pids(pids: list[int]) -> None:
    for pid in pids:
        subprocess.run(
            ["taskkill.exe", "/F", "/PID", str(pid)],
            capture_output=True,
            creationflags=_flags(),
        )


def _spawn(script: str) -> None:
    exe = _pythonw()
    path = SRC / script
    if not path.exists() or not exe.exists():
        return
    subprocess.Popen(
        [str(exe), "-u", str(path)],
        cwd=str(user_data()),
        creationflags=_flags(),
    )


def watchdog_running() -> bool:
    return bool(_pids_matching("rtsp_watchdog.py"))


def archive_running() -> bool:
    return bool(_pids_matching("archive_recorder.py"))


def set_watchdog(on: bool) -> None:
    if on:
        if not watchdog_running():
            _spawn("rtsp_watchdog.py")
        return
    _kill_pids(_pids_matching("rtsp_watchdog.py"))
    lock = user_data() / "rtsp_watchdog.lock"
    if lock.exists():
        try:
            lock.unlink()
        except OSError:
            pass


def set_archive(on: bool) -> None:
    if on:
        if not archive_running():
            _spawn("archive_recorder.py")
        return
    _kill_pids(_pids_matching("archive_recorder.py"))


def status() -> dict[str, Any]:
    flags = load_flags()
    return {
        "flags": flags,
        "watchdogRunning": watchdog_running(),
        "archiveRunning": archive_running(),
    }
