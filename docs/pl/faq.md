# FAQ

### Pusta lista kamer po logowaniu
Zły region. «Europa Zachodnia» w aplikacji DE = **EU**, nie WE.

### QR się nie kończy
Zostaw okno otwarte i **potwierdź** w telefonie.

### QR maleńki / szczelina / nie da się zeskanować (Windows)
Naprawione w **1.2.4+**: stałe płótno **320×320** (NEAREST). Zaktualizuj aplikację. «No QR» przed Create QR jest normalne.

### Połączenie odrzucone (WinError 10061)
UI samo uruchamia API (`:8787`). Ponów Create QR.

### VLC czarne
VLC 3 często pada na HEVC/RTSP. Strumień żyje. Agent/Frigate. Linux: pipe MJPEG ffmpeg.

### Chciałem 60 fps
Wiele modeli daje ~**10 fps** w HD.

### Czy to ONVIF?
Nie. Tylko RTSP.

### Czy wideo wychodzi z domu?
Sygnalizacja do Tuya. Lokalnie zwykle kamera → ten PC.

### Cloud PTZ poza LAN?
Najpierw LAN PTZ (TCP **6668**). Zdalnie: cloud po jednorazowym email+hasło (`POST /api/cloud/auth`) — bez kluczy IoT developer.

### Add-on Home Assistant?
Tak — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Dane: `~/.local/share/tuya-rtsp-bridge/`.
