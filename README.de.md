# Tuya RTSP Bridge (Deutsch)

Lokaler QR-Login für Tuya / Smart Life / iSmartLife → **RTSP** für Frigate, Agent DVR, go2rtc, VLC.

Englisch und Deutsch wählbar (Installer und App). Dieses Repo enthält **keine** Konten, Geräte-IDs oder LAN-Adressen.

## Was es macht

- QR in Tuya Smart / Smart Life scannen (EU, US, …)
- Kameras im Konto finden
- `rtsp://<dieser-PC>:8554/<Kameraname>/hd` (HEVC) und `/sd` (H.264)
- Optionales LAN-PTZ (Port 6668)
- Optionale Vorschau über VLC (separat installieren)
- Optionaler Wächter, der eine tote Engine neu startet

Es gibt **kein ONVIF** auf der Stock-Firmware.

## Anforderungen

Python 3.10+ (PSF), optional [VLC](https://www.videolan.org/) (LGPL) für die Vorschau, optional ffmpeg für den Wächter.

Details: [DEPENDENCIES.md](DEPENDENCIES.md).

## Start

```bat
launch.bat
```

Daten liegen unter `%APPDATA%\TuyaRtspBridge\` — nie ins Git.

Englische Anleitung: [README.md](README.md).
