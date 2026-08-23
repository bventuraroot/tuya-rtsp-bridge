# Tuya RTSP most

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**Proměňte jakoukoli kameru Tuya / Smart Life / iSmartLife na běžnou RTSP kameru** — pro Frigate, Agent DVR, go2rtc, Home Assistant nebo VLC.

Žádný flash firmwaru. Žádné ONVIF (tovární firmware ho nemá). Naskenujte QR a zkopírujte RTSP adresu.

| Jste… | Začněte zde |
|---|---|
| Chcete, aby to jen fungovalo | [Za 5 minut](#instalace-za-5-minut) |
| Laboratoř / NVR | [docs/nvr.md](docs/nvr.md) |
| Vývojář | [docs/architecture.md](docs/architecture.md) |

Tento repozitář **neobsahuje** účty, ID zařízení ani domácí IP.

## Proč to levné Tuya kamery potřebují

Ty 20–40€ «Smart Life» kamery vypadají jako IP kamery. Nejsou. Tovární firmware: **žádné ONVIF**, **žádné políčko RTSP**. Živý náhled jde přes aplikaci výrobce a cloud, který neřídíte. Druhý telefon nebo «cloud NVR» často chce předplatné — nebo ukradne jedinou živou relaci.

Zaplatili jste senzor na *vaší* zdi. Záznam patří na *váš* disk.

Tato aplikace je malý místní most: naskenujte QR v aplikaci, kterou už máte, a každá kamera má běžnou adresu:

```
rtsp://<tento-pc>:8554/<NazevKamery>/hd
```

Signaling zůstává u Tuya. Z tohoto PC video obvykle zůstane v LAN. Delší text: [docs/cs/why.md](docs/cs/why.md).

### Aplikace

První spuštění — jazyk, region, QR, potvrzení ve Smart Life:

![Uvítací obrazovka. Prázdný seznam, žádný QR, jen localhost.](docs/images/ui-welcome.png)

Po přihlášení — jen ukázkové názvy. Náhledy jsou záměrně černé (v dokumentaci není živé video):

![Dvě fiktivní kamery, HD RTSP na 127.0.0.1.](docs/images/ui-ready.png)

## Poděkování

RTSP engine je **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** od **[seydx](https://github.com/seydx)** (MIT, commit `d65b3e9`). Viz [CREDITS.md](CREDITS.md) a [NOTICE.md](NOTICE.md).

## Co dostanete

- HD: `rtsp://<tento-pc>:8554/<Nazev>/hd` (obvykle HEVC 1080p)
- SD: `…/sd` (H.264)
- Všechny kamery sdílejí **jednu** IP mostu; mění se jen cesta
- Náhled, pokud je nainstalovaný [VLC](https://www.videolan.org/)
- Jazyky: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Čestné limity

- Žádné ONVIF, žádné nativní RTSP na kameře
- Mnoho modelů dává v HD zhruba **10 fps** — to je kamera
- VLC 3 je u HEVC/RTSP často černé; použijte Agent DVR / Frigate
- Nahrávejte na svém NVR, ne na mostě

Regiony: západní/východní Evropa, USA západ/východ, Čína, Indie.

## Instalace za 5 minut

1. Windows 10/11 **nebo Arch Linux**
2. Účet Smart Life / Tuya Smart, který už kamery vidí

Ve Windows Python, VLC ani ffmpeg neinstalujte — jsou v Setupu.

Windows: `TuyaRtspBridge-Setup.exe` z [Releases](../../releases) — další, další, dokončit. Podrobnosti: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Přihlášení: vytvořit QR → naskenovat ve Smart Life → **potvrdit** → zkopírovat `rtsp://127.0.0.1:8554/<Nazev>/hd`.

Relace: `%APPDATA%\TuyaRtspBridge\` (Windows) nebo `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Licence

Náš kód: MIT. Dodaný engine: MIT, Copyright (c) 2025 seydx. Není přidruženo k Tuya Inc.
