# Docker

Headless: web UI `:8787` + RTSP `:8554`. No desktop GUI, no VLC inside the image.

Session files stay in `./data` and `./config` next to the compose file — never in the image.

## Linux / Home Assistant host (recommended)

Host networking lets the engine talk to cameras on the LAN (WebRTC/UDP + PTZ on TCP 6668).

```bash
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
docker compose up -d --build
```

Open `http://<this-host>:8787` → same region as the phone app → **Create QR** → scan and **confirm** in Smart Life / Tuya Smart.

Then in Frigate / go2rtc / Agent DVR:

```
rtsp://<this-host>:8554/<CameraName>/hd
```

## Windows / macOS Docker Desktop

`network_mode: host` does not work there:

```bash
docker compose -f docker-compose.ports.yml up -d --build
```

If PTZ or live video is flaky, run the native Windows app instead of the container.

## Frigate on the same machine

Use `127.0.0.1` as the bridge IP (see [nvr.md](nvr.md) and `examples/frigate.yml`). Do **not** also add the official Tuya / `tuya://` integration for the same cameras — it steals the live session.

## Updates

```bash
git pull
docker compose up -d --build
```

Login session survives in `./data`.

## What is not in the image

- Desktop GUI / python-vlc
- Your Tuya account, device IDs, or LAN IPs
