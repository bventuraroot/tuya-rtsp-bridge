"""Live preview via libVLC. HWND on Windows, X11 window id on Linux."""
from __future__ import annotations

import os
import sys
from paths import vlc_dir

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
    """Return a shared libVLC Instance, or None if libVLC cannot start."""
    global _instance, _instance_failed
    if _instance is not None:
        return _instance
    if _instance_failed:
        return None
    vlc = vlc_mod()
    # Prefer plain software decode; hw flags break some Linux installs.
    attempts = [
        (
            "--intf",
            "dummy",
            "--no-video-title-show",
            "--quiet",
            "--network-caching=200",
            "--live-caching=200",
            "--rtsp-tcp",
            "--no-audio",
            "--vout=x11",
        ),
        (
            "--intf",
            "dummy",
            "--quiet",
            "--rtsp-tcp",
            "--no-audio",
        ),
        [],
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


class VlcPreview:
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
