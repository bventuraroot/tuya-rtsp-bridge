# Premiers pas

Caméras visibles dans **Tuya Smart**, **Smart Life** ou **iSmartLife**.

## Premier lancement
1. Windows : Setup depuis les [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux : `./launch.sh` / Arch. Docker/HA : [docker.md](docker.md).
2. Lancez **Tuya RTSP Bridge** (ou `http://<host>:8787`).
3. Même région que le téléphone.
4. Create QR → scanner → **confirmer**. QR fixe **320×320**.
5. Copiez l’URL HD dans le NVR.

Sessions : `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`. Relogin auto possible avec email/mot de passe sauvé.

## Déménagement / nouveau Wi‑Fi
Ne supprimez pas les caméras du compte. Nouveau SSID dans l’app, bridge sur le nouveau LAN, nouvelle IP PC dans le NVR, même chemin `/CameraName/hd`.

## PTZ
Flèches UI. LAN **TCP 6668**. Hors site : cloud PTZ après `POST /api/cloud/auth`.

## Aperçu
Windows Setup = VLC. Linux = ffmpeg MJPEG. Optionnel.

## Démarrage auto
Windows : `launch-hidden.vbs` dans Démarrage. Linux : `systemctl --user enable --now tuya-rtsp-bridge.service tuya-rtsp-gui.service`.
