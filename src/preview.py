"""Live preview via libVLC (Windows) or ffmpeg snapshots (Linux/Wayland)."""
from __future__ import annotations

import os
import subprocess
import sys
import threading
import time
from pathlib import Path

from paths import ffmpeg_exe, user_data, vlc_dir

_instance = None
_instance_failed = ""


def configure_vlc_env() -> None:
    d = vlc_dir()
    if not d:
        return
    os.environ["PATH"] = str(d) + os.pathsep + os.environ.get("PATH", "")
    plug = d / "plugins"
    if plug.is_dir():
        os.environ.setdefault("VLC_PLUGIN_PATH", str(plug))


def vlc_mod():
    configure_vlc_env()
    import vlc  # type: ignore

    return vlc


def vlc_instance():
    global _instance, _instance_failed
    if _instance is not None:
        return _instance
    if _instance_failed:
        return None
    vlc = vlc_mod()
    attempts = [
        ("--intf", "dummy", "--quiet", "--rtsp-tcp", "--no-audio", "--vout=x11"),
        ("--intf", "dummy", "--quiet", "--rtsp-tcp", "--no-audio"),
        (),
    ]
    last = ""
    for args in attempts:
        try:
            inst = vlc.Instance(*args) if args else vlc.Instance()
        except Exception as exc:
            last = str(exc)
            continue
        if inst is not None:
            _instance = inst
            return _instance
        last = "Instance() returned None"
    _instance_failed = last or "libVLC unavailable"
    return None


def _attach(player, wid: int) -> None:
    if os.name == "nt":
        player.set_hwnd(wid)
        return
    if sys.platform == "darwin":
        player.set_nsobject(wid)
        return
    player.set_xwindow(wid)


def _nowin() -> int:
    return subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0


def grab_jpeg(url: str, dest: Path, timeout_s: float = 10.0) -> bool:
    """One frame from RTSP via ffmpeg. Returns True if dest is a usable JPEG."""
    ff = ffmpeg_exe()
    if not ff or not url:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".part.jpg")
    try:
        if tmp.exists():
            tmp.unlink()
        r = subprocess.run(
            [
                str(ff),
                "-hide_banner",
                "-loglevel",
                "error",
                "-rtsp_transport",
                "tcp",
                "-timeout",
                "5000000",
                "-i",
                url,
                "-frames:v",
                "1",
                "-q:v",
                "4",
                "-update",
                "1",
                "-y",
                str(tmp),
            ],
            capture_output=True,
            timeout=timeout_s,
            creationflags=_nowin(),
        )
        if r.returncode != 0 or not tmp.exists() or tmp.stat().st_size < 800:
            if tmp.exists():
                tmp.unlink(missing_ok=True)
            return False
        tmp.replace(dest)
        return True
    except Exception:
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass
        return False


class VlcPreview:
    """libVLC window embed — works best on Windows; fragile on Wayland."""

    def __init__(self) -> None:
        self.player = None
        self.url = ""
        self.hwnd = 0
        self.last_error = ""

    @property
    def running(self) -> bool:
        return self.player is not None

    def start(self, url: str, hwnd: int, cache_ms: int = 150) -> None:
        hwnd = int(hwnd or 0)
        if not url or not hwnd:
            return
        if self.player is not None and self.url == url and self.hwnd == hwnd:
            return
        self.stop()
        try:
            inst = vlc_instance()
            if inst is None:
                self.last_error = _instance_failed or "libVLC missing"
                return
            ply = inst.media_player_new()
            if ply is None:
                self.last_error = "media_player_new failed"
                return
            _attach(ply, hwnd)
            media = inst.media_new(url)
            if media is None:
                self.last_error = "media_new failed"
                return
            media.add_option(f":network-caching={cache_ms}")
            media.add_option(f":live-caching={cache_ms}")
            media.add_option(":rtsp-tcp")
            media.add_option(":no-audio")
            ply.set_media(media)
            ply.play()
            self.player = ply
            self.url = url
            self.hwnd = hwnd
            self.last_error = ""
        except Exception as exc:
            self.last_error = f"{type(exc).__name__}: {exc}"
            self.stop()

    def stop(self) -> None:
        ply = self.player
        self.player = None
        self.url = ""
        self.hwnd = 0
        if not ply:
            return
        try:
            ply.stop()
        except Exception:
            pass


class SnapPreview:
    """Periodic ffmpeg stills drawn onto a Tk canvas — reliable on Linux/Wayland."""

    def __init__(self, canvas, txt_id: int, cam_key: str, interval_s: float = 2.5) -> None:
        self.canvas = canvas
        self.txt_id = txt_id
        self.cam_key = cam_key
        self.interval_s = interval_s
        self.url = ""
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._photo = None
        self._img_id = None
        self.last_error = ""
        self.hwnd = 0  # API compat with VlcPreview

    @property
    def running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def start(self, url: str, hwnd: int = 0, cache_ms: int = 150) -> None:  # noqa: ARG002
        if not url:
            return
        if self.running and self.url == url:
            return
        self.stop()
        self.url = url
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True, name=f"snap-{self.cam_key[:12]}")
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()
        self.url = ""
        t = self._thread
        self._thread = None
        if t and t.is_alive():
            t.join(timeout=0.2)

    def _loop(self) -> None:
        dest = user_data() / "tmp" / f"prev_{self.cam_key}.jpg"
        fails = 0
        while not self._stop.is_set():
            url = self.url
            if not url:
                break
            ok = grab_jpeg(url, dest, timeout_s=12.0)
            if ok:
                fails = 0
                self.last_error = ""
                try:
                    self.canvas.after(0, lambda p=dest: self._paint(p))
                except Exception:
                    break
            else:
                fails += 1
                if fails >= 2:
                    self.last_error = "no frame"
                    try:
                        self.canvas.after(
                            0,
                            lambda: self.canvas.itemconfig(self.txt_id, text="no frame / offline"),
                        )
                    except Exception:
                        break
            # wait interval, but wake early on stop
            self._stop.wait(self.interval_s if ok else 4.0)

    def _paint(self, path: Path) -> None:
        if self._stop.is_set():
            return
        try:
            from PIL import Image, ImageTk

            im = Image.open(path).convert("RGB")
            # fit 480x270 canvas
            im = im.resize((480, 270), Image.Resampling.BILINEAR)
            photo = ImageTk.PhotoImage(im)
            self._photo = photo  # keep ref
            if self._img_id is None:
                self._img_id = self.canvas.create_image(0, 0, anchor="nw", image=photo)
            else:
                self.canvas.itemconfig(self._img_id, image=photo)
            self.canvas.itemconfig(self.txt_id, text="")
            self.canvas.tag_raise(self.txt_id)
        except Exception as exc:
            self.last_error = str(exc)
