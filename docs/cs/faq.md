# Časté otázky

### Prázdný seznam kamer
Špatný region. «Západní Evropa» v DE app = **EU**, ne WE.

### QR se nedokončí
Okno otevřené a **potvrďte** v telefonu.

### QR štěrbina (Windows)
Opraveno v **1.2.4+**: plátno **320×320** (NEAREST). Aktualizujte Setup.

### WinError 10061
UI spustí API `:8787` samo. Znovu Create QR.

### VLC černé
Stream žije. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps?
Často ~**10 fps** HD.

### ONVIF?
Ne. Jen RTSP.

### Odejde video z domu?
Signaling k Tuya. Lokálně: kamera → tento PC.

### go2rtc `tuya://`?
Email/heslo Tuya Smart, ne QR Smart Life.

### Cloud PTZ mimo LAN?
Nejdřív LAN TCP **6668**. Vzdáleně: `POST /api/cloud/auth`, `cloud_auth.json` mode 600. Bez IoT developer keys.

### Kde je login?
`%APPDATA%\TuyaRtspBridge\` nebo `~/.local/share/tuya-rtsp-bridge/`.

### HA add-on?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). [docker.md](docker.md).

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md).
