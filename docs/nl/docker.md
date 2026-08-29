# Docker

Headless: web-UI `:8787` + RTSP `:8554`. Geen desktop-GUI, geen VLC in het image.

Sessies in `./data` en `./config` naast compose — nooit in het image.

## Linux / Home Assistant-host (aanbevolen)
Host-networking voor LAN (WebRTC/UDP + PTZ TCP 6668).

```bash
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
docker compose up -d --build
```

Open `http://<host>:8787` → regio = telefoon → **Create QR** → scannen en **bevestigen**.

```
rtsp://<host>:8554/<CameraName>/hd
```

## Home Assistant OS add-on
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). `host_network: true` verplicht. Geen parallelle officiële Tuya-cloud-integratie voor dezelfde camera’s.

## Windows / macOS Docker Desktop
`network_mode: host` werkt niet:
```bash
docker compose -f docker-compose.ports.yml up -d --build
```
Bij flaky PTZ/video: native Windows-app.

## Frigate op dezelfde machine
`127.0.0.1` als bridge-IP. Zie [nvr.md](nvr.md). Geen `tuya://` ernaast.

## Updates
```bash
git pull
docker compose up -d --build
```
