# לאָקאַל HTTP API (`http://127.0.0.1:8787`)

JSON. קיין auth — לאָקאַל+LAN. ניט expose `:8787` צום אינטערנעץ.

| מעטאָד | פּאַט | ציל |
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

סטאַטיש UI: `GET /` פֿון `web/`. מיט `cloud_auth.json` — password-relogin אָן נײַעם QR.
