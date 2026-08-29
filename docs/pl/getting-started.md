# Pierwsze kroki

Kamery w **Tuya Smart**, **Smart Life** lub **iSmartLife**.

## Pierwsze uruchomienie
1. Windows: Setup z Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Uruchom **Tuya RTSP Bridge** (lub `http://<host>:8787`).
3. Ten sam region co w telefonie.
4. Create QR → skan → **potwierdź**. QR **320×320**.
5. Skopiuj URL HD do NVR.

## PTZ
Strzałki w UI. **LAN:** TCP **6668**. **Zdalnie:** cloud po email+hasło raz (`POST /api/cloud/auth`) — bez kluczy IoT.

## Podgląd
Windows Setup = VLC. Linux = ffmpeg MJPEG. RTSP go nie wymaga.
