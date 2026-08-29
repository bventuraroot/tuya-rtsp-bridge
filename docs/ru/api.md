# Локальный HTTP API (`http://127.0.0.1:8787`)

JSON in/out. Без auth — bind локально + LAN; не открывайте `:8787` в интернет.

| Метод | Путь | Назначение |
|---|---|---|
| GET | `/api/state` | Login, cameras, RTSP URLs, flags, `lanIp` |
| GET | `/api/qr.png` | QR PNG **320×320** |
| POST | `/api/qr/start` | `{ "region": "eu" }` |
| POST | `/api/logout` | Drop session |
| POST | `/api/cameras/refresh` | Re-list + RTSP engine restart |
| POST | `/api/cloud/auth` | cloud PTZ creds (local mode 600) |
| POST | `/api/flags` | flags |
| POST | `/api/lang` | language |
| POST | `/api/rtsp/start` `/stop` | Engine |
| POST | `/api/restart/rtsp` `/ui` `/all` | Restarts |
| POST | `/api/ptz/move` | LAN first, cloud fallback |
| POST | `/api/hd-proxy/start` | Optional HLS |
| GET | `/api/frigate.yaml` | Snippet |

Статический UI: `GET /` из `web/`. С `cloud_auth.json` возможен password-relogin без нового QR.
