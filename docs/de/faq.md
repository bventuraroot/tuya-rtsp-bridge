# FAQ

### Kameraliste leer nach Login

Falsche Region. „Westeuropa“ in der deutschen App ist **EU** (`protect-eu`), nicht WE. Anderen Cluster desselben Kontinents versuchen.

### QR wird nie fertig

Fenster offen lassen und im Handy **bestätigen**. Pending-Poll (`result: true` ohne User-ID) ist normal.

### QR winzig / horizontaler Schlitz / unscannbar (Windows)

Behoben ab **1.2.4+**: GUI zeichnet den QR auf festem **320×320**-Canvas (NEAREST), nicht als Tk-Label mit Zeichen-Zellen. App/Setup aktualisieren. Steht noch „Kein QR“, **QR erzeugen** klicken und warten — leerer Platzhalter davor ist normal.

### Backend: Verbindung verweigert (WinError 10061)

Die Desktop-UI startet die lokale API (`:8787`) selbst, wenn sie down war. Nochmal **QR erzeugen**, oder **UI/API neu starten**.

### VLC schwarz / Preview ist ein Schlitz

VLC 3 scheitert oft an HEVC über RTSP. Der Stream ist trotzdem **nicht** tot. Agent DVR, Frigate oder ffplay nutzen. Desktop-Preview braucht aktuelles VLC (Windows-Setup bringt es mit). Unter Linux nutzt die GUI eine ffmpeg-MJPEG-Pipe statt eingebettetem VLC.

### Ich wollte 60 fps

Viele Tuya-IPC-Modelle liefern im HD-HEVC-Stream ca. **10 fps**. Diese Bridge erfindet keine Frames.

### Ist das ONVIF?

Nein. Stock-Firmware von Tuya spricht kein ONVIF. Dieses Projekt ist nur RTSP.

### Verlässt Video das Haus?

Signaling (Login, WebRTC-Handshake) geht zu Tuya. Wenn du über diesen PC schaust, läuft das Medium typisch Kamera → dieser PC im LAN. Handy im Mobilfunk = **zweiter** Viewer über Cloud-Pfad.

### Kann ich go2rtc `tuya://` stattdessen nutzen?

Das braucht Tuya-Smart-**E-Mail/Passwort**, nicht Smart-Life-QR. Anderer Login.

### Cloud-PTZ ohne LAN?

LAN-PTZ (TCP **6668**) hat Vorrang, wenn die Kamera erreichbar ist. Remote: Fallback über reverse Mobile-API (`tuya.m.device.dp.publish`) mit **Smart-Life-/Tuya-Smart-E-Mail + Passwort** einmal (nur lokal in `cloud_auth.json`, mode 600 — keine Tuya-IoT-Platform-Developer-Keys). Setzen via `POST /api/cloud/auth` oder beim ersten Cloud-PTZ, sobald Creds da sind.

### HLS / VLC HTTP?

Optional und teuer (x264-Transcode). Standard aus. Agent/Frigate sollen RTSP `/hd` nutzen.

### Wo liegt mein Login?

`%APPDATA%\TuyaRtspBridge\` (Windows) oder `~/.local/share/tuya-rtsp-bridge/` (Linux) — Cookies, Kameraliste, optionales Cloud-Passwort. Ordner nie in Git oder Screenshots.

### Home-Assistant-Add-on?

Ja — Supervisor-Add-on unter [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Braucht **Host-Netz**. Plain Docker auf dem HA-Host geht auch: [docker.md](docker.md).

### Linux / macOS?

`./launch.sh` aus dem Clone. Arch-Paket: [arch-linux.md](../arch-linux.md). Daten: `~/.local/share/tuya-rtsp-bridge/`.
