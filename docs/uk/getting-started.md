# Початок роботи

Камери в **Tuya Smart**, **Smart Life** або **iSmartLife**.

## Перший запуск
1. Windows: Setup з Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Запустіть **Tuya RTSP Bridge** (або `http://<host>:8787`).
3. Той самий регіон, що в телефоні.
4. Create QR → сканувати → **підтвердити**. QR **320×320**.
5. Скопіюйте HD URL у NVR.

## PTZ
Стрілки в UI. **LAN:** TCP **6668**. **Віддалено:** cloud після email+пароль один раз (`POST /api/cloud/auth`) — без IoT keys.

## Попередній перегляд
Windows Setup = VLC. Linux = ffmpeg MJPEG. RTSP його не потребує.
