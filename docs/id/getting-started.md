# Mulai

Kamera di **Tuya Smart**, **Smart Life**, atau **iSmartLife**.

## Jalankan pertama
1. Windows Setup dari [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. Jalankan **Tuya RTSP Bridge** atau `http://<host>:8787`.
3. Region sama seperti ponsel.
4. Create QR → pindai → **konfirmasi**. QR **320×320**.
5. Salin URL HD ke NVR.

Sesi: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## Pindah rumah / Wi‑Fi baru
Jangan hapus kamera dari akun. SSID baru di app, bridge di LAN baru, IP PC baru di NVR.

## PTZ
Panah UI. LAN **TCP 6668**. Off-site cloud setelah `POST /api/cloud/auth`.

## Pratinjau / Autostart
Windows = VLC. Linux = ffmpeg MJPEG. `launch-hidden.vbs` / systemd user.
