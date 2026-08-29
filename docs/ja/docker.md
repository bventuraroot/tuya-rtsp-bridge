# Docker

Headless: web UI `:8787` + RTSP `:8554`. Sessions in `./data` + `./config` (never in the image).

## Linux / HA host
```bash
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
docker compose up -d --build
```
Open `http://<host>:8787` → Create QR → `rtsp://<host>:8554/<CameraName>/hd`

## Home Assistant OS add-on
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/) — `host_network: true` required.

## Docker Desktop (Win/mac)
```bash
docker compose -f docker-compose.ports.yml up -d --build
```

## Frigate same machine
Use `127.0.0.1`. See [nvr.md](nvr.md). Do not also run official Tuya / `tuya://` on the same cameras.

## Updates
```bash
git pull && docker compose up -d --build
```
