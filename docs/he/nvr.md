# NVR / Home Assistant

Replace `BRIDGE_IP` and `CameraName` (spaces → `_`). Prefer **`/hd`**.

## Agent DVR
```
rtsp://BRIDGE_IP:8554/CameraName/hd
```
Transport TCP. No second Tuya integration on the same cameras.

## Frigate
```yaml
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
See also `examples/frigate.yml`.

## go2rtc
```yaml
streams:
  cam1: rtsp://BRIDGE_IP:8554/CameraName/hd
```
Do not mix `tuya://` with this QR bridge on the same device.

## Home Assistant
Generic camera or go2rtc with the same RTSP URL. Docker/add-on: [docker.md](docker.md).

## VLC (debug)
```
vlc --rtsp-tcp rtsp://127.0.0.1:8554/CameraName/hd
```
