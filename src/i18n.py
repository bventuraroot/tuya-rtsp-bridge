"""UI strings. Persisted in user config."""
from __future__ import annotations

import json
from typing import Any

from paths import config_path

LANGS = ("en", "de", "fr", "zh", "hi")

LANG_LABELS = {
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
    "zh": "简体中文",
    "hi": "हिन्दी",
}

_STRINGS: dict[str, dict[str, str]] = {
    "en": {
        "app_title": "Tuya Bridge",
        "app_banner": "■  TUYA BRIDGE",
        "lang_heading": "LANGUAGE",
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
        "yaml_empty": "# no cameras yet\n",
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
        "chip_api_off": "API OFF",
        "phase_idle": "READY",
        "phase_wait": "WAITING SCAN",
        "phase_in": "SIGNED IN",
        "phase_err": "ERROR",
        "empty_cams": "HD links appear after you scan.",
        "no_stream": "no stream",
        "fs_hint": "click = fullscreen",
        "lang": "Language",
        "msg_qr": "Create a QR code, then scan it with Smart Life.",
        "msg_session": "Session loaded.",
        "copied": "copied",
        "engine_restart": "Restarting engine …",
        "ui_restart": "Restarting UI …",
        "all_restart": "Restarting everything …",
        "lang_saved": "Language saved — restart the app.",
        "qr_error": "QR error",
        "vlc_missing": "VLC not found. Install VideoLAN VLC (free, LGPL).",
        "camera": "Camera",
    },
    "de": {
        "app_title": "Tuya-Brücke",
        "app_banner": "■  TUYA-BRÜCKE",
        "lang_heading": "SPRACHE",
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
        "yaml_empty": "# noch keine Kameras\n",
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
        "chip_api_off": "API AUS",
        "phase_idle": "BEREIT",
        "phase_wait": "WARTE SCAN",
        "phase_in": "ANGEMELDET",
        "phase_err": "FEHLER",
        "empty_cams": "Nach dem Scan erscheinen die HD-Links.",
        "no_stream": "kein Stream",
        "fs_hint": "klick = Vollbild",
        "lang": "Sprache",
        "msg_qr": "QR erzeugen, dann mit Smart Life scannen.",
        "msg_session": "Sitzung geladen.",
        "copied": "kopiert",
        "engine_restart": "Engine startet neu …",
        "ui_restart": "API startet neu …",
        "all_restart": "Alles neu …",
        "lang_saved": "Sprache gespeichert — App neu starten.",
        "qr_error": "QR-Fehler",
        "vlc_missing": "VLC nicht gefunden. Bitte VideoLAN VLC installieren (kostenlos, LGPL).",
        "camera": "Kamera",
    },
    "fr": {
        "app_title": "Pont Tuya",
        "app_banner": "■  PONT TUYA",
        "lang_heading": "LANGUE",
        "server": "Serveur",
        "qr_none": "Pas de QR",
        "qr_session": "Session active",
        "hint": "Smart Life : scanner, puis confirmer.",
        "btn_qr": "Créer le QR",
        "btn_logout": "Déconnexion",
        "cameras": "CAMÉRAS  ·  HD UNIQUEMENT",
        "cameras_refresh": "Actualiser",
        "copy_hd": "Copier HD",
        "fullscreen": "Plein écran",
        "back": "Retour  (Échap)",
        "yaml_copy": "Copier le YAML",
        "yaml_empty": "# pas encore de caméras\n",
        "switches": "INTERRUPTEURS",
        "rtsp_engine": "Moteur RTSP",
        "rtsp_engine_d": ":8554 pour Agent / Frigate",
        "watchdog": "Chien de garde",
        "watchdog_d": "relance les flux morts",
        "hls": "HLS / VLC",
        "hls_d": "transcodage x264 coûteux",
        "archive": "Archive du pont",
        "archive_d": "sinon Agent / Frigate",
        "restart": "REDÉMARRER",
        "rst_engine": "Redémarrer le moteur  (:8554)",
        "rst_ui": "Redémarrer l’interface / API",
        "rst_all": "Tout redémarrer",
        "chip_rtsp_off": "RTSP OFF",
        "chip_wd_on": "GARDE ON",
        "chip_wd_off": "GARDE OFF",
        "chip_hls_on": "HLS ON",
        "chip_hls_off": "HLS OFF",
        "chip_api_off": "API OFF",
        "phase_idle": "PRÊT",
        "phase_wait": "ATTENTE SCAN",
        "phase_in": "CONNECTÉ",
        "phase_err": "ERREUR",
        "empty_cams": "Les liens HD apparaissent après le scan.",
        "no_stream": "pas de flux",
        "fs_hint": "clic = plein écran",
        "lang": "Langue",
        "msg_qr": "Créez un QR, puis scannez-le avec Smart Life.",
        "msg_session": "Session chargée.",
        "copied": "copié",
        "engine_restart": "Redémarrage du moteur…",
        "ui_restart": "Redémarrage de l’interface…",
        "all_restart": "Redémarrage complet…",
        "lang_saved": "Langue enregistrée — redémarrez l’application.",
        "qr_error": "Erreur QR",
        "vlc_missing": "VLC introuvable. Installez VideoLAN VLC (gratuit, LGPL).",
        "camera": "Caméra",
    },
    "zh": {
        "app_title": "涂鸦网桥",
        "app_banner": "■  涂鸦网桥",
        "lang_heading": "语言",
        "server": "服务器",
        "qr_none": "尚无二维码",
        "qr_session": "会话有效",
        "hint": "用 Smart Life 扫码并确认。",
        "btn_qr": "生成二维码",
        "btn_logout": "退出登录",
        "cameras": "摄像机  ·  仅高清",
        "cameras_refresh": "刷新摄像机",
        "copy_hd": "复制高清地址",
        "fullscreen": "全屏",
        "back": "返回  (Esc)",
        "yaml_copy": "复制 YAML",
        "yaml_empty": "# 还没有摄像机\n",
        "switches": "开关",
        "rtsp_engine": "RTSP 引擎",
        "rtsp_engine_d": ":8554 供 Agent / Frigate",
        "watchdog": "看门狗",
        "watchdog_d": "死流自动重启",
        "hls": "HLS / VLC",
        "hls_d": "昂贵的 x264 转码",
        "archive": "网桥存档",
        "archive_d": "建议用 Agent / Frigate",
        "restart": "重启",
        "rst_engine": "重启引擎  (:8554)",
        "rst_ui": "重启界面 / API",
        "rst_all": "全部重启",
        "chip_rtsp_off": "RTSP 关",
        "chip_wd_on": "看门狗 开",
        "chip_wd_off": "看门狗 关",
        "chip_hls_on": "HLS 开",
        "chip_hls_off": "HLS 关",
        "chip_api_off": "API 关",
        "phase_idle": "就绪",
        "phase_wait": "等待扫码",
        "phase_in": "已登录",
        "phase_err": "错误",
        "empty_cams": "扫码确认后将显示高清链接。",
        "no_stream": "无码流",
        "fs_hint": "点击全屏",
        "lang": "语言",
        "msg_qr": "生成二维码，再用 Smart Life 扫描。",
        "msg_session": "已加载会话。",
        "copied": "已复制",
        "engine_restart": "正在重启引擎…",
        "ui_restart": "正在重启界面…",
        "all_restart": "正在全部重启…",
        "lang_saved": "语言已保存 — 请重新启动应用。",
        "qr_error": "二维码错误",
        "vlc_missing": "未找到 VLC。请安装 VideoLAN VLC（免费，LGPL）。",
        "camera": "摄像机",
    },
    "hi": {
        "app_title": "टुया ब्रिज",
        "app_banner": "■  टुया ब्रिज",
        "lang_heading": "भाषा",
        "server": "सर्वर",
        "qr_none": "कोई QR नहीं",
        "qr_session": "सत्र सक्रिय",
        "hint": "Smart Life से स्कैन करें, फिर पुष्टि करें।",
        "btn_qr": "QR बनाएँ",
        "btn_logout": "साइन आउट",
        "cameras": "कैमरे  ·  केवल HD",
        "cameras_refresh": "कैमरे ताज़ा करें",
        "copy_hd": "HD कॉपी करें",
        "fullscreen": "पूर्ण स्क्रीन",
        "back": "वापस  (Esc)",
        "yaml_copy": "YAML कॉपी करें",
        "yaml_empty": "# अभी कोई कैमरा नहीं\n",
        "switches": "स्विच",
        "rtsp_engine": "RTSP इंजन",
        "rtsp_engine_d": ":8554 Agent / Frigate के लिए",
        "watchdog": "वॉचडॉग",
        "watchdog_d": "मरे स्ट्रीम फिर चलाता है",
        "hls": "HLS / VLC",
        "hls_d": "महँगा x264 ट्रांसकोड",
        "archive": "ब्रिज संग्रह",
        "archive_d": "नहीं तो Agent / Frigate",
        "restart": "रीस्टार्ट",
        "rst_engine": "इंजन रीस्टार्ट  (:8554)",
        "rst_ui": "UI / API रीस्टार्ट",
        "rst_all": "सब रीस्टार्ट",
        "chip_rtsp_off": "RTSP बंद",
        "chip_wd_on": "वॉचडॉग चालू",
        "chip_wd_off": "वॉचडॉग बंद",
        "chip_hls_on": "HLS चालू",
        "chip_hls_off": "HLS बंद",
        "chip_api_off": "API बंद",
        "phase_idle": "तैयार",
        "phase_wait": "स्कैन की प्रतीक्षा",
        "phase_in": "साइन इन",
        "phase_err": "त्रुटि",
        "empty_cams": "स्कैन के बाद HD लिंक दिखेंगे।",
        "no_stream": "कोई स्ट्रीम नहीं",
        "fs_hint": "क्लिक = पूर्ण स्क्रीन",
        "lang": "भाषा",
        "msg_qr": "QR बनाएँ, फिर Smart Life से स्कैन करें।",
        "msg_session": "सत्र लोड हो गया।",
        "copied": "कॉपी हो गया",
        "engine_restart": "इंजन रीस्टार्ट हो रहा है…",
        "ui_restart": "UI रीस्टार्ट हो रहा है…",
        "all_restart": "सब रीस्टार्ट हो रहा है…",
        "lang_saved": "भाषा सहेजी गई — ऐप फिर से खोलें।",
        "qr_error": "QR त्रुटि",
        "vlc_missing": "VLC नहीं मिला। VideoLAN VLC लगाएँ (मुफ़्त, LGPL)।",
        "camera": "कैमरा",
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


def lang_from_label(label: str) -> str:
    for code, name in LANG_LABELS.items():
        if name == label:
            return code
    return "en"


def current_label() -> str:
    return LANG_LABELS.get(_lang, "English")


load_lang()
