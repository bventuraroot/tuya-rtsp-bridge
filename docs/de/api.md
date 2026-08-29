# Lokale HTTP-API (`http://127.0.0.1:8787`)

JSON rein/raus. Kein Auth — Bind lokal plus LAN; `:8787` **nicht** ins Internet exposen.

| Methode | Pfad | Zweck |
|---|---|---|
| GET | `/api/state` | Login, Kameras, RTSP-URLs, Flags, `lanIp` |
| GET | `/api/qr.png` | Aktuelles QR-Bild (festes **320×320**-PNG) |
| POST | `/api/qr/start` | `{ "region": "eu" }` QR starten |
| POST | `/api/logout` | Session droppen |
| POST | `/api/cameras/refresh` | Geräte neu listen; RTSP-Engine neu, frische WebRTC-Session |
| POST | `/api/cloud/auth` | `{ "email"?, "password", "countryCode"? }` — reverse-App-Creds für Cloud-PTZ (nur lokal, mode 600) |
| POST | `/api/flags` | `{ "rtsp": true, "watchdog": true, "hls": false, "archive": false }` |
| POST | `/api/lang` | `{ "lang": "en" \| "de" \| … }` |
| POST | `/api/rtsp/start` `/api/rtsp/stop` | Engine |
| POST | `/api/restart/rtsp` `/ui` `/all` | Restarts |
| POST | `/api/ptz/move` | `{ "deviceId", "direction": "up\|down\|left\|right\|stop" }` — LAN first, Cloud-Fallback bei Creds |
| POST | `/api/hd-proxy/start` | Optionales HLS (schwer) |
| GET | `/api/frigate.yaml` | Generiertes Snippet |

Statische UI: `GET /` aus `web/`.

Protect-Session-Cookies laufen ab; mit `cloud_auth.json` kann der Server per Passwort reloggen ohne neuen QR-Scan.
