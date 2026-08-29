# Local HTTP API (`http://127.0.0.1:8787`)

JSON in/out. No auth — bind is local plus LAN; do not expose `:8787` to the internet.

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/state` | Login, cameras, RTSP URLs, flags, `lanIp` |
| GET | `/api/qr.png` | Current QR image (fixed **320×320** PNG) |
| POST | `/api/qr/start` | `{ "region": "eu" }` start QR |
| POST | `/api/logout` | Drop session |
| POST | `/api/cameras/refresh` | Re-list devices; restarts RTSP engine so WebRTC picks a fresh session |
| POST | `/api/cloud/auth` | `{ "email"?, "password", "countryCode"? }` — store reverse-app credentials for cloud PTZ (local file only, mode 600) |
| POST | `/api/flags` | `{ "rtsp": true, "watchdog": true, "hls": false, "archive": false }` |
| POST | `/api/lang` | `{ "lang": "en" \| "de" \| … }` |
| POST | `/api/rtsp/start` `/api/rtsp/stop` | Engine |
| POST | `/api/restart/rtsp` `/ui` `/all` | Restarts |
| POST | `/api/ptz/move` | `{ "deviceId", "direction": "up\|down\|left\|right\|stop" }` — LAN first, cloud fallback when credentials exist |
| POST | `/api/hd-proxy/start` | Optional HLS (heavy) |
| GET | `/api/frigate.yaml` | Generated snippet |

Static UI: `GET /` from `web/`.

Protect session cookies expire; with `cloud_auth.json` the server can password-relogin without another QR scan.
