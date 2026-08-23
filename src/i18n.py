"""UI strings: German + US English. Persisted in user config."""
from __future__ import annotations

import json
from typing import Any

from paths import config_path

LANGS = ("de", "en")

_STRINGS: dict[str, dict[str, str]] = {
    "de": {
        "app_title": "Tuya-Brücke",
        "app_sub": "QR-Login → Kameras → RTSP für Frigate / Agent DVR",
        "server": "Server",
        "qr_none": "Kein QR",
        "qr_session": "Sitzung aktiv",
        "hint": "Smart Life: scannen, dann bestätigen.",
        "btn_qr": "QR erzeugen",
        "btn_logout": "Abmelden",
        "cameras": "KAMERAS  ·  NUR HD",
        "cameras_refresh": "Kameras neu",
        "copy_hd": "HD kopieren",
        "fullscreen": "Vollbild",
        "back": "Zurück  (Esc)",
        "yaml_copy": "YAML kopieren",
        "switches": "SCHALTER",
        "rtsp_engine": "RTSP-Engine",
        "rtsp_engine_d": ":8554 für Agent / Frigate",
        "watchdog": "Wächter",
        "watchdog_d": "startet tote Streams neu",
        "hls": "HLS / VLC",
        "hls_d": "teurer x264-Transcode",
        "archive": "Brücken-Archiv",
        "archive_d": "sonst Agent / Frigate",
        "restart": "NEUSTART",
        "rst_engine": "Engine neu  (:8554)",
        "rst_ui": "Oberfläche / API neu",
        "rst_all": "Alles neu",
        "chip_rtsp_off": "RTSP AUS",
        "chip_wd_on": "WÄCHTER AN",
        "chip_wd_off": "WÄCHTER AUS",
        "chip_hls_on": "HLS AN",
        "chip_hls_off": "HLS AUS",
        "phase_idle": "BEREIT",
        "phase_wait": "WARTE SCAN",
        "phase_in": "ANGEMELDET",
        "phase_err": "FEHLER",
        "empty_cams": "Nach dem Scan erscheinen die HD-Links.",
        "no_stream": "kein Stream",
        "fs_hint": "klick = Vollbild",
        "lang": "Sprache",
        "region_eu": "Western Europe (EU)",
        "region_we": "Western Europe (WE)",
        "region_us": "USA West",
        "region_ue": "USA East",
        "msg_qr": "QR erzeugen, dann mit Smart Life scannen.",
        "msg_session": "Sitzung geladen.",
        "copied": "kopiert",
        "engine_restart": "Engine startet neu …",
        "vlc_missing": "VLC nicht gefunden. Bitte VideoLAN VLC installieren (kostenlos, LGPL).",
    },
    "en": {
        "app_title": "Tuya Bridge",
        "app_sub": "QR login → cameras → RTSP for Frigate / Agent DVR",
        "server": "Server",
        "qr_none": "No QR",
        "qr_session": "Session active",
        "hint": "Smart Life: scan, then confirm.",
        "btn_qr": "Create QR",
        "btn_logout": "Sign out",
        "cameras": "CAMERAS  ·  HD ONLY",
        "cameras_refresh": "Refresh cameras",
        "copy_hd": "Copy HD",
        "fullscreen": "Fullscreen",
        "back": "Back  (Esc)",
        "yaml_copy": "Copy YAML",
        "switches": "SWITCHES",
        "rtsp_engine": "RTSP engine",
        "rtsp_engine_d": ":8554 for Agent / Frigate",
        "watchdog": "Watchdog",
        "watchdog_d": "restarts dead streams",
        "hls": "HLS / VLC",
        "hls_d": "expensive x264 transcode",
        "archive": "Bridge archive",
        "archive_d": "otherwise Agent / Frigate",
        "restart": "RESTART",
        "rst_engine": "Restart engine  (:8554)",
        "rst_ui": "Restart UI / API",
        "rst_all": "Restart all",
        "chip_rtsp_off": "RTSP OFF",
        "chip_wd_on": "WATCHDOG ON",
        "chip_wd_off": "WATCHDOG OFF",
        "chip_hls_on": "HLS ON",
        "chip_hls_off": "HLS OFF",
        "phase_idle": "READY",
        "phase_wait": "WAITING SCAN",
        "phase_in": "SIGNED IN",
        "phase_err": "ERROR",
        "empty_cams": "HD links appear after you scan.",
        "no_stream": "no stream",
        "fs_hint": "click = fullscreen",
        "lang": "Language",
        "region_eu": "Western Europe (EU)",
        "region_we": "Western Europe (WE)",
        "region_us": "USA West",
        "region_ue": "USA East",
        "msg_qr": "Create a QR code, then scan it with Smart Life.",
        "msg_session": "Session loaded.",
        "copied": "copied",
        "engine_restart": "Restarting engine …",
        "vlc_missing": "VLC not found. Install VideoLAN VLC (free, LGPL).",
    },
}

_lang = "en"


def load_lang() -> str:
    global _lang
    p = config_path()
    if p.exists():
        try:
            raw = json.loads(p.read_text(encoding="utf-8"))
            if raw.get("lang") in LANGS:
                _lang = raw["lang"]
                return _lang
        except (OSError, json.JSONDecodeError):
            pass
    _lang = "en"
    return _lang


def save_lang(lang: str) -> None:
    global _lang
    if lang not in LANGS:
        lang = "en"
    _lang = lang
    cfg: dict[str, Any] = {}
    p = config_path()
    if p.exists():
        try:
            cfg = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            cfg = {}
    cfg["lang"] = lang
    p.write_text(json.dumps(cfg, indent=2), encoding="utf-8")


def t(key: str) -> str:
    return _STRINGS.get(_lang, _STRINGS["en"]).get(key) or _STRINGS["en"].get(key, key)


def current_lang() -> str:
    return _lang


load_lang()
