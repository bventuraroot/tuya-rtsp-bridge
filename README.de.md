# Tuya RTSP Bridge

[![Lizenz: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Français](README.fr.md)](README.fr.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md)

**Jede Tuya- / Smart-Life- / iSmartLife-Kamera als normales RTSP** — für Frigate, Agent DVR, go2rtc, Home Assistant oder VLC.

Kein Firmware-Flash. Kein ONVIF (gibt es auf der Stock-Firmware nicht). Einmal QR scannen, URL kopieren.

| Du bist… | Hier entlang |
|---|---|
| Soll einfach laufen | [In 5 Minuten](#in-5-minuten) |
| Heimnetz / NVR | [docs/nvr.md](docs/nvr.md) |
| Entwickler | [docs/architecture.md](docs/architecture.md) · [CONTRIBUTING.md](CONTRIBUTING.md) |

Im Repo stecken **keine** Konten, Geräte-IDs oder Heim-IPs.

## Warum billige Tuya-Cams das brauchen

Die 20–40-€-„Smart-Life“-Kamera sieht aus wie eine IP-Cam. Ist sie nicht. Stock-Firmware: **kein ONVIF**, **kein RTSP**. Live nur über die Hersteller-App und eine Cloud, die du nicht kontrollierst. Zweites Handy oder „Cloud-NVR“ heißt oft Abo — oder klaut die einzige Live-Session.

Du hast einen Sensor an deiner Wand bezahlt. Aufnehmen gehört auf **deine** Platte.

Dieses Programm ist eine kleine lokale Brücke: QR in der App scannen, die du schon hast. Danach ist jede Kamera eine normale URL für Frigate, Agent DVR, go2rtc, Home Assistant oder VLC:

```
rtsp://<dieser-PC>:8554/<Kameraname>/hd
```

Die Anmeldung bleibt bei Tuya. Vom diesem PC aus bleibt das Video typischerweise im LAN. Länger: [docs/warum.md](docs/warum.md).

### Die Oberfläche

Erster Start — Sprache, Region, QR, in Smart Life bestätigen:

![Startbildschirm. Leere Liste, kein QR, nur localhost.](docs/images/ui-welcome.png)

Nach dem Login — nur Demo-Namen (`Front yard`, `Driveway`). Die Vorschau bleibt in der Doku absichtlich schwarz (kein Livebild):

![Zwei Platzhalter-Kameras, HD-RTSP auf 127.0.0.1.](docs/images/ui-ready.png)

## Credits

Die RTSP-Engine ist **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** von **[seydx](https://github.com/seydx)** (MIT), Stand Commit `d65b3e9`, plus drei lokale Patches. Siehe [CREDITS.md](CREDITS.md) und [NOTICE.md](NOTICE.md).

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

Unser Code: MIT ([LICENSE](LICENSE)).  
Vendored Engine: MIT, Copyright (c) 2025 seydx — [NOTICE.md](NOTICE.md).

Nicht mit Tuya Inc. verbunden.
