# Mulai

Kamera di **Tuya Smart**, **Smart Life**, atau **iSmartLife**.

## Jalankan pertama
1. Windows: Setup dari Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Jalankan **Tuya RTSP Bridge** (atau `http://<host>:8787`).
3. Region sama seperti ponsel.
4. Create QR → pindai → **konfirmasi**. QR **320×320**.
5. Salin URL HD ke NVR.

## PTZ
Panah di UI. **LAN:** TCP **6668**. **Off-site:** cloud setelah email+password sekali (`POST /api/cloud/auth`) — tanpa kunci IoT.

## Pratinjau
Windows Setup = VLC. Linux = ffmpeg MJPEG. RTSP tidak membutuhkannya.
