# Lokalne API HTTP (`http://127.0.0.1:8787`)

JSON we/wy. Bez auth — bind lokalny + LAN; nie wystawiaj `:8787` do Internetu.

| Metoda | Ścieżka | Cel |
|---|---|---|
| GET | `/api/state` | Login, cameras, RTSP URLs, flags, `lanIp` |
| GET | `/api/qr.png` | QR PNG fixed **320×320** |
| POST | `/api/qr/start` | `{ "region": "eu" }` |
| POST | `/api/logout` | Drop session |
| POST | `/api/cameras/refresh` | Re-list + restart RTSP engine |
| POST | `/api/cloud/auth` | `{ "email"?, "password", "countryCode"? }` cloud PTZ (local, mode 600) |
| POST | `/api/flags` | flags |
| POST | `/api/lang` | language |
| POST | `/api/rtsp/start` `/stop` | Engine |
| POST | `/api/restart/rtsp` `/ui` `/all` | Restarts |
| POST | `/api/ptz/move` | LAN first, cloud fallback |
| POST | `/api/hd-proxy/start` | Optional HLS |
| GET | `/api/frigate.yaml` | Snippet |

Statyczne UI: `GET /` z `web/`. Z `cloud_auth.json` serwer robi password-relogin bez nowego QR.
