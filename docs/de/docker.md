# Docker

Headless: Web-UI `:8787` + RTSP `:8554`. Keine Desktop-GUI, kein VLC im Image.

Session-Dateien in `./data` und `./config` neben der Compose-Datei — nie im Image.

## Linux / Home-Assistant-Host (empfohlen)

Host-Networking lässt die Engine mit Kameras im LAN sprechen (WebRTC/UDP + PTZ TCP 6668).

```bash
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
docker compose up -d --build
```

`http://<dieser-host>:8787` öffnen → Region wie Handy → **QR erzeugen** → scannen und in Smart Life / Tuya Smart **bestätigen**.

Dann in Frigate / go2rtc / Agent DVR:

```
rtsp://<dieser-host>:8554/<CameraName>/hd
```

## Home-Assistant-OS-Add-on

Supervisor-Add-on: [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/).

1. Repo auf dem HA-Host clonen **oder** `https://github.com/DanEng1982/tuya-rtsp-bridge` (Unterordner `homeassistant`) als Custom-Add-on-Repo via `repository.json`
2. ggf. **Einstellungen → Add-ons → Add-on-Store → ⋮ → Repositories**
3. **Tuya RTSP Bridge** installieren → Start
4. `http://<ha-host>:8787` für QR-Login

Details: [homeassistant/tuya_rtsp_bridge/README.md](../../homeassistant/tuya_rtsp_bridge/README.md).

`host_network: true` ist Pflicht. Dieselbe Kameras **nicht** parallel über die offizielle Tuya-Cloud-Integration fahren.

## Windows / macOS Docker Desktop

`network_mode: host` funktioniert dort nicht:

```bash
docker compose -f docker-compose.ports.yml up -d --build
```

Bei flackrigem PTZ/Video lieber native Windows-App statt Container.

## Frigate auf derselben Maschine

`127.0.0.1` als Bridge-IP (siehe [nvr.md](nvr.md) und `examples/frigate.yml`). Dieselben Kameras **nicht** zusätzlich mit offizieller Tuya- / `tuya://`-Integration — die stiehlt die Live-Session.

## Updates

```bash
git pull
docker compose up -d --build
```

Login-Session bleibt in `./data`.

## Was nicht im Image ist

- Desktop-GUI / python-vlc
- Dein Tuya-Account, Device-IDs oder LAN-IPs
