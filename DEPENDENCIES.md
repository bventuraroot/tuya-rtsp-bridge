# Third-party notices

This project is MIT-licensed. It vendors and depends on other free/open-source works:

## Vendored

| Component | License | Source |
|---|---|---|
| tuya-ipc-terminal | MIT | https://github.com/seydx/tuya-ipc-terminal |

See `NOTICE.md` (full legal text) and `vendor/tuya-ipc-terminal/LICENSE`.

## Python runtime dependencies (pip)

| Package | License | Use |
|---|---|---|
| requests | Apache-2.0 | HTTPS to Tuya / iSmartLife |
| qrcode | BSD-3-Clause | Login QR |
| pillow | HPND-like (PIL) | QR + images |
| tinytuya | MIT | Local PTZ (TCP 6668) |
| python-vlc | LGPL-2.1+ | Live preview HWND (does **not** ship VLC) |

## Required on the user's machine (not bundled)

| Software | License | Why not bundled |
|---|---|---|
| Python 3.10+ | PSF | Interpreter |
| VideoLAN VLC 3.x | LGPL-2.1+ | Hardware video preview. Install from https://www.videolan.org/ |
| ffmpeg (optional) | LGPL/GPL | Watchdog byte-probe only. Any LGPL build is enough. |

## Go engine transitive (MIT / BSD)

pion/webrtc, eclipse/paho.mqtt.golang, rs/zerolog, spf13/cobra, golang.org/x/* — all OSI-approved.

## Not included on purpose

- No Tuya/Smart Life credentials, cookies, or `localKey`
- No camera device IDs or LAN IPs
- No VLC or ffmpeg binaries (license / size)
- No telemetry
