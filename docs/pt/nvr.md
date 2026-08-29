# NVR / Home Assistant

Substitua `BRIDGE_IP` y `CameraName`. Use **`/hd`**.

## Agent DVR
```
rtsp://BRIDGE_IP:8554/CameraName/hd
```

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
Câmara genérica / go2rtc. [docker.md](docker.md).

## VLC
```
vlc --rtsp-tcp rtsp://127.0.0.1:8554/CameraName/hd
```
