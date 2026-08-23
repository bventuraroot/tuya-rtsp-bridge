# Ponte RTSP Tuya

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**Trasforma qualsiasi telecamera Tuya / Smart Life / iSmartLife in una telecamera RTSP normale** — per Frigate, Agent DVR, go2rtc, Home Assistant o VLC.

Niente flash del firmware. Niente ONVIF (il firmware di serie non ce l’ha). Scansiona un QR e copia un URL RTSP.

| Sei… | Inizia qui |
|---|---|
| Vuoi solo che funzioni | [In 5 minuti](#installazione-in-5-minuti) |
| Laboratorio / NVR | [docs/nvr.md](docs/nvr.md) |
| Sviluppatore | [docs/architecture.md](docs/architecture.md) |

Questo repository **non** contiene account, ID dispositivo o IP di casa.

## Perché le telecamere Tuya economiche ne hanno bisogno

Quelle telecamere «Smart Life» da 20–40 € sembrano IP. Non lo sono. Firmware di serie: **niente ONVIF**, **niente casella RTSP**. Il live passa dall’app del produttore e da un cloud che non controlli. Un secondo telefono o un «NVR cloud» è spesso un abbonamento — o ruba l’unica sessione live.

Hai pagato un sensore sul *tuo* muro. La registrazione deve finire sul *tuo* disco.

Questa app è un ponte locale: scansiona un QR nell’app che hai già e ogni telecamera ha un URL normale:

```
rtsp://<questo-pc>:8554/<NomeTelecamera>/hd
```

La segnalazione resta su Tuya. Da questo PC il video di solito resta sulla LAN. Testo lungo: [docs/it/why.md](docs/it/why.md).

### L’applicazione

Primo avvio — lingua, regione, QR, conferma in Smart Life:

![Schermata di benvenuto. Elenco vuoto, nessun QR, solo localhost.](docs/images/ui-welcome.png)

Dopo l’accesso — solo nomi demo. Le anteprime restano nere di proposito (niente video nella documentazione):

![Due telecamere fittizie, RTSP HD su 127.0.0.1.](docs/images/ui-ready.png)

## Crediti

Il motore RTSP è **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** di **[seydx](https://github.com/seydx)** (MIT, commit `d65b3e9`). Vedi [CREDITS.md](CREDITS.md) e [NOTICE.md](NOTICE.md).

## Cosa ottieni

- HD: `rtsp://<questo-pc>:8554/<Nome>/hd` (di solito HEVC 1080p)
- SD: `…/sd` (H.264)
- Tutte le telecamere condividono **un** IP del ponte; cambia solo il percorso
- Anteprima se [VLC](https://www.videolan.org/) è installato
- Lingue: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Limiti onesti

- Niente ONVIF, niente RTSP nativo sulla telecamera
- Molti modelli escono a circa **10 fps** in HD — è la telecamera
- VLC 3 è spesso nero con HEVC/RTSP; usa Agent DVR / Frigate
- Registra sul tuo NVR, non sul ponte

Regioni: Europa occidentale/orientale, USA Ovest/Est, Cina, India.

## Installazione in 5 minuti

1. Windows 10/11 **o Arch Linux**
2. Un account Smart Life / Tuya Smart che vede già le telecamere

Su Windows non serve installare Python, VLC o ffmpeg: sono nel Setup.

Windows: `TuyaRtspBridge-Setup.exe` da [Releases](../../releases) — avanti, avanti, fine. Dettagli: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Accesso: crea QR → scansiona in Smart Life → **conferma** → copia `rtsp://127.0.0.1:8554/<Nome>/hd`.

Sessioni: `%APPDATA%\TuyaRtspBridge\` (Windows) o `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Licenza

Il nostro codice: MIT. Motore incluso: MIT, Copyright (c) 2025 seydx. Non affiliato a Tuya Inc.
