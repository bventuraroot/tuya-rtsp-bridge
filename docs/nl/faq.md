# Veelgestelde vragen

### Cameralijst leeg na login
Verkeerde regio. «West-Europa» in de Duitse app is **EU** (`protect-eu`), niet WE. Probeer het andere cluster op hetzelfde continent.

### QR wordt nooit klaar
Laat het venster open en **bevestig** op de telefoon. Pending poll (`result: true` zonder user-id) is normaal.

### QR piepklein / horizontale spleet / onleesbaar (Windows)
Opgelost in **1.2.4+**: GUI tekent de QR op een vast **320×320**-canvas (NEAREST), geen Tk-Label met teken-cellen. Update app/Setup. Staat er nog «No QR», klik **Create QR** en wacht — lege placeholder daarvoor is normaal.

### Backend verbinding geweigerd (WinError 10061)
De desktop-UI start de lokale API (`:8787`) zelf als die down was. Opnieuw **Create QR**, of herstart UI/API.

### VLC zwart / preview is een spleet
VLC 3 faalt vaak op HEVC over RTSP. De stream is **niet** dood. Gebruik Agent DVR, Frigate of ffplay. Desktop-preview heeft actuele VLC nodig (Windows Setup bundelt die). Op Linux gebruikt de GUI een ffmpeg-MJPEG-pipe i.p.v. embedded VLC.

### Ik wou 60 fps
Veel Tuya-IPC-modellen doen ~**10 fps** in de HD-HEVC-stream. Deze bridge verzint geen frames.

### Is dit ONVIF?
Nee. Stock-Tuya-firmware spreekt geen ONVIF. Dit project is alleen RTSP.

### Verlaat video het huis?
Signaling (login, WebRTC-handshake) gaat naar Tuya. Kijk je via deze pc, dan is medium typisch camera → deze pc op LAN. Telefoon op mobiel data = **tweede** viewer via cloud.

### Kan ik go2rtc `tuya://` gebruiken?
Dat vraagt Tuya Smart **e-mail/wachtwoord**, geen Smart Life-QR. Andere login.

### Cloud-PTZ buiten LAN?
LAN-PTZ (TCP **6668**) heeft voorrang. Off-site: fallback via reverse mobile API (`tuya.m.device.dp.publish`) met **Smart Life / Tuya Smart e-mail + wachtwoord** eenmaal (alleen lokaal `cloud_auth.json`, mode 600 — geen IoT Platform developer keys). Via `POST /api/cloud/auth`.

### HLS / VLC HTTP?
Optioneel en zwaar (x264). Standaard uit. Agent/Frigate: RTSP `/hd`.

### Waar staat mijn login?
`%APPDATA%\TuyaRtspBridge\` (Windows) of `~/.local/share/tuya-rtsp-bridge/` (Linux). Nooit in git of screenshots.

### Home Assistant add-on?
Ja — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). **Host-netwerk** verplicht. Docker: [docker.md](docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Data: `~/.local/share/tuya-rtsp-bridge/`.
