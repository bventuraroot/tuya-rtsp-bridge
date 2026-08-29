# 로컬 HTTP API (`http://127.0.0.1:8787`)

JSON in/out. 인증 없음 — 로컬+LAN. `:8787`을 인터넷에 노출하지 마세요.

| 메서드 | 경로 | 목적 |
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

정적 UI: `web/`의 `GET /`. `cloud_auth.json`이 있으면 QR 없이 password-relogin 가능.
