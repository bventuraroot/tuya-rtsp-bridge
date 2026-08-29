# Domande frequenti

### Elenco telecamere vuoto
Regione sbagliata. «Europa occidentale» nell’app DE = **EU**, non WE.

### Il QR non finisce
Tieni la finestra aperta e **conferma** sul telefono.

### QR minuscolo / fessura / non scansionabile (Windows)
Risolto in **1.2.4+**: canvas fisso **320×320** (NEAREST). Aggiorna l’app. «No QR» prima di Create QR è normale.

### Connessione rifiutata (WinError 10061)
La UI avvia l’API (`:8787`) da sola. Riprova Create QR.

### VLC nero
VLC 3 fallisce spesso su HEVC/RTSP. Lo stream è vivo. Agent/Frigate. Linux: pipe MJPEG ffmpeg.

### Mi aspettavo 60 fps
Molti modelli danno ~**10 fps** in HD.

### È ONVIF?
No. Solo RTSP.

### Il video esce di casa?
Segnalazione a Tuya. In locale di solito camera → questo PC.

### Cloud PTZ fuori LAN?
Prima PTZ LAN (TCP **6668**). Fuori rete: cloud dopo email+password una volta (`POST /api/cloud/auth`) — senza chiavi IoT developer.

### Add-on Home Assistant?
Sì — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Dati: `~/.local/share/tuya-rtsp-bridge/`.
