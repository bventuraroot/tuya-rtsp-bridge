# शुरू करें

**Tuya Smart** / **Smart Life** / **iSmartLife**।

## पहली बार
1. Windows Setup: [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases)। Linux: `./launch.sh`। Docker/HA: [docker.md](docker.md)।
2. **Tuya RTSP Bridge** या `http://<host>:8787`।
3. फोन जैसा रीजन।
4. Create QR → स्कैन → **confirm**। QR **320×320**।
5. HD URL NVR में।

सत्र: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`।

## नया Wi‑Fi
कैमरे अकाउंट से न हटाएँ। ऐप में नया SSID, नए LAN पर bridge, NVR में नई PC IP।

## PTZ / Preview / Autostart
LAN **TCP 6668**; cloud: `POST /api/cloud/auth`। Windows VLC; Linux ffmpeg MJPEG।
