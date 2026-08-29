# Docker

Headless : UI `:8787` + RTSP `:8554`. Pas de GUI desktop / VLC dans l’image. Sessions dans `./data` + `./config`.

## Linux / hôte HA (recommandé)
```bash
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
docker compose up -d --build
```
`http://<host>:8787` → QR → `rtsp://<host>:8554/<CameraName>/hd`

## Add-on Home Assistant OS
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). `host_network: true` obligatoire.

## Docker Desktop Win/mac
```bash
docker compose -f docker-compose.ports.yml up -d --build
```

## Frigate même machine
`127.0.0.1` — [nvr.md](nvr.md). Pas d’intégration Tuya officielle en parallèle.
