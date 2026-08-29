# Preguntas frecuentes

### Lista de cámaras vacía
Región incorrecta. «Europa occidental» en la app alemana es **EU**, no WE.

### El QR no termina
Deja la ventana abierta y **confirma** en el teléfono.

### QR minúsculo / ranura / no se escanea (Windows)
Corregido en **1.2.4+**: lienzo fijo **320×320** (NEAREST). Actualiza la app. «No QR» antes de **Create QR** es normal.

### Conexión rechazada (WinError 10061)
La UI arranca la API (`:8787`) sola. Vuelve a **Create QR** o reinicia UI/API.

### VLC en negro
VLC 3 falla a menudo con HEVC/RTSP. El stream vive. Usa Agent/Frigate. En Linux: pipe MJPEG ffmpeg.

### Esperaba 60 fps
Muchos modelos dan ~**10 fps** en HD.

### ¿Es ONVIF?
No. Solo RTSP.

### ¿Sale el vídeo de casa?
Señalización a Tuya. En local suele ser cámara → este PC.

### ¿PTZ en la nube fuera de LAN?
PTZ LAN (TCP **6668**) primero. Fuera de red: cloud con email+contraseña una vez (`POST /api/cloud/auth`) — sin claves IoT developer.

### ¿Add-on Home Assistant?
Sí — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Datos: `~/.local/share/tuya-rtsp-bridge/`.
