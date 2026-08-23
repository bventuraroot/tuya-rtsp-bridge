# Rechtliches

Das ist kein Anwaltsschreiben. Es erklärt, wofür das Programm gedacht ist.

## Was das ist

Ein lokales Hilfsprogramm auf **deinem** Rechner. QR in Smart Life / Tuya Smart / iSmartLife scannen, danach bietet dieser PC RTSP im LAN an.

Es ist **kein** offizielles Tuya-Produkt. Tuya, Smart Life, iSmartLife und die zugehörigen Zeichen gehören ihren Inhabern. Die Namen stehen hier nur, damit klar ist, mit welchen Kameras das Ding spricht.

Die Anmeldung am Handy läuft weiter über Tuya-Server. Für **dein** Konto gelten deren Bedingungen. Wenn das nicht passt: nicht scannen.

## Was wir nicht tun

- Keine Telemetrie, kein stilles Nach-Hause-Telefonieren, keine Werbung
- Keine Konten, Geräte-IDs oder Videos im Git oder im Setup
- Sitzung und Kameraliste liegen in `%APPDATA%\TuyaRtspBridge\` (Windows) bzw. `~/.local/share/tuya-rtsp-bridge/` (Linux)
- Kein Firmware-Flash, kein ONVIF

## Deine Daten

Dieses Programm betreibt keine Cloud. Was Tuya schon sieht (Login, Signalisierung), sieht Tuya weiter. Video, das du über diesen PC anschaust, bleibt meist Kamera → dieser Rechner im LAN. Ein Handy im Mobilfunk ist ein zweiter Zuschauer und geht den Cloud-Weg.

Datenordner löschen = lokale Sitzung weg.

## Lizenzen im Windows-Setup

Unser Code: MIT. RTSP-Engine: MIT (seydx). Texte: [NOTICE.md](../NOTICE.md), [DEPENDENCIES.md](../DEPENDENCIES.md).

Das Setup legt **unveränderte** Fremdbinaries neben die App (nicht fest in unseren Python-Code gelinkt):

| Binary | Lizenz dieses Binary | Zugehörige Quellen |
|---|---|---|
| Offizielles VideoLAN VLC 3 (win64-Zip) | GPL-2.0 für den Player; libVLC ist LGPL-2.1+ | https://www.videolan.org |
| ffmpeg 9.0.1 essentials (Gyan, `--enable-gpl`) | GPL-3.0 | https://ffmpeg.org und https://www.gyan.dev/ffmpeg/builds/ |
| Privates CPython 3.12 | PSF | https://www.python.org |

ffmpeg läuft als eigener Prozess. VLC kommt als `libvlc` in die optionale Vorschau. Beides darfst du durch einen anderen offiziellen Build ersetzen.

Inno Setup ist nur der Compiler für die Setup.exe, keine mitgelieferte Bibliothek. Dieses Projekt wird verschenkt (MIT, keine Bezahlversion).

## Gewähr

MIT: wie es ist. Kein Versprechen, dass jedes Modell, jede Region oder jeder Tuya-API-Wechsel ewig läuft. Aufnehmen soll der NVR.

## Kontakt

Fehler und Sicherheit: das GitHub-Repo. Keine Cookies, kein `localKey`, kein Livebild schicken.
