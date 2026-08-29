# Частые вопросы

### Список камер пуст после входа
Неверный регион. «Западная Европа» в DE-приложении = **EU**, не WE.

### QR не завершается
Держите окно открытым и **подтвердите** в телефоне.

### QR крошечный / щель / не сканируется (Windows)
Исправлено в **1.2.4+**: фиксированный холст **320×320** (NEAREST). Обновите приложение. «No QR» до Create QR — нормально.

### Соединение отклонено (WinError 10061)
UI сам запускает API (`:8787`). Повторите Create QR.

### VLC чёрный
VLC 3 часто падает на HEVC/RTSP. Поток жив. Agent/Frigate. Linux: pipe MJPEG ffmpeg.

### Хотел 60 fps
Многие модели дают ~**10 fps** в HD.

### Это ONVIF?
Нет. Только RTSP.

### Уходит ли видео из дома?
Сигнализация к Tuya. Локально обычно камера → этот ПК.

### Cloud PTZ вне LAN?
Сначала LAN PTZ (TCP **6668**). Удалённо: cloud после email+пароль один раз (`POST /api/cloud/auth`) — без IoT developer keys.

### Аддон Home Assistant?
Да — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Данные: `~/.local/share/tuya-rtsp-bridge/`.
