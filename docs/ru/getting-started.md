# Начало работы

Камеры в **Tuya Smart**, **Smart Life** или **iSmartLife**.

## Первый запуск
1. Windows: Setup из Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Запустите **Tuya RTSP Bridge** (или `http://<host>:8787`).
3. Тот же регион, что в телефоне.
4. Create QR → сканировать → **подтвердить**. QR **320×320**.
5. Скопируйте HD URL в NVR.

## PTZ
Стрелки в UI. **LAN:** TCP **6668**. **Удалённо:** cloud после email+пароль один раз (`POST /api/cloud/auth`) — без IoT keys.

## Превью
Windows Setup = VLC. Linux = ffmpeg MJPEG. RTSP не требует превью.
