"""Live-Vorschau über VLC (HWND). Ein Start pro Kamera, kein Restart-Loop."""
from __future__ import annotations

import os
from pathlib import Path

VLC_DIR = Path(r"C:\Program Files\VideoLAN\VLC")
_instance = None


def configure_vlc_env() -> None:
    if not VLC_DIR.exists():
        return
    os.environ["PATH"] = str(VLC_DIR) + os.pathsep + os.environ.get("PATH", "")
    os.environ.setdefault("VLC_PLUGIN_PATH", str(VLC_DIR / "plugins"))


def vlc_mod():
    configure_vlc_env()
    import vlc  # type: ignore

    return vlc


def vlc_instance():
    global _instance
    vlc = vlc_mod()
    if _instance is None:
        _instance = vlc.Instance(
            "--intf",
            "dummy",
            "--no-video-title-show",
            "--quiet",
            "--network-caching=150",
            "--live-caching=150",
            "--rtsp-tcp",
            "--avcodec-hw=any",
            "--no-audio",
        )
    return _instance


class VlcPreview:
    def __init__(self) -> None:
        self.player = None
        self.url = ""
        self.hwnd = 0

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
        inst = vlc_instance()
        ply = inst.media_player_new()
        ply.set_hwnd(hwnd)
        media = inst.media_new(url)
        media.add_option(f":network-caching={cache_ms}")
        media.add_option(f":live-caching={cache_ms}")
        media.add_option(":rtsp-tcp")
        media.add_option(":no-audio")
        ply.set_media(media)
        ply.play()
        self.player = ply
        self.url = url
        self.hwnd = hwnd

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
