# API HTTP local (`http://127.0.0.1:8787`)

JSON entrada/saída. Sem auth — bind local + LAN; não exponha `:8787` à Internet.

| Método | Caminho | Função |
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

UI estática: `GET /` de `web/`. Com `cloud_auth.json`, re-login por password sem novo QR.
