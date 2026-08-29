# FAQ

### Kameraliste leer nach Login
Falsche Region. „Westeuropa“ in der DE-App = **EU** (`protect-eu`), nicht WE.

### QR wird nicht fertig
Fenster offen lassen und im Handy **bestätigen**.

### QR winzig / Schlitz / unscannbar (Windows)
Behoben ab **1.2.4+**: festes **320×320**-Canvas (NEAREST). App/Setup updaten. „Kein QR“ vor Klick auf **QR erzeugen** ist normal.

### Verbindung verweigert (WinError 10061)
UI startet die lokale API (`:8787`) selbst. Nochmal **QR erzeugen** oder UI/API neu starten.

### VLC schwarz
VLC 3 scheitert oft an HEVC/RTSP. Stream lebt trotzdem. Agent/Frigate. Linux-GUI: ffmpeg-MJPEG-Pipe.

### Ich wollte 60 fps
Viele Modelle liefern im HD-Stream ca. **10 fps**.

### ONVIF?
Nein. Nur RTSP.

### Verlässt Video das Haus?
Signaling zu Tuya. Lokal typisch Kamera → dieser PC im LAN.

### Cloud-PTZ ohne LAN?
LAN-PTZ (TCP **6668**) zuerst. Remote: Cloud-Fallback nach einmaligem Email/Passwort (`POST /api/cloud/auth`) — keine IoT-Developer-Keys.

### Home-Assistant-Add-on?
Ja — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host-Netz. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Daten: `~/.local/share/tuya-rtsp-bridge/`.
