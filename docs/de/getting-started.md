# Erste Schritte

Funktioniert mit Kameras, die in **Tuya Smart**, **Smart Life** oder **iSmartLife** erscheinen. Markennamen auf der Box (LSC, Nous, BlitzWolf, generisch „Tuya“) sind egal, solange die Handy-App eine davon ist.

## Erster Start

1. Windows: `TuyaRtspBridge-Setup.exe` aus den [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases) (Python/VLC/ffmpeg inklusive). Linux: `./launch.sh` oder Arch-Paket. Docker / HA OS: [docker.md](docker.md).
2. **Tuya RTSP Bridge** starten (oder headless `http://<host>:8787`).
3. Region wie in der Handy-App (Deutschland → **EU**).
4. QR erzeugen → scannen → im Handy **bestätigen**. QR ist fest **320×320**, damit Handys ihn lesen.
5. HD-URL in den NVR kopieren.

Sessions überleben Reboots (`%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`). Nur neu scannen, wenn Tuya die Session schmeißt — mit gespeichertem E-Mail/Passwort kann die Bridge die Protect-Session automatisch erneuern.

## Umzug / neues WLAN

Geräte-IDs bleiben gleich, wenn du Kameras **nicht** aus dem Konto löschst und **nicht** factory-resettest.

1. Am neuen Ort Kameras per App auf neue SSID bringen (Pairing / „Netzwerk wechseln“).
2. Bridge auf einem PC **im gleichen LAN** starten.
3. Agent/Frigate auf die **neue PC-IP** zeigen; Pfad beibehalten (`/CameraName/hd`).

Keine Remote-SSID aus einer anderen Stadt pushen — die Kamera hält nur ein Netz und geht offline.

## PTZ

Pfeil in der Desktop-UI halten = bewegen. Loslassen = stop.

- **Im LAN:** lokales Tuya-Protokoll auf **TCP 6668** (gleiches Subnetz; VPN-Interfaces werden übersprungen).
- **Remote / kein LAN-Pfad:** optional **Cloud-PTZ** über reverse Smart-Life-/Tuya-App-API nach einmaligem Speichern von E-Mail+Passwort (`POST /api/cloud/auth`). Keine IoT-Platform Access ID/Secret.

Nicht jedes Modell exponiert PTZ-Datenpunkte.

## Preview

Windows-Setup bringt VLC mit. Unter Linux nutzt die GUI eine ffmpeg-Live-MJPEG-Pipe (kein X11-VLC-Embed). Vollbild per Button; Esc zurück.

Preview ist optional. RTSP für Frigate/Agent läuft ohne.

## Autostart

Windows: Verknüpfung auf `launch-hidden.vbs` im Autostart-Ordner — startet API/Engine ohne Fenster. `launch.bat` für Desktop-UI.

Linux (user-systemd nach Arch-Paket): `systemctl --user enable --now tuya-rtsp-bridge.service tuya-rtsp-gui.service`.
