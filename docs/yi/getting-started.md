# אָנהייב

**Tuya Smart** / **Smart Life** / **iSmartLife**.

## ערשטע מאָל
1. Windows Setup פֿון [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. סטאַרט **Tuya RTSP Bridge** אָדער `http://<host>:8787`.
3. זעלבע רעגיאָן ווי דער טעלעפֿאָן.
4. Create QR → סקען → **באַשטעטיק**. QR **320×320**.
5. קאָפּיר HD URL אין NVR.

סעסיעס: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## אַריבערציען / נײַ Wi‑Fi
ניט אויסמעקן קאַמערעס פֿונעם אַקאַונט. נײַ SSID אין אַפּ, bridge אויף נײַ LAN, נײַ PC IP אין NVR.

## PTZ / פּרעוויו / אויטאָסטאַרט
LAN **TCP 6668**; cloud: `POST /api/cloud/auth`. Windows VLC; Linux ffmpeg MJPEG.
