# Docker

Headless `:8787` + `:8554`. Sesiones en `./data` y `./config`.

```bash
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
docker compose up -d --build
```

Add-on HA OS: [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/) (`host_network: true`).

Docker Desktop:
```bash
docker compose -f docker-compose.ports.yml up -d --build
```

Frigate local: `127.0.0.1` — [nvr.md](nvr.md).
