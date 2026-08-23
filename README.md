# Tuya RTSP Bridge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Windows](https://img.shields.io/badge/Windows-10%2F11-blue.svg)](#install)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md)

**Turn any Tuya / Smart Life / iSmartLife camera into a normal RTSP camera** — so Frigate, Agent DVR, go2rtc, Home Assistant, or VLC can use it.

No firmware flash. No ONVIF (stock Tuya does not offer it). Scan a QR code once, then copy an RTSP URL.

| You are… | Start here |
|---|---|
| Just want it to work | [5-minute setup](#5-minute-setup) |
| Home-lab / NVR tinkerer | [docs/nvr.md](docs/nvr.md) |
| Developer | [docs/architecture.md](docs/architecture.md) · [CONTRIBUTING.md](CONTRIBUTING.md) |

This repository ships **no** accounts, device IDs, or home IPs.

---

## What you get

```
Phone (Smart Life) ──QR──► this PC ──RTSP :8554──► Frigate / Agent DVR / VLC
                              │
                              └── LAN PTZ (port 6668) when the camera allows it
```

- HD: `rtsp://<this-pc>:8554/<CameraName>/hd` (usually HEVC 1080p)
- SD: `rtsp://<this-pc>:8554/<CameraName>/sd` (H.264, smaller)
- All cameras share **one** bridge IP; only the path changes
- Live preview if [VLC](https://www.videolan.org/) is installed
- English or Deutsch (installer + app)

Signaling still uses Tuya cloud. When you watch from this PC, video typically stays on your LAN.

## Honest limits

- Stock firmware has **no ONVIF** and **no camera-native RTSP**
- Many models output about **10 fps** in the HD bitstream — that is the camera, not this app
- VLC 3 sometimes shows a black window on HEVC/RTSP; Agent DVR / Frigate are the intended viewers
- Preview needs VLC; recording should happen in your NVR, not on the bridge

Supported login regions: Western Europe, Eastern Europe, USA West, USA East, China, India.

---

## 5-minute setup

### 0. You need

1. Windows 10/11 64-bit
2. [Python 3.10+](https://www.python.org/downloads/) — tick **Add python.exe to PATH**
3. A Tuya Smart or Smart Life account that already sees the cameras
4. Optional: [VLC](https://www.videolan.org/) for the in-app preview

### 1. Install

- **Easy:** download `TuyaRtspBridge-Setup.exe` from [Releases](../../releases), pick English or Deutsch
- **From source:** see [Install from source](#install-from-source)

The app lives in `%LOCALAPPDATA%\Programs\TuyaRtspBridge`. Logins live in `%APPDATA%\TuyaRtspBridge\` (never in git).

### 2. Log in

1. Start **Tuya RTSP Bridge**
2. Pick the same region as in the phone app (Germany “Western Europe” → **EU**)
3. Click **Create QR**
4. In Smart Life / Tuya Smart: scan, then **confirm**
5. Cameras appear with copy-paste HD URLs

If the QR “does nothing”, wait — the app polls until you confirm. Wrong region = empty camera list; try the other EU/US cluster.

### 3. Watch

Paste into Agent DVR / Frigate / go2rtc:

```
rtsp://127.0.0.1:8554/<CameraName>/hd
```

From another machine on the LAN, replace `127.0.0.1` with this PC’s IP. Prefer **RTP over TCP**.

Ready-made snippets: [docs/nvr.md](docs/nvr.md).

---

## Install from source

```bat
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
cd vendor\tuya-ipc-terminal
go build -o ..\..\bin\tuya-ipc-terminal.exe .
cd ..\..
launch.bat
```

Need Go only to build the engine. Release builds already include `bin/tuya-ipc-terminal.exe`.

## Docs

| Doc | Audience |
|---|---|
| [docs/getting-started.md](docs/getting-started.md) | First run, Wi‑Fi move, PTZ |
| [docs/faq.md](docs/faq.md) | Black VLC, empty list, “only 10 fps” |
| [docs/nvr.md](docs/nvr.md) | Frigate, Agent DVR, go2rtc |
| [docs/architecture.md](docs/architecture.md) | How the pieces fit |
| [docs/api.md](docs/api.md) | Local HTTP API `:8787` |
| [DEPENDENCIES.md](DEPENDENCIES.md) | Licenses (all redistributable or not shipped) |
| [SECURITY.md](SECURITY.md) | What not to commit |

## License

MIT. RTSP engine by [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT), vendored with attribution.

Tuya, Smart Life, and iSmartLife are trademarks of their owners. This project is not affiliated with Tuya Inc.
