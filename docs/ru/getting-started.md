# Начало работы

Камеры в **Tuya Smart**, **Smart Life** или **iSmartLife**.

## Первый запуск
1. Windows: Setup из [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. Запустите **Tuya RTSP Bridge** или `http://<host>:8787`.
3. Тот же регион, что в телефоне.
4. Create QR → сканировать → **подтвердить**. QR **320×320**.
5. Скопируйте HD URL в NVR.

Сессии: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`. Авто-relogin возможен с сохранённым email/паролем.

## Переезд / новый Wi‑Fi
Не удаляйте камеры из аккаунта. Новый SSID в приложении, bridge в новой LAN, новый IP ПК в NVR, путь `/CameraName/hd` тот же.

## PTZ
Стрелки в UI. LAN **TCP 6668**. Удалённо cloud после `POST /api/cloud/auth`.

## Превью / автозапуск
Windows Setup = VLC. Linux = ffmpeg MJPEG. `launch-hidden.vbs` / `systemctl --user enable --now tuya-rtsp-bridge.service tuya-rtsp-gui.service`.
