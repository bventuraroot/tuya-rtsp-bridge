# FAQ

### Liste de caméras vide
Mauvaise région. « Europe de l’Ouest » dans l’app DE = **EU**, pas WE.

### Le QR ne se termine pas
Gardez la fenêtre ouverte et **confirmez** sur le téléphone.

### QR minuscule / fente / illisible (Windows)
Corrigé en **1.2.4+** : canvas fixe **320×320** (NEAREST). Mettez à jour l’app. « No QR » avant **Create QR** est normal.

### Connexion refusée (WinError 10061)
L’UI démarre l’API (`:8787`) toute seule. Refaites **Create QR** ou redémarrez UI/API.

### VLC noir
VLC 3 échoue souvent sur HEVC/RTSP. Le flux vit. Agent/Frigate. Linux : pipe MJPEG ffmpeg.

### J’attendais 60 fps
Beaucoup de modèles font ~**10 fps** en HD.

### C’est de l’ONVIF ?
Non. RTSP seulement.

### La vidéo quitte-t-elle la maison ?
Signaling vers Tuya. En local : caméra → ce PC en général.

### PTZ cloud hors LAN ?
PTZ LAN (TCP **6668**) d’abord. Hors site : cloud après email+mot de passe une fois (`POST /api/cloud/auth`) — pas de clés IoT developer.

### Add-on Home Assistant ?
Oui — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker : [docker.md](../docker.md).

### Linux / macOS ?
`./launch.sh`. Arch : [arch-linux.md](../arch-linux.md). Données : `~/.local/share/tuya-rtsp-bridge/`.
