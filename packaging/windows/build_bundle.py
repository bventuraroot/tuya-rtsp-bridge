"""Build a foolproof Windows runtime (Python + wheels + VLC + ffmpeg + engine).

Run from anywhere:

    python packaging/windows/build_bundle.py

Then compile the Inno script (this file can call ISCC at the end).
Downloads land in packaging/windows/cache/ and are reused.
Staging is packaging/windows/staging/ — not committed.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"
STAGING = HERE / "staging"
RUNTIME = STAGING / "runtime"
VLC_DIR = STAGING / "vlc"
BIN = STAGING / "bin"

PYTHON_VER = "3.12.10"
PYTHON_URL = f"https://www.python.org/ftp/python/{PYTHON_VER}/python-{PYTHON_VER}-amd64.exe"
VLC_URL = "https://download.videolan.org/pub/videolan/vlc/3.0.21/win64/vlc-3.0.21-win64.zip"
FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
ISCC = Path(r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe")

UA = "tuya-rtsp-bridge-bundle/1.2 (+https://github.com/DanEng1982/tuya-rtsp-bridge)"


def log(msg: str) -> None:
    print(msg, flush=True)


def download(url: str, dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 1_000_000:
        log(f"cache hit {dest.name} ({dest.stat().st_size // 1024} KB)")
        return dest
    log(f"download {url}")
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=180) as r, dest.open("wb") as f:
        shutil.copyfileobj(r, f)
    log(f"  -> {dest} ({dest.stat().st_size // 1024} KB)")
    return dest


def unzip(archive: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        z.extractall(dest)


def install_python() -> Path:
    installer = download(PYTHON_URL, CACHE / f"python-{PYTHON_VER}-amd64.exe")
    if (RUNTIME / "python.exe").exists() and (RUNTIME / "Lib" / "tkinter").exists() or (
        RUNTIME / "tcl"
    ).exists():
        # already installed
        if (RUNTIME / "python.exe").exists():
            log("python already in staging")
            return RUNTIME / "python.exe"
    if RUNTIME.exists():
        shutil.rmtree(RUNTIME, ignore_errors=True)
    RUNTIME.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(installer),
        "/quiet",
        "InstallAllUsers=0",
        f"TargetDir={RUNTIME}",
        "PrependPath=0",
        "Shortcuts=0",
        "AssociateFiles=0",
        "Include_doc=0",
        "Include_dev=0",
        "Include_launcher=0",
        "Include_test=0",
        "Include_pip=1",
        "Include_tcltk=1",
        "CompileAll=0",
        "SimpleInstall=1",
    ]
    log("silent-install Python into staging/runtime …")
    subprocess.run(cmd, check=True, timeout=400)
    py = RUNTIME / "python.exe"
    if not py.exists():
        raise SystemExit(f"Python installer finished but {py} is missing")
    return py


def pip_install(py: Path) -> None:
    log("pip install requirements into bundled runtime …")
    subprocess.run([str(py), "-m", "pip", "install", "--upgrade", "pip"], check=True, timeout=180)
    subprocess.run(
        [str(py), "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")],
        check=True,
        timeout=300,
    )


def stage_vlc() -> None:
    z = download(VLC_URL, CACHE / "vlc-3.0.21-win64.zip")
    extract = CACHE / "vlc-extract"
    if extract.exists():
        shutil.rmtree(extract, ignore_errors=True)
    unzip(z, extract)
    inner = None
    for p in extract.iterdir():
        if p.is_dir() and (p / "libvlc.dll").exists():
            inner = p
            break
    if inner is None:
        # maybe files are at root
        if (extract / "libvlc.dll").exists():
            inner = extract
    if inner is None:
        raise SystemExit("VLC zip has no libvlc.dll")
    if VLC_DIR.exists():
        shutil.rmtree(VLC_DIR)
    shutil.copytree(inner, VLC_DIR)
    log(f"vlc staged ({VLC_DIR})")


def stage_ffmpeg() -> None:
    z = download(FFMPEG_URL, CACHE / "ffmpeg-release-essentials.zip")
    extract = CACHE / "ffmpeg-extract"
    if extract.exists():
        shutil.rmtree(extract, ignore_errors=True)
    unzip(z, extract)
    exe = next(extract.rglob("ffmpeg.exe"), None)
    license_f = next(extract.rglob("LICENSE"), None)
    if exe is None:
        raise SystemExit("ffmpeg zip has no ffmpeg.exe")
    BIN.mkdir(parents=True, exist_ok=True)
    shutil.copy2(exe, BIN / "ffmpeg.exe")
    if license_f:
        shutil.copy2(license_f, BIN / "FFMPEG-LICENSE.txt")
    log("ffmpeg staged")


def stage_engine() -> None:
    src = ROOT / "bin" / "tuya-ipc-terminal.exe"
    if not src.exists():
        go = shutil.which("go")
        if not go:
            raise SystemExit("bin/tuya-ipc-terminal.exe missing and go is not on PATH")
        vendor = ROOT / "vendor" / "tuya-ipc-terminal"
        log("go build engine …")
        subprocess.run(
            [go, "build", "-o", str(src), "."],
            cwd=vendor,
            check=True,
            timeout=300,
        )
    BIN.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, BIN / "tuya-ipc-terminal.exe")
    log("engine staged")


def verify(py: Path) -> None:
    env = os.environ.copy()
    env["PATH"] = str(VLC_DIR) + os.pathsep + str(BIN) + os.pathsep + env.get("PATH", "")
    env["VLC_PLUGIN_PATH"] = str(VLC_DIR / "plugins")
    code = (
        "import tkinter, requests, qrcode, PIL, tinytuya, vlc; "
        "print('imports-ok', tkinter.TkVersion)"
    )
    subprocess.run([str(py), "-c", code], check=True, env=env, timeout=60)
    if not (BIN / "ffmpeg.exe").exists():
        raise SystemExit("ffmpeg missing after stage")
    if not (VLC_DIR / "libvlc.dll").exists():
        raise SystemExit("libvlc missing after stage")
    log("verify ok")


def compile_inno() -> Path:
    if not ISCC.exists():
        raise SystemExit(f"Inno Setup not found: {ISCC}")
    iss = ROOT / "installer" / "TuyaRtspBridge.iss"
    log("ISCC …")
    subprocess.run([str(ISCC), str(iss)], check=True, timeout=300)
    out = ROOT / "installer" / "output" / "TuyaRtspBridge-Setup.exe"
    if not out.exists():
        raise SystemExit("ISCC reported success but Setup.exe is missing")
    log(f"SETUP {out} ({out.stat().st_size // 1024 // 1024} MB)")
    return out


def main() -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    STAGING.mkdir(parents=True, exist_ok=True)
    py = install_python()
    pip_install(py)
    stage_vlc()
    stage_ffmpeg()
    stage_engine()
    verify(py)
    compile_inno()
    return 0


if __name__ == "__main__":
    sys.exit(main())
