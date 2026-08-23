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
| python-vlc | LGPL-2.1+ | Live preview HWND |

## Windows Setup.exe (v1.2+) redistributes

These sit next to the app. You can replace them with any compatible official build.

| Software | License | Notes |
|---|---|---|
| CPython 3.12 | PSF | Private copy under `runtime\` |
| VideoLAN VLC 3 (64-bit) | LGPL-2.1+ | Official zip; `vlc\COPYING` |
| ffmpeg essentials (Gyan) | LGPL | `bin\ffmpeg.exe` + `bin\FFMPEG-LICENSE.txt` |

Linux / source installs still use distro Python, VLC, and ffmpeg.

## Go engine transitive (MIT / BSD)

pion/webrtc, eclipse/paho.mqtt.golang, rs/zerolog, spf13/cobra, golang.org/x/* — all OSI-approved.

## Not included on purpose

- No Tuya/Smart Life credentials, cookies, or `localKey`
- No camera device IDs or LAN IPs
- No telemetry
