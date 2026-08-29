# Primeros pasos

Cámaras en **Tuya Smart**, **Smart Life** o **iSmartLife**.

## Primera ejecución
1. Windows: Setup de [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. Arranca **Tuya RTSP Bridge** o `http://<host>:8787`.
3. Misma región que el móvil.
4. Create QR → escanear → **confirmar**. QR **320×320**.
5. Copia URL HD al NVR.

Sesiones en `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## Mudanza / nuevo Wi‑Fi
No borres cámaras de la cuenta. Nuevo SSID en la app, bridge en el nuevo LAN, nueva IP en el NVR.

## PTZ
Flechas UI. LAN **TCP 6668**. Remoto: cloud tras `POST /api/cloud/auth`.

## Vista previa
Windows = VLC. Linux = ffmpeg MJPEG. Opcional.

## Inicio automático
Windows: `launch-hidden.vbs`. Linux: `systemctl --user enable --now tuya-rtsp-bridge.service tuya-rtsp-gui.service`.
