# Lokální HTTP API (`http://127.0.0.1:8787`)

JSON dovnitř/ven. Bez auth — bind lokálně + LAN; `:8787` nevystavujte na internet.

| Metoda | Cesta | Účel |
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

Statické UI: `GET /` z `web/`. S `cloud_auth.json` server umí password-relogin bez nového QR.
