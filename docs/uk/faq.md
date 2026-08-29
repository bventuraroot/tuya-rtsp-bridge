# Поширені запитання

### Список камер порожній після входу
Невірний регіон. «Західна Європа» в DE-додатку = **EU**, не WE.

### QR не завершується
Тримайте вікно відкритим і **підтвердіть** в телефоні.

### QR крихітний / щілина / не сканується (Windows)
Виправлено в **1.2.4+**: фіксоване полотно **320×320** (NEAREST). Оновіть застосунок. «No QR» до Create QR — нормально.

### З’єднання відхилено (WinError 10061)
UI сам запускає API (`:8787`). Повторіть Create QR.

### VLC чорний
VLC 3 часто падає на HEVC/RTSP. Потік живий. Agent/Frigate. Linux: pipe MJPEG ffmpeg.

### Хотів 60 fps
Багато моделей дають ~**10 fps** у HD.

### Це ONVIF?
Ні. Лише RTSP.

### Чи виходить відео з дому?
Сигналізація до Tuya. Локально зазвичай камера → цей ПК.

### Cloud PTZ поза LAN?
Спочатку LAN PTZ (TCP **6668**). Віддалено: cloud після email+пароль один раз (`POST /api/cloud/auth`) — без IoT developer keys.

### Аддон Home Assistant?
Так — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Дані: `~/.local/share/tuya-rtsp-bridge/`.
