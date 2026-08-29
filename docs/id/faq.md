# FAQ

### Daftar kamera kosong
Region salah. «Western Europe» app DE = **EU**, bukan WE.

### QR tidak selesai
Jendela terbuka dan **konfirmasi** di ponsel.

### QR celah (Windows)
Diperbaiki di **1.2.4+**: kanvas **320×320** (NEAREST). Update Setup.

### WinError 10061
UI menjalankan API `:8787` sendiri. Coba Create QR lagi.

### VLC hitam
Stream hidup. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps?
Sering ~**10 fps** HD.

### ONVIF?
Tidak. Hanya RTSP.

### Video keluar rumah?
Signaling ke Tuya. Lokal: kamera → PC ini.

### go2rtc `tuya://`?
Email/password Tuya Smart, bukan QR Smart Life.

### Cloud PTZ di luar LAN?
LAN TCP **6668** dulu. Off-site: `POST /api/cloud/auth`, `cloud_auth.json` mode 600.

### Login di mana?
`%APPDATA%\TuyaRtspBridge\` atau `~/.local/share/tuya-rtsp-bridge/`.

### Add-on HA?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). [docker.md](docker.md).

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md).
