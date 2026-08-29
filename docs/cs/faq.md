# Časté otázky

### Seznam kamer je prázdný
Špatný region. «Západní Evropa» v německé aplikaci je **EU**, ne WE.

### QR se nedokončí
Nechte okno otevřené a **potvrďte** v telefonu.

### QR je malý / štěrbina / nenačte se (Windows)
Opraveno v **1.2.4+**: GUI kreslí QR na pevném plátně **320×320** (NEAREST). Aktualizujte app/Setup. Prázdný box „No QR“ je normální před **Create QR**.

### Spojení odmítnuto (WinError 10061)
UI teď API (`:8787`) spustí samo. Znovu **Create QR** nebo Restart UI/API.

### VLC je černé
VLC 3 u HEVC/RTSP často selže. Stream není mrtvý. Agent DVR / Frigate. Na Linuxu GUI používá ffmpeg MJPEG.

### Čekal jsem 60 fps
Mnoho modelů dává v HD zhruba **10 fps**.

### Je to ONVIF?
Ne. Jen RTSP.

### Odchází video z domu?
Signaling jde k Tuya. Lokálně je médium obvykle kamera → tento PC.

### Cloud PTZ mimo LAN?
LAN PTZ (TCP **6668**) má přednost. Mimo síť: cloud fallback přes reverse app API po uložení email+hesla (`POST /api/cloud/auth`) — bez IoT developer keys.

### Home Assistant add-on?
Ano — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Data: `~/.local/share/tuya-rtsp-bridge/`.
