# FAQ

### Pusta lista kamer
Zły region. «Europa Zachodnia» w app DE = **EU**, nie WE.

### QR się nie kończy
Okno otwarte i **potwierdź** w telefonie.

### QR-szczelina (Windows)
Naprawione w **1.2.4+**: płótno **320×320** (NEAREST). Zaktualizuj Setup.

### WinError 10061
UI samo startuje API `:8787`. Ponów Create QR.

### VLC czarne
Strumień żyje. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps?
Często ~**10 fps** HD.

### ONVIF?
Nie. Tylko RTSP.

### Czy wideo wychodzi z domu?
Sygnalizacja do Tuya. Lokalnie: kamera → ten PC.

### go2rtc `tuya://`?
Email/hasło Tuya Smart, nie QR Smart Life.

### Cloud PTZ poza LAN?
Najpierw LAN TCP **6668**. Zdalnie: `POST /api/cloud/auth`, `cloud_auth.json` mode 600. Bez kluczy IoT developer.

### Gdzie login?
`%APPDATA%\TuyaRtspBridge\` lub `~/.local/share/tuya-rtsp-bridge/`.

### Add-on HA?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). [docker.md](docker.md).

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md).
