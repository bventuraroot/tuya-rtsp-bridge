# 本地 HTTP API（`http://127.0.0.1:8787`）

JSON 进出。无鉴权 — 绑定本机+局域网；不要把 `:8787` 暴露到公网。

| 方法 | 路径 | 用途 |
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

静态 UI：`GET /` 来自 `web/`。有 `cloud_auth.json` 时可密码重新登录而无需再扫 QR。
