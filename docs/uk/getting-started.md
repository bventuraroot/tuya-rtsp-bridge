# З чого почати

Працює з камерами, які видно в **Tuya Smart**, **Smart Life** або **iSmartLife**.

1. Windows: `TuyaRtspBridge-Setup.exe` з Releases (Python/VLC/ffmpeg усередині). Linux: `./launch.sh`.
2. Запустіть **Tuya RTSP Bridge**.
3. Оберіть той самий регіон, що в телефоні.
4. Створити QR → сканувати → **підтвердити**.
5. Скопіюйте HD-адресу в NVR.

Сеанси: `%APPDATA%\TuyaRtspBridge` або `~/.local/share/tuya-rtsp-bridge/`.

Новий Wi‑Fi: **не** видаляйте камери з облікового запису. На новому місці змініть мережу в додатку, запустіть міст, у NVR змініть лише IP комп’ютера.

PTZ: утримувати стрілку = рух, відпустити = стоп. Локальний протокол TCP **6668**.
