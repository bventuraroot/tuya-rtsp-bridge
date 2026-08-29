# Veelgestelde vragen

### Cameralijst leeg na login
Verkeerde regio. «West-Europa» in DE-app = **EU**, niet WE.

### QR raakt niet klaar
Laat het venster open en **bevestig** op de telefoon.

### QR piepklein / spleet / onleesbaar (Windows)
Opgelost in **1.2.4+**: vast **320×320**-canvas (NEAREST). Update de app. «No QR» vóór Create QR is normaal.

### Verbinding geweigerd (WinError 10061)
UI start de API (`:8787`) zelf. Opnieuw Create QR.

### VLC zwart
VLC 3 faalt vaak op HEVC/RTSP. Stream leeft. Agent/Frigate. Linux: ffmpeg-MJPEG-pipe.

### Ik wou 60 fps
Veel modellen doen ~**10 fps** in HD.

### Is dit ONVIF?
Nee. Alleen RTSP.

### Verlaat video het huis?
Signaling naar Tuya. Lokaal meestal camera → deze pc.

### Cloud-PTZ buiten LAN?
Eerst LAN-PTZ (TCP **6668**). Remote: cloud na eenmalig email+wachtwoord (`POST /api/cloud/auth`) — geen IoT-developer-keys.

### Home Assistant-add-on?
Ja — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host-netwerk. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Data: `~/.local/share/tuya-rtsp-bridge/`.
