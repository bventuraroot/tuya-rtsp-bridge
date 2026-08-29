# Aan de slag

Camera’s in **Tuya Smart**, **Smart Life** of **iSmartLife**.

## Eerste start
1. Windows: Setup uit Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Start **Tuya RTSP Bridge** (of `http://<host>:8787`).
3. Zelfde regio als de telefoon.
4. Create QR → scannen → **bevestigen**. QR vast **320×320**.
5. Kopieer HD-URL naar de NVR.

## PTZ
Pijlen in de UI. **LAN:** TCP **6668**. **Off-site:** cloud na eenmalig email+wachtwoord (`POST /api/cloud/auth`) — geen IoT-keys.

## Preview
Windows Setup = VLC. Linux = ffmpeg-MJPEG. RTSP heeft het niet nodig.
