# Most RTSP Tuya

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md)

**Zamień dowolną kamerę Tuya / Smart Life / iSmartLife w zwykłą kamerę RTSP** — dla Frigate, Agent DVR, go2rtc, Home Assistant lub VLC.

Bez flashowania firmware. Bez ONVIF (fabryczny firmware go nie ma). Zeskanuj QR i skopiuj adres RTSP.

| Jesteś… | Zacznij tutaj |
|---|---|
| Chcesz, żeby po prostu działało | [W 5 minut](#instalacja-w-5-minut) |
| Homelab / NVR | [docs/nvr.md](docs/nvr.md) |
| Deweloper | [docs/architecture.md](docs/architecture.md) |

To repozytorium **nie** zawiera kont, ID urządzeń ani domowych IP.

## Dlaczego tanie kamery Tuya tego potrzebują

Kamery «Smart Life» za 20–40 € wyglądają jak kamery IP. Nie są. Fabryczny firmware: **brak ONVIF**, **brak opcji RTSP**. Podgląd idzie przez aplikację producenta i chmurę, której nie kontrolujesz. Drugi telefon lub «NVR w chmurze» to często abonament — albo kradnie jedyną sesję na żywo.

Zapłaciłeś za czujnik na *swojej* ścianie. Nagrania powinny iść na *twój* dysk.

Ta aplikacja to lokalny most: zeskanuj QR w aplikacji, którą już masz, a każda kamera dostanie zwykły adres:

```
rtsp://<ten-pc>:8554/<NazwaKamery>/hd
```

Sygnalizacja zostaje u Tuya. Z tego PC wideo zwykle zostaje w LAN. Dłuższy tekst: [docs/pl/why.md](docs/pl/why.md).

### Aplikacja

Pierwsze uruchomienie — język, region, QR, potwierdzenie w Smart Life:

![Ekran powitalny. Pusta lista, brak QR, tylko localhost.](docs/images/ui-welcome.png)

Po logowaniu — tylko nazwy demonstracyjne. Podglądy w dokumentacji są celowo czarne (bez żywego wideo):

![Dwie przykładowe kamery, HD RTSP na 127.0.0.1.](docs/images/ui-ready.png)

## Podziękowania

Silnik RTSP to **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** od **[seydx](https://github.com/seydx)** (MIT, commit `d65b3e9`). Zobacz [CREDITS.md](CREDITS.md) i [NOTICE.md](NOTICE.md).

## Co dostajesz

- HD: `rtsp://<ten-pc>:8554/<Nazwa>/hd` (zwykle HEVC 1080p)
- SD: `…/sd` (H.264)
- Wszystkie kamery dzielą **jeden** IP mostu; zmienia się tylko ścieżka
- Podgląd, jeśli zainstalujesz [VLC](https://www.videolan.org/)
- Języki: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Uczciwe ograniczenia

- Brak ONVIF, brak natywnego RTSP na kamerze
- Wiele modeli w HD daje około **10 kl./s** — tak działa kamera
- VLC 3 często jest czarny przy HEVC/RTSP; użyj Agent DVR / Frigate
- Nagrywaj na swoim NVR, nie na moście

Regiony: Europa Zachodnia/Wschodnia, USA Zachód/Wschód, Chiny, Indie.

## Instalacja w 5 minut

1. Windows 10/11 **lub Arch Linux**
2. Konto Smart Life / Tuya Smart, które już widzi kamery

Na Windowsie nie instaluj Pythona, VLC ani ffmpeg — są w Setupie.

Windows: `TuyaRtspBridge-Setup.exe` z [Releases](../../releases) — dalej, dalej, zakończ. Szczegóły: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Logowanie: utwórz QR → zeskanuj w Smart Life → **potwierdź** → skopiuj `rtsp://127.0.0.1:8554/<Nazwa>/hd`.

Sesje: `%APPDATA%\TuyaRtspBridge\` (Windows) lub `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Licencja

Nasz kod: MIT. Dołączony silnik: MIT, Copyright (c) 2025 seydx. Niepowiązane z Tuya Inc.
