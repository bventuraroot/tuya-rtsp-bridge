# Primeros pasos

Cámaras en **Tuya Smart**, **Smart Life** o **iSmartLife**.

## Primera ejecución
1. Windows: Setup de Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Arranca **Tuya RTSP Bridge** (o `http://<host>:8787`).
3. Misma región que el móvil.
4. Create QR → escanear → **confirmar**. QR fijo **320×320**.
5. Copia la URL HD al NVR.

## PTZ
Flechas en la UI. **LAN:** TCP **6668**. **Fuera de red:** cloud tras email+contraseña (`POST /api/cloud/auth`) — sin claves IoT.

## Vista previa
Windows Setup = VLC. Linux = ffmpeg MJPEG. El RTSP no la necesita.
