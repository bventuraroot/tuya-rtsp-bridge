# Windows-installer (noob / foolproof)

Dubbelklik **TuyaRtspBridge-Setup.exe** van [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Volgende, Volgende, Voltooien.

Wizard volgt Windows-taal als Inno die heeft (EN/DE/NL/FR/ES/PT/IT/PL/CS/RU/UK/JA/KO/HE). ZH/HI/ID/YI in het app-menu na eerste start.

Je hoeft **geen** Python, VLC, ffmpeg of Git te installeren. Setup plaatst private runtime in `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## Na installatie
1. Start **Tuya RTSP Bridge** (Startmenu/desktop, geen console).
2. Zelfde regio als telefoon-app.
3. Create QR → bevestigen in Smart Life/Tuya Smart. QR-box vast **320×320**.
4. Eenmaal verbinding geweigerd? Even wachten en opnieuw — UI start API zelf.
5. `rtsp://<deze-pc>:8554/<CameraName>/hd` naar Frigate/Agent/go2rtc.

Logins in `%APPDATA%\TuyaRtspBridge\` — nooit in de installatiemap. Optioneel cloud-PTZ-wachtwoord: `cloud_auth.json` (mode 600).

## Inhoud Setup
| Onderdeel | Waarom |
|---|---|
| Private CPython 3.12 + tkinter + wheels | GUI/login zonder systeem-Python |
| `tuya-ipc-terminal.exe` | RTSP-engine (MIT, seydx) |
| VideoLAN VLC 3 64-bit | In-app preview |
| ffmpeg essentials (GPL-3) | Watchdog |

## SmartScreen
Niet Authenticode-gesigneerd. **Meer info → Toch uitvoeren**. Unsigned-OSS-belasting, geen virus.

## Setup herbouwen
```bat
python packaging\windows\build_bundle.py
```
Output: `installer\output\TuyaRtspBridge-Setup.exe`
