# Primeiros passos

Cámaras en **Tuya Smart**, **Smart Life** o **iSmartLife**.

## Primeira execução
1. Windows: Setup de [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. Inicie **Tuya RTSP Bridge** o `http://<host>:8787`.
3. Mesma região do telemóvel.
4. Create QR → escanear → **confirmar**. QR **320×320**.
5. Copie o URL HD para o NVR.

Sesiones en `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## Mudança / nuevo Wi‑Fi
No borres cámaras de la cuenta. Nuevo SSID en la app, bridge en el nuevo LAN, nueva IP en el NVR.

## PTZ
Flechas UI. LAN **TCP 6668**. Remoto: cloud tras `POST /api/cloud/auth`.

## Pré-visualização
Windows = VLC. Linux = ffmpeg MJPEG. Opcional.

## Arranque automático
Windows: `launch-hidden.vbs`. Linux: `systemctl --user enable --now tuya-rtsp-bridge.service tuya-rtsp-gui.service`.
