# התחלה

**Tuya Smart** / **Smart Life** / **iSmartLife**.

## הרצה ראשונה
1. Windows Setup מ-[Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. הפעילו **Tuya RTSP Bridge** או `http://<host>:8787`.
3. אותו אזור כמו בטלפון.
4. Create QR → סריקה → **אישור**. QR **320×320**.
5. העתיקו URL HD ל-NVR.

סשנים: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## מעבר דירה / Wi‑Fi חדש
אל תמחקו מצלמות מהחשבון. SSID חדש באפליקציה, bridge ב-LAN חדש, IP חדש ב-NVR.

## PTZ / תצוגה / הפעלה אוטומטית
LAN **TCP 6668**; cloud: `POST /api/cloud/auth`. Windows VLC; Linux ffmpeg MJPEG.
