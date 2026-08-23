# Tuya RTSP Bridge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Local QR login for Tuya / Smart Life / iSmartLife cameras → **RTSP** for Frigate, Agent DVR, go2rtc, VLC.

Languages: **English** and **Deutsch** (pick in the installer and in the app).

This repository contains **no** personal accounts, device IDs, or LAN addresses.

## What it does

- Scan a QR code in Tuya Smart / Smart Life (any region: EU, US, …)
- Discovers cameras in that account
- Serves `rtsp://<this-pc>:8554/<CameraName>/hd` (HEVC) and `/sd` (H.264)
- Optional LAN PTZ (Tuya protocol, port 6668)
- Optional live preview via VLC (must be installed separately)
- Optional watchdog that restarts a dead engine

Video bits stay on your LAN when you watch from this PC. Signaling still uses Tuya cloud. There is **no ONVIF** on stock Tuya firmware.

## Requirements

| Need | License |
|---|---|
| Windows 10/11 x64 | — |
| Python 3.10+ | PSF |
| [VLC](https://www.videolan.org/) (preview) | LGPL-2.1 |
| ffmpeg on PATH (optional watchdog) | LGPL/GPL |

See [DEPENDENCIES.md](DEPENDENCIES.md). Everything we ship is OSI-approved or not redistributed.

## Install from source

```bat
git clone https://github.com/YOURUSER/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

Build the engine (or use a release `bin/tuya-ipc-terminal.exe`):

```bat
cd vendor\tuya-ipc-terminal
go build -o ..\..\bin\tuya-ipc-terminal.exe .
```

Start:

```bat
launch.bat
```

Data (sessions, flags) goes to `%APPDATA%\TuyaRtspBridge\` — never into git.

## Installer

`installer\TuyaRtspBridge-Setup.exe` — choose English or German, installs under `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## RTSP URLs

After login:

```
rtsp://127.0.0.1:8554/<CameraName>/hd
rtsp://<LAN-IP>:8554/<CameraName>/hd
```

Use RTP over TCP in picky clients. Agent DVR / Frigate: the `/hd` URL.

## License

MIT. Engine by [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT), vendored with attribution.

Tuya, Smart Life, and iSmartLife are trademarks of their owners. This project is not affiliated with Tuya Inc.
