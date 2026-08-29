# FAQ

### Daftar kamera kosong
Region salah. «Western Europe» di app DE = **EU**, bukan WE.

### QR tidak selesai
Biarkan jendela terbuka dan **konfirmasi** di ponsel.

### QR kecil / celah / tak terbaca (Windows)
Diperbaiki di **1.2.4+**: kanvas tetap **320×320** (NEAREST). Update app. «No QR» sebelum Create QR normal.

### Koneksi ditolak (WinError 10061)
UI menjalankan API (`:8787`) sendiri. Coba Create QR lagi.

### VLC hitam
VLC 3 sering gagal di HEVC/RTSP. Stream hidup. Agent/Frigate. Linux: pipe MJPEG ffmpeg.

### Mengharapkan 60 fps
Banyak model ~**10 fps** di HD.

### Apakah ONVIF?
Tidak. Hanya RTSP.

### Apakah video keluar rumah?
Signaling ke Tuya. Lokal biasanya kamera → PC ini.

### Cloud PTZ di luar LAN?
LAN PTZ (TCP **6668**) dulu. Off-site: cloud setelah email+password sekali (`POST /api/cloud/auth`) — tanpa kunci IoT developer.

### Add-on Home Assistant?
Ya — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Data: `~/.local/share/tuya-rtsp-bridge/`.
