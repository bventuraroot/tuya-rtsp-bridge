# NVR / Home Assistant

Remplacez `BRIDGE_IP` et `CameraName` (espaces → `_`). Préférez **`/hd`**.

## Agent DVR
```
rtsp://BRIDGE_IP:8554/CameraName/hd
```
TCP. Pas de 2ᵉ intégration Tuya.

## Frigate
```yaml
cameras:
  front_yard:
    ffmpeg:
      inputs:
        - path: rtsp://BRIDGE_IP:8554/CameraName/hd
          input_args: preset-rtsp-restream
          roles: [record, detect]
    detect: { width: 1920, height: 1080, fps: 5 }
```

## go2rtc
```yaml
streams:
  cam1: rtsp://BRIDGE_IP:8554/CameraName/hd
```

## Home Assistant
Caméra générique / go2rtc. Docker : [docker.md](docker.md). Add-on : [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/).

## VLC debug
```
vlc --rtsp-tcp rtsp://127.0.0.1:8554/CameraName/hd
```
