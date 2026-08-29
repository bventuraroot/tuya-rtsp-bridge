# Per iniziare

Telecamere in **Tuya Smart**, **Smart Life** o **iSmartLife**.

## Prima esecuzione
1. Windows: Setup da Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Avvia **Tuya RTSP Bridge** (o `http://<host>:8787`).
3. Stessa regione del telefono.
4. Create QR → scansiona → **conferma**. QR fisso **320×320**.
5. Copia l’URL HD nell’NVR.

## PTZ
Frecce nella UI. **LAN:** TCP **6668**. **Fuori rete:** cloud dopo email+password una volta (`POST /api/cloud/auth`) — senza chiavi IoT.

## Anteprima
Windows Setup = VLC. Linux = ffmpeg MJPEG. L’RTSP non la richiede.
