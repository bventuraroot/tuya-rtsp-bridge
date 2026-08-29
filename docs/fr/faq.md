# FAQ

### Liste de caméras vide après login
Mauvaise région. « Europe de l’Ouest » dans l’app DE = **EU** (`protect-eu`), pas WE.

### Le QR ne se termine jamais
Gardez la fenêtre ouverte et **confirmez** sur le téléphone.

### QR minuscule / fente / illisible (Windows)
Corrigé en **1.2.4+** : canvas fixe **320×320** (NEAREST). Mettez à jour l’app/Setup. « No QR » avant Create QR est normal.

### Connexion refusée (WinError 10061)
L’UI démarre l’API locale (`:8787`) toute seule. Refaites Create QR ou redémarrez UI/API.

### VLC noir
VLC 3 échoue souvent sur HEVC/RTSP. Le flux vit. Agent/Frigate/ffplay. Linux : pipe MJPEG ffmpeg.

### 60 fps ?
Souvent ~**10 fps** HD HEVC — c’est la caméra.

### ONVIF ?
Non. RTSP uniquement.

### La vidéo quitte-t-elle la maison ?
Signaling vers Tuya. En local : caméra → ce PC. Téléphone 4G = second viewer cloud.

### go2rtc `tuya://` ?
Email/mot de passe Tuya Smart, pas QR Smart Life.

### Cloud PTZ hors LAN ?
LAN TCP **6668** d’abord. Hors site : API mobile reverse après email+mot de passe une fois (`POST /api/cloud/auth`, `cloud_auth.json` mode 600) — pas de clés IoT developer.

### Où est mon login ?
`%APPDATA%\TuyaRtspBridge\` ou `~/.local/share/tuya-rtsp-bridge/`. Jamais dans git.

### Add-on Home Assistant ?
Oui — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker : [docker.md](docker.md).

### Linux / macOS ?
`./launch.sh`. Arch : [arch-linux.md](../arch-linux.md).
