# Démarrage

Fonctionne avec les caméras visibles dans **Tuya Smart**, **Smart Life** ou **iSmartLife**.

1. Windows : `TuyaRtspBridge-Setup.exe` depuis Releases (Python/VLC/ffmpeg inclus). Linux : `./launch.sh`.
2. Démarrer **Tuya RTSP Bridge**.
3. Choisir la même région que dans le téléphone.
4. Créer le QR → scanner → **confirmer**.
5. Copier l’URL HD dans le NVR.

Sessions : `%APPDATA%\TuyaRtspBridge` ou `~/.local/share/tuya-rtsp-bridge/`.

Nouveau Wi‑Fi : ne **pas** supprimer les caméras du compte. Changer le réseau dans l’appli sur place, relancer le pont, changer seulement l’IP du PC dans le NVR.

PTZ : maintenir une flèche = bouger, relâcher = stop. Protocole local TCP **6668**.
