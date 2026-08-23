# С чего начать

Работает с камерами, которые видны в **Tuya Smart**, **Smart Life** или **iSmartLife**.

1. Windows: `TuyaRtspBridge-Setup.exe` из Releases (Python/VLC/ffmpeg внутри). Linux: `./launch.sh`.
2. Запустите **Tuya RTSP Bridge**.
3. Выберите тот же регион, что в телефоне.
4. Создать QR → сканировать → **подтвердить**.
5. Скопируйте HD-адрес в NVR.

Сессии: `%APPDATA%\TuyaRtspBridge` или `~/.local/share/tuya-rtsp-bridge/`.

Новый Wi‑Fi: **не** удаляйте камеры из аккаунта. На новом месте смените сеть в приложении, запустите мост, в NVR смените только IP компьютера.

PTZ: удерживать стрелку = движение, отпустить = стоп. Локальный протокол TCP **6668**.
