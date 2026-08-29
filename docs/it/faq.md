# Domande frequenti

### Elenco telecamere vuoto
Regione sbagliata. «Europa occidentale» app DE = **EU**, non WE.

### Il QR non finisce
Finestra aperta e **conferma** sul telefono.

### QR minuscolo / fessura (Windows)
Risolto in **1.2.4+**: canvas fisso **320×320** (NEAREST). Aggiorna Setup.

### Connessione rifiutata (WinError 10061)
La UI avvia l’API (`:8787`) da sola. Riprova Create QR.

### VLC nero
Lo stream è vivo. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps?
Spesso ~**10 fps** HD.

### ONVIF?
No. Solo RTSP.

### Il video esce di casa?
Segnalazione a Tuya. In locale: camera → questo PC.

### go2rtc `tuya://`?
Email/password Tuya Smart, non QR Smart Life.

### Cloud PTZ fuori LAN?
LAN TCP **6668** prima. Remoto: `POST /api/cloud/auth`, `cloud_auth.json` mode 600. Niente chiavi IoT developer.

### Dove sta il login?
`%APPDATA%\TuyaRtspBridge\` o `~/.local/share/tuya-rtsp-bridge/`.

### Add-on Home Assistant?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). [docker.md](docker.md).

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md).
