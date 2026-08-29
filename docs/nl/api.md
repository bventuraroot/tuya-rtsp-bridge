# Lokale HTTP-API (`http://127.0.0.1:8787`)

JSON in/uit. Geen auth — bind lokaal + LAN; expose `:8787` **niet** op internet.

| Methode | Pad | Doel |
|---|---|---|
| GET | `/api/state` | Login, camera’s, RTSP-URL’s, flags, `lanIp` |
| GET | `/api/qr.png` | Huidige QR (**320×320** PNG) |
| POST | `/api/qr/start` | `{ "region": "eu" }` |
| POST | `/api/logout` | Sessie droppen |
| POST | `/api/cameras/refresh` | Herlisten + RTSP-engine herstart |
| POST | `/api/cloud/auth` | `{ "email"?, "password", "countryCode"? }` cloud-PTZ-creds (lokaal, mode 600) |
| POST | `/api/flags` | `{ "rtsp", "watchdog", "hls", "archive" }` |
| POST | `/api/lang` | `{ "lang": "nl" \| … }` |
| POST | `/api/rtsp/start` `/stop` | Engine |
| POST | `/api/restart/rtsp` `/ui` `/all` | Restarts |
| POST | `/api/ptz/move` | `{ "deviceId", "direction" }` — LAN first, cloud fallback |
| POST | `/api/hd-proxy/start` | Optioneel HLS |
| GET | `/api/frigate.yaml` | Snippet |

Statische UI: `GET /` uit `web/`. Met `cloud_auth.json` kan de server password-relogin zonder nieuwe QR.
