# Per iniziare

Telecamere in **Tuya Smart**, **Smart Life** o **iSmartLife**.

## Prima esecuzione
1. Windows: Setup da [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. Avvia **Tuya RTSP Bridge** o `http://<host>:8787`.
3. Stessa regione del telefono.
4. Create QR → scansiona → **conferma**. QR **320×320**.
5. Copia URL HD nell’NVR.

Sessioni: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## Trasloco / nuovo Wi‑Fi
Non cancellare le camere dall’account. Nuovo SSID in app, bridge sulla nuova LAN, nuovo IP PC nell’NVR.

## PTZ
Frecce UI. LAN **TCP 6668**. Fuori rete: cloud dopo `POST /api/cloud/auth`.

## Anteprima / Autostart
Windows = VLC. Linux = ffmpeg MJPEG. `launch-hidden.vbs` / systemd user.
