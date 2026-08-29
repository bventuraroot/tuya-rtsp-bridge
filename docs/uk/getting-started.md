# Початок роботи

Камери в **Tuya Smart**, **Smart Life** або **iSmartLife**.

## Перший запуск
1. Windows Setup з [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. Запустіть **Tuya RTSP Bridge** або `http://<host>:8787`.
3. Той самий регіон, що в телефоні.
4. Create QR → сканувати → **підтвердити**. QR **320×320**.
5. Скопіюйте HD URL у NVR.

Сесії: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## Переїзд / новий Wi‑Fi
Не видаляйте камери з акаунта. Новий SSID у додатку, bridge у новій LAN, нова IP ПК у NVR.

## PTZ
Стрілки UI. LAN **TCP 6668**. Віддалено cloud після `POST /api/cloud/auth`.

## Перегляд / автозапуск
Windows = VLC. Linux = ffmpeg MJPEG. `launch-hidden.vbs` / systemd user.
