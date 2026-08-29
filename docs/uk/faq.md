# Поширені запитання

### Список камер порожній
Невірний регіон. «Західна Європа» в DE-додатку = **EU**, не WE.

### QR не завершується
Вікно відкрите і **підтвердіть** у телефоні.

### QR-щілина (Windows)
Виправлено в **1.2.4+**: полотно **320×320** (NEAREST). Оновіть Setup.

### WinError 10061
UI сам запускає API `:8787`. Повторіть Create QR.

### VLC чорний
Потік живий. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps?
Часто ~**10 fps** HD.

### ONVIF?
Ні. Лише RTSP.

### Чи виходить відео з дому?
Сигналізація до Tuya. Локально: камера → цей ПК.

### go2rtc `tuya://`?
Email/пароль Tuya Smart, не QR Smart Life.

### Cloud PTZ поза LAN?
Спочатку LAN TCP **6668**. Віддалено: `POST /api/cloud/auth`, `cloud_auth.json` mode 600.

### Де логін?
`%APPDATA%\TuyaRtspBridge\` або `~/.local/share/tuya-rtsp-bridge/`.

### Аддон HA?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). [docker.md](docker.md).

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md).
