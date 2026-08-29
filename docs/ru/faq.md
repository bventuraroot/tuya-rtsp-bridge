# Частые вопросы

### Список камер пуст после входа
Неверный регион. «Западная Европа» в DE-приложении = **EU** (`protect-eu`), не WE.

### QR не завершается
Окно открыто и **подтвердите** в телефоне.

### QR крошечный / щель (Windows)
Исправлено в **1.2.4+**: холст **320×320** (NEAREST). Обновите Setup. «No QR» до Create QR — нормально.

### Соединение отклонено (WinError 10061)
UI сам запускает API (`:8787`). Повторите Create QR.

### VLC чёрный
Поток жив. Agent/Frigate. Linux: ffmpeg MJPEG.

### Хотел 60 fps
Часто ~**10 fps** HD HEVC — это камера.

### Это ONVIF?
Нет. Только RTSP.

### Уходит ли видео из дома?
Сигнализация к Tuya. Локально: камера → этот ПК. Телефон в LTE = второй cloud-viewer.

### go2rtc `tuya://`?
Email/пароль Tuya Smart, не QR Smart Life.

### Cloud PTZ вне LAN?
Сначала LAN TCP **6668**. Удалённо: `POST /api/cloud/auth` → `cloud_auth.json` mode 600. Без IoT developer keys.

### Где логин?
`%APPDATA%\TuyaRtspBridge\` или `~/.local/share/tuya-rtsp-bridge/`. Не в git и не в скриншоты.

### Аддон Home Assistant?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. [docker.md](docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md).
