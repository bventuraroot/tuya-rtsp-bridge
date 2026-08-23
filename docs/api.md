# Local HTTP API (`http://127.0.0.1:8787`)

JSON in/out. No auth — bind is local plus LAN; do not expose `:8787` to the internet.

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/state` | Login, cameras, RTSP URLs, flags, `lanIp` |
| POST | `/api/qr/start` | `{ "region": "eu" }` start QR |
| POST | `/api/logout` | Drop session |
| POST | `/api/cameras/refresh` | Re-list devices |
| POST | `/api/flags` | `{ "rtsp": true, "watchdog": true, "hls": false, "archive": false }` |
| POST | `/api/lang` | `{ "lang": "en" \| "de" }` |
| POST | `/api/rtsp/start` `/api/rtsp/stop` | Engine |
| POST | `/api/restart/rtsp` `/ui` `/all` | Restarts |
| POST | `/api/ptz/move` | `{ "deviceId", "direction": "up\|down\|left\|right\|stop" }` |
| POST | `/api/hd-proxy/start` | Optional HLS (heavy) |
| GET | `/api/frigate.yaml` | Generated snippet |

Static UI: `GET /` from `web/`.
