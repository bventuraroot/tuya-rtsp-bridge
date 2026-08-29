# Začínáme

Kamery v **Tuya Smart**, **Smart Life** nebo **iSmartLife**.

## První spuštění
1. Windows: Setup z [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. Spusťte **Tuya RTSP Bridge** nebo `http://<host>:8787`.
3. Stejný region jako telefon.
4. Create QR → sken → **potvrdit**. QR **320×320**.
5. Zkopírujte HD URL do NVR.

Session: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## Stěhování / nová Wi‑Fi
Nemazejte kamery z účtu. Nové SSID v app, bridge v nové LAN, nová IP PC v NVR.

## PTZ
Šipky UI. LAN **TCP 6668**. Vzdáleně cloud po `POST /api/cloud/auth`.

## Náhled / Autostart
Windows = VLC. Linux = ffmpeg MJPEG. `launch-hidden.vbs` / systemd user.
