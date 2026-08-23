# Tuya RTSP-brug

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**Maak van elke Tuya- / Smart Life- / iSmartLife-camera een gewone RTSP-camera** — voor Frigate, Agent DVR, go2rtc, Home Assistant of VLC.

Geen firmware-flash. Geen ONVIF (de fabrieksfirmware heeft dat niet). Scan een QR en kopieer een RTSP-URL.

| Jij bent… | Begin hier |
|---|---|
| Je wilt dat het gewoon werkt | [In 5 minuten](#installatie-in-5-minuten) |
| Homelab / NVR | [docs/nvr.md](docs/nvr.md) |
| Ontwikkelaar | [docs/architecture.md](docs/architecture.md) |

Deze repository bevat **geen** accounts, apparaat-ID’s of thuis-IP’s.

## Waarom goedkope Tuya-camera’s dit nodig hebben

Die «Smart Life»-camera’s van €20–40 (vaak Action / LSC) lijken IP-camera’s. Dat zijn ze niet. Fabrieksfirmware: **geen ONVIF**, **geen RTSP-vinkje**. Live beeld gaat via de app van de fabrikant en een cloud die jij niet beheert. Een tweede telefoon of «cloud-NVR» is vaak een abonnement — of steelt de enige livesessie.

Jij hebt een sensor op *jouw* muur betaald. Opnames horen op *jouw* schijf.

Deze app is een lokale brug: scan een QR in de app die je al hebt, daarna heeft elke camera een gewone URL:

```
rtsp://<deze-pc>:8554/<Cameranaam>/hd
```

Signaling blijft bij Tuya. Vanaf deze pc blijft de video meestal op het LAN. Lange tekst: [docs/nl/why.md](docs/nl/why.md).

### De app

Eerste start — taal, regio, QR, bevestigen in Smart Life:

![Welkomstscherm. Lege lijst, geen QR, alleen localhost.](docs/images/ui-welcome.png)

Na inloggen — alleen demonamen. Previews in de docs zijn expres zwart (geen livebeeld):

![Twee voorbeeldcamera’s, HD-RTSP op 127.0.0.1.](docs/images/ui-ready.png)

## Credits

De RTSP-engine is **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** van **[seydx](https://github.com/seydx)** (MIT, commit `d65b3e9`). Zie [CREDITS.md](CREDITS.md) en [NOTICE.md](NOTICE.md).

## Wat je krijgt

- HD: `rtsp://<deze-pc>:8554/<Naam>/hd` (vaak HEVC 1080p)
- SD: `…/sd` (H.264)
- Alle camera’s delen **één** brug-IP; alleen het pad verandert
- Voorbeeld als [VLC](https://www.videolan.org/) is geïnstalleerd
- Talen: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Eerlijke grenzen

- Geen ONVIF, geen native RTSP op de camera
- Veel modellen geven ongeveer **10 fps** in HD — dat is de camera
- VLC 3 is vaak zwart bij HEVC/RTSP; gebruik Agent DVR / Frigate
- Neem op op je NVR, niet op de brug

Regio’s: West-/Oost-Europa, VS West/Oost, China, India.

## Installatie in 5 minuten

1. Windows 10/11 **of Arch Linux**
2. Een Smart Life- / Tuya Smart-account dat de camera’s al ziet

Windows: geen extra Python, VLC of ffmpeg — dat zit in de Setup.

Windows: `TuyaRtspBridge-Setup.exe` van [Releases](../../releases) — volgende, volgende, klaar. Details: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Inloggen: QR maken → scannen in Smart Life → **bevestigen** → `rtsp://127.0.0.1:8554/<Naam>/hd` kopiëren.

Sessies: `%APPDATA%\TuyaRtspBridge\` (Windows) of `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Licentie

Onze code: MIT. Meegeleverde engine: MIT, Copyright (c) 2025 seydx. Niet verbonden aan Tuya Inc.

Namen, lokale data, meegeleverde licenties: [docs/legal.md](docs/legal.md).
