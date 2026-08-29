# NVR / Home Assistant

Vervang `BRIDGE_IP` door de pc met deze app (`127.0.0.1` als NVR lokaal is). `CameraName` = UI-naam (spaties → `_`). Gebruik **`/hd`** tenzij je `/sd` wilt.

## Agent DVR
```
rtsp://BRIDGE_IP:8554/CameraName/hd
```
Transport: TCP. Geen tweede Tuya-integratie op dezelfde camera’s.

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
Zie `examples/frigate.yml`.

## go2rtc
```yaml
streams:
  cam1: rtsp://BRIDGE_IP:8554/CameraName/hd
```
Meng `tuya://` niet met deze QR-bridge op hetzelfde device.

## Home Assistant
Generic camera of go2rtc met dezelfde RTSP-URL. Nog steeds geen ONVIF. Docker/add-on: [docker.md](docker.md).

## VLC (debug)
```
vlc --rtsp-tcp rtsp://127.0.0.1:8554/CameraName/hd
```
