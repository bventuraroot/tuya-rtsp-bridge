"""Install vs. user-data paths. No secrets."""
from __future__ import annotations

import os
import sys
from pathlib import Path

APP_NAME = "TuyaRtspBridge"


def install_root() -> Path:
    here = Path(__file__).resolve().parent
    if here.name == "src":
        return here.parent
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return here


def user_data() -> Path:
    base = Path(os.environ.get("APPDATA") or Path.home()) / APP_NAME
    base.mkdir(parents=True, exist_ok=True)
    return base


def tuya_data() -> Path:
    d = user_data() / ".tuya-data"
    d.mkdir(parents=True, exist_ok=True)
    return d


def config_path() -> Path:
    return user_data() / "config.json"


def web_dir() -> Path:
    return install_root() / "web"


def bin_dir() -> Path:
    return install_root() / "bin"


def engine_src() -> Path:
    return install_root() / "vendor" / "tuya-ipc-terminal"


def engine_exe() -> Path:
    return bin_dir() / "tuya-ipc-terminal.exe"
