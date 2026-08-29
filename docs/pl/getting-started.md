# Pierwsze kroki

Kamery w **Tuya Smart**, **Smart Life** lub **iSmartLife**.

## Pierwsze uruchomienie
1. Windows: Setup z [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. Uruchom **Tuya RTSP Bridge** lub `http://<host>:8787`.
3. Ten sam region co w telefonie.
4. Create QR → skan → **potwierdź**. QR **320×320**.
5. Skopiuj URL HD do NVR.

Sesje: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## Przeprowadzka / nowe Wi‑Fi
Nie usuwaj kamer z konta. Nowe SSID w app, bridge w nowym LAN, nowe IP PC w NVR.

## PTZ
Strzałki UI. LAN **TCP 6668**. Zdalnie cloud po `POST /api/cloud/auth`.

## Podgląd / Autostart
Windows = VLC. Linux = ffmpeg MJPEG. `launch-hidden.vbs` / systemd user.
