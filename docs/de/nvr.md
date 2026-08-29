# NVR / Home Assistant

`BRIDGE_IP` durch den PC ersetzen, auf dem diese App läuft (`127.0.0.1`, wenn NVR auf derselben Maschine). `CameraName` = Name in der UI (Leerzeichen → `_`).

Immer **`/hd`**, außer du brauchst bewusst `/sd`.

## Agent DVR

Kamera hinzufügen → RTSP:

```
rtsp://BRIDGE_IP:8554/CameraName/hd
```

Transport: TCP. Keine zweite Tuya-Integration auf denselben Kameras (stiehlt WebRTC-Session).

## Frigate

```yaml
mqtt:
  enabled: false

cameras:
  front_yard:
    ffmpeg:
      inputs:
        - path: rtsp://BRIDGE_IP:8554/CameraName/hd
          input_args: preset-rtsp-restream
          roles: [record, detect]
    detect:
      width: 1920
      height: 1080
      fps: 5
```

Detect-fps kann 5 bleiben, auch wenn die Quelle ~10 ist. Record nutzt dieselbe HD-URL.

Siehe auch `examples/frigate.yml`.

## go2rtc

```yaml
streams:
  cam1: rtsp://BRIDGE_IP:8554/CameraName/hd
```

`tuya://` (Passwort-Login) **nicht** mit dieser QR-Bridge auf demselben Gerät mischen.

## Home Assistant

Generic Camera oder go2rtc-Add-on mit derselben RTSP-URL. Immer noch kein ONVIF.

Auf dem HA-Host (Linux) kann die Bridge neben Frigate laufen:

```bash
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
docker compose up -d --build
```

Dann `http://<ha-host>:8787`, QR scannen, Frigate auf `rtsp://127.0.0.1:8554/<CameraName>/hd`. Details: [docker.md](docker.md). Supervisor-Add-on: [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/).

## VLC (nur Debug)

```
vlc --rtsp-tcp rtsp://127.0.0.1:8554/CameraName/hd
```

Fenster schwarz? ffplay oder Agent — nicht noch eine Tuya-App.
