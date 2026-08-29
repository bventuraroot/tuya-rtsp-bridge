# Premiers pas

Caméras dans **Tuya Smart**, **Smart Life** ou **iSmartLife**.

## Premier lancement
1. Windows : Setup des Releases. Linux : `./launch.sh` / Arch. Docker/HA : [docker.md](../docker.md).
2. Lancez **Tuya RTSP Bridge** (ou `http://<host>:8787`).
3. Même région que le téléphone.
4. Create QR → scanner → **confirmer**. QR fixe **320×320**.
5. Copiez l’URL HD dans le NVR.

## PTZ
Flèches dans l’UI. **LAN :** TCP **6668**. **Hors site :** cloud après email+mot de passe (`POST /api/cloud/auth`) — pas de clés IoT.

## Aperçu
Windows Setup = VLC. Linux = ffmpeg MJPEG. Le RTSP n’en a pas besoin.
