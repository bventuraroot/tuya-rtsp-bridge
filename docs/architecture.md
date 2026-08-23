# Architecture

```
┌─────────────┐   HTTPS QR/session    ┌──────────────────┐
│ Smart Life  │ ◄──────────────────► │ Tuya / iSmartLife│
└─────────────┘                       └────────┬─────────┘
                                               │ MQTT + WebRTC signaling
┌─────────────┐   HTTP :8787                   │
│ Desktop GUI │ ◄────────────┐                 │
│ web/index   │              │                 ▼
└─────────────┘       ┌──────┴──────┐   ┌──────────────────┐
                      │ server.py   │   │ tuya-ipc-terminal│
                      │ flags, PTZ  │──►│ RTSP :8554       │
                      └──────┬──────┘   └────────┬─────────┘
                             │                   │ media (often LAN UDP)
                      tinytuya :6668             ▼
                             │            Frigate / Agent / VLC
                             ▼
                         Camera PTZ
```

| Piece | Path | Job |
|---|---|---|
| GUI | `src/gui.py` | Desktop UI, language, preview HWND |
| API | `src/server.py` | QR login, cameras, restarts, `:8787` |
| Login | `src/tuya_client.py` | iSmartLife web API |
| Engine | `vendor/tuya-ipc-terminal` | WebRTC → RTSP (MIT, seydx) |
| PTZ | `src/local_ptz.py` | TCP 6668, DP 119/116 |
| Preview | `src/preview.py` | VLC embed, no transcode |
| Watchdog | `src/rtsp_watchdog.py` | Restart engine if HD goes silent |

User data (`%APPDATA%\TuyaRtspBridge`) is separate from the install dir so upgrades do not wipe logins.

## Why not ONVIF / camera RTSP?

Measured on common Tuya IPC: only port **6668** is open locally. Video is WebRTC after cloud signaling. This project does not flash firmware.

## Why one engine?

A second `tuya-ipc-terminal` (or a phone on LTE plus the PC) can steal the WebRTC session. One engine, many RTSP clients.
