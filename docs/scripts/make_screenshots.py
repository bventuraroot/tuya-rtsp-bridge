"""Sanitized GUI screenshots. Window-only capture, no live API, no video."""
from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
os.environ["TUYA_BRIDGE_ROOT"] = str(ROOT)
os.environ["APPDATA"] = str(ROOT / "docs" / "images" / ".shot-appdata")

import gui  # noqa: E402

OUT = ROOT / "docs" / "images"
OUT.mkdir(parents=True, exist_ok=True)

REGIONS = {
    "eu": {"label": "Western Europe (EU)", "host": "protect-eu.ismartlife.me"},
    "us": {"label": "USA West", "host": "protect-us.ismartlife.me"},
}

EMPTY = {
    "phase": "idle",
    "message": "Create a QR code, then scan it with Smart Life.",
    "loggedIn": False,
    "hasQr": False,
    "qrId": "",
    "cameras": [],
    "rtsp": {"running": False, "port": 8554},
    "watchdogRunning": False,
    "hlsRunning": False,
    "lanIp": "127.0.0.1",
    "uiPort": 8787,
    "region": "eu",
    "regions": REGIONS,
    "flags": {"rtsp": True, "watchdog": True, "hls": False, "archive": False},
    "user": None,
}

DEMO_CAMS = {
    **EMPTY,
    "phase": "logged_in",
    "message": "Session loaded.",
    "loggedIn": True,
    "watchdogRunning": True,
    "cameras": [
        {
            "deviceId": "demo-front",
            "deviceName": "Front yard",
            "frigateId": "front_yard",
            "rtspHd": "rtsp://127.0.0.1:8554/Front_yard/hd",
        },
        {
            "deviceId": "demo-drive",
            "deviceName": "Driveway",
            "frigateId": "driveway",
            "rtspHd": "rtsp://127.0.0.1:8554/Driveway/hd",
        },
    ],
}


def _grab(win, name: str) -> Path:
    import ctypes
    from ctypes import wintypes

    from PIL import Image

    win.update()
    win.update_idletasks()
    hwnd = int(str(win.wm_frame()), 16)
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32
    rect = wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    w, h = rect.right - rect.left, rect.bottom - rect.top
    hwnd_dc = user32.GetWindowDC(hwnd)
    mem_dc = gdi32.CreateCompatibleDC(hwnd_dc)
    hbmp = gdi32.CreateCompatibleBitmap(hwnd_dc, w, h)
    gdi32.SelectObject(mem_dc, hbmp)
    # 2 = PW_RENDERFULLCONTENT
    ok = user32.PrintWindow(hwnd, mem_dc, 2)
    # BITMAP bits via GetDIBits
    class BITMAPINFOHEADER(ctypes.Structure):
        _fields_ = [
            ("biSize", wintypes.DWORD),
            ("biWidth", ctypes.c_long),
            ("biHeight", ctypes.c_long),
            ("biPlanes", wintypes.WORD),
            ("biBitCount", wintypes.WORD),
            ("biCompression", wintypes.DWORD),
            ("biSizeImage", wintypes.DWORD),
            ("biXPelsPerMeter", ctypes.c_long),
            ("biYPelsPerMeter", ctypes.c_long),
            ("biClrUsed", wintypes.DWORD),
            ("biClrImportant", wintypes.DWORD),
        ]

    class BITMAPINFO(ctypes.Structure):
        _fields_ = [("bmiHeader", BITMAPINFOHEADER), ("bmiColors", wintypes.DWORD * 3)]

    bmi = BITMAPINFO()
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biWidth = w
    bmi.bmiHeader.biHeight = -h
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 32
    buf = ctypes.create_string_buffer(w * h * 4)
    gdi32.GetDIBits(mem_dc, hbmp, 0, h, buf, ctypes.byref(bmi), 0)
    img = Image.frombuffer("RGB", (w, h), buf, "raw", "BGRX", 0, 1)
    gdi32.DeleteObject(hbmp)
    gdi32.DeleteDC(mem_dc)
    user32.ReleaseDC(hwnd, hwnd_dc)
    if img.width > 1600:
        img = img.resize((1600, int(img.height * 1600 / img.width)))
    dest = OUT / name
    img.save(dest, "PNG", optimize=True)
    print("wrote", dest, img.size, "printwindow", ok, "hwnd", hwnd)
    return dest


def main() -> None:
    gui.ensure_backend = lambda: None
    gui.api = lambda path, body=None: EMPTY
    from i18n import save_lang

    save_lang("en")
    gui.BridgeGui.refresh = lambda self: None
    app = gui.BridgeGui()
    app.geometry("1280x800+80+40")
    app.minsize(1100, 700)
    app._paint(EMPTY)

    def shot2() -> None:
        _grab(app, "ui-ready.png")
        app.destroy()

    def shot1() -> None:
        _grab(app, "ui-welcome.png")
        app._paint(DEMO_CAMS)
        app.after(400, shot2)

    app.after(500, shot1)
    app.mainloop()


if __name__ == "__main__":
    main()
