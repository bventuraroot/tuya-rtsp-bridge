# Aan de slag

Werkt met camera’s in **Tuya Smart**, **Smart Life** of **iSmartLife**. Merk op de doos (LSC, Nous, BlitzWolf, generiek «Tuya») is oké zolang de telefoon-app een van die is.

## Eerste start
1. Windows: `TuyaRtspBridge-Setup.exe` van [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases) (Python/VLC/ffmpeg inbegrepen). Linux: `./launch.sh` of Arch. Docker/HA: [docker.md](docker.md).
2. Start **Tuya RTSP Bridge** (of headless `http://<host>:8787`).
3. Zelfde regio als de telefoon-app.
4. Create QR → scannen → **bevestigen**. QR is vast **320×320**.
5. Kopieer de HD-URL naar je NVR.

Sessies overleven reboots (`%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`). Alleen opnieuw scannen als Tuya de sessie gooit — met opgeslagen e-mail/wachtwoord kan de bridge de protect-sessie vernieuwen.

## Verhuizen / nieuw wifi
Device-IDs blijven gelijk als je camera’s **niet** uit het account verwijdert en **niet** factory-reset.

1. Op de nieuwe plek camera’s via de app op de nieuwe SSID.
2. Bridge starten op een pc in **datzelfde LAN**.
3. Agent/Frigate naar het **nieuwe pc-IP**; pad behouden (`/CameraName/hd`).

Geen remote SSID vanuit een andere stad pushen.

## PTZ
Pijl vasthouden = bewegen. Loslaten = stop.
- **LAN:** lokaal Tuya-protocol **TCP 6668** (zelfde subnet; VPN-ifaces overgeslagen).
- **Off-site:** optioneel **cloud-PTZ** na eenmalig e-mail+wachtwoord (`POST /api/cloud/auth`). Geen IoT Access ID/Secret.

## Preview
Windows Setup = VLC. Linux GUI = ffmpeg MJPEG-pipe. Fullscreen-knop; Esc terug. Preview optioneel.

## Autostart
Windows: snelkoppeling naar `launch-hidden.vbs` in Opstarten. Linux: `systemctl --user enable --now tuya-rtsp-bridge.service tuya-rtsp-gui.service`.
