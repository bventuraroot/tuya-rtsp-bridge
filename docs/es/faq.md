# Preguntas frecuentes

### Lista de cámaras vacía
Región incorrecta. «Europa occidental» en la app DE = **EU** (`protect-eu`), no WE.

### El QR no termina
Ventana abierta y **confirma** en el teléfono.

### QR minúsculo / ranura (Windows)
Corregido en **1.2.4+**: lienzo fijo **320×320** (NEAREST). Actualiza Setup. «No QR» antes de Create QR es normal.

### Conexión rechazada (WinError 10061)
La UI arranca la API (`:8787`) sola. Reintenta Create QR.

### VLC negro
VLC 3 falla en HEVC/RTSP. El stream vive. Agent/Frigate. Linux: ffmpeg MJPEG.

### ¿60 fps?
A menudo ~**10 fps** HD. Es la cámara.

### ¿ONVIF?
No. Solo RTSP.

### ¿El vídeo sale de casa?
Señalización a Tuya. En local: cámara → este PC. Móvil 4G = segundo visor cloud.

### ¿go2rtc `tuya://`?
Email/contraseña Tuya Smart, no QR Smart Life.

### ¿Cloud PTZ fuera de LAN?
LAN TCP **6668** primero. Fuera: API móvil reverse tras email+contraseña (`POST /api/cloud/auth`, `cloud_auth.json` 600) — sin claves IoT developer.

### ¿Dónde está el login?
`%APPDATA%\TuyaRtspBridge\` o `~/.local/share/tuya-rtsp-bridge/`.

### ¿Add-on Home Assistant?
Sí — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. [docker.md](docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md).
