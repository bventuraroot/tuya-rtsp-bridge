# Tuya RTSP Bridge

[![Lizenz: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md)

**Jede Tuya- / Smart-Life- / iSmartLife-Kamera als normales RTSP** — für Frigate, Agent DVR, go2rtc, Home Assistant oder VLC.

Kein Firmware-Flash. Kein ONVIF (gibt es auf der Stock-Firmware nicht). Einmal QR scannen, URL kopieren.

| Du bist… | Hier entlang |
|---|---|
| Soll einfach laufen | [In 5 Minuten](#in-5-minuten) |
| Heimnetz / NVR | [docs/nvr.md](docs/nvr.md) |
| Entwickler | [docs/architecture.md](docs/architecture.md) · [CONTRIBUTING.md](CONTRIBUTING.md) |

Im Repo stecken **keine** Konten, Geräte-IDs oder Heim-IPs.

## Was du bekommst

- HD: `rtsp://<dieser-PC>:8554/<Kameraname>/hd` (meist HEVC 1080p)
- SD: `…/sd` (H.264)
- Alle Kameras über **eine** Brücken-IP, nur der Pfad unterscheidet sich
- Vorschau, wenn [VLC](https://www.videolan.org/) installiert ist
- Deutsch oder English

Signalisierung bleibt Tuya-Cloud. Vom diesem PC aus bleibt das Video meist im LAN.

## Ehrliche Grenzen

- Kein ONVIF, kein Kamera-eigenes RTSP
- Viele Modelle liefern im HD-Strom etwa **10 fps** — das ist die Kamera
- VLC 3 zeigt HEVC/RTSP oft schwarz; Agent DVR / Frigate sind die Ziel-Clients
- Aufnehmen soll der NVR, nicht die Brücke

Regionen: Westeuropa, Osteuropa, USA West/Ost, China, Indien.

## In 5 Minuten

1. Windows 10/11, [Python 3.10+](https://www.python.org/downloads/) (**Add to PATH** ankreuzen), Smart-Life-Konto
2. `TuyaRtspBridge-Setup.exe` aus [Releases](../../releases) — Sprache wählen
3. App starten → Region wie im Handy (DE = **EU**) → **QR erzeugen** → in der App scannen und **bestätigen**
4. HD-URL kopieren nach Agent DVR / Frigate: `rtsp://127.0.0.1:8554/<Name>/hd`

Leere Kameraliste = oft falsche Region. QR „tut nichts“ = noch nicht bestätigt, einfach warten.

Daten: `%APPDATA%\TuyaRtspBridge\`. Programm: `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

Ausführlich: [docs/getting-started.md](docs/getting-started.md) · [docs/faq.md](docs/faq.md)

## Lizenz

MIT. Engine: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT). Nicht mit Tuya Inc. verbunden.
