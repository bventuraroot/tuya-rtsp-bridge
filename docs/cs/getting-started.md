# Začínáme

Funguje s kamerami v **Tuya Smart**, **Smart Life** nebo **iSmartLife**.

## První spuštění
1. Windows: Setup z Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Spusťte **Tuya RTSP Bridge** (nebo `http://<host>:8787`).
3. Region jako v telefonu.
4. Create QR → naskenovat → **potvrdit**. QR je **320×320**.
5. Zkopírujte HD URL do NVR.

## PTZ
Šipky v GUI. **LAN:** TCP **6668**. **Mimo síť:** cloud po email+hesle (`POST /api/cloud/auth`) — bez IoT keys.

## Náhled
Windows Setup = VLC. Linux = ffmpeg MJPEG. RTSP funguje i bez náhledu.
