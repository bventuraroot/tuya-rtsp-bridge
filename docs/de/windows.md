# Windows-Installer (noob / foolproof)

Doppelklick auf **TuyaRtspBridge-Setup.exe** aus den [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Weiter, Weiter, Fertig.

Der Wizard folgt der Windows-Sprache, wenn Inno ein Paket hat (Englisch, Deutsch, Niederländisch, Französisch, Spanisch, Portugiesisch, Italienisch, Polnisch, Tschechisch, Russisch, Ukrainisch, Japanisch, Koreanisch, Hebräisch). Chinesisch, Hindi, Indonesisch und Jiddisch sind nach dem ersten Start im App-Menü.

Du brauchst **kein** separates Python, VLC, ffmpeg oder Git. Setup kopiert eine private Runtime nach `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## Nach der Installation

1. **Tuya RTSP Bridge** über Startmenü oder Desktop-Icon starten (keine schwarze Konsole).
2. Gleiche Region wie in der Handy-App.
3. QR erzeugen → in Smart Life / Tuya Smart bestätigen. QR-Box ist fest **320×320** (scanbar; kein dünner Schlitz).
4. Einmal **Verbindung verweigert**? Eine Sekunde warten und erneut QR erzeugen — die UI startet die lokale API selbst.
5. `rtsp://<dieser-pc>:8554/<CameraName>/hd` in Frigate / Agent DVR / go2rtc kopieren.

Logins liegen in `%APPDATA%\TuyaRtspBridge\` — nie im Install-Ordner. Optionales Cloud-PTZ-Passwort als `cloud_auth.json` (mode 600).

## Was im Setup steckt

| Teil | Warum |
|---|---|
| Privates CPython 3.12 + tkinter + pip-Wheels | GUI und Login, kein System-Python |
| `tuya-ipc-terminal.exe` | RTSP-Engine (MIT, seydx) |
| Offizielles VideoLAN VLC 3 (64-bit) | In-App-Preview (`libvlc`) |
| ffmpeg essentials (GPL-3, Gyan) | Watchdog-Probe |

Lizenzen: `NOTICE.md`, `DEPENDENCIES.md`, plus `bin/FFMPEG-LICENSE.txt` und VLCs COPYING unter `vlc\`.

## SmartScreen

Setup ist nicht Authenticode-signiert. Windows kann „Windows hat den PC geschützt“ sagen. **Weitere Infos → Trotzdem ausführen**. Das ist die Unsigned-Open-Source-Steuer, kein Virus.

## Setup neu bauen

Braucht Inno Setup 6 und Netz (lädt Python/VLC/ffmpeg einmal, dann Cache).

```bat
python packaging\windows\build_bundle.py
```

Output: `installer\output\TuyaRtspBridge-Setup.exe`

Die Runtime wird nicht committed. Nur die Setup.exe gehört auf das GitHub-Release.

## Source-Checkout (Entwickler)

`launch.bat` legt bei fehlendem `runtime\` ein `.venv` an. Preview braucht dann System-VLC.
