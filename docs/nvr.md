# NVR / Home Assistant

Replace `BRIDGE_IP` with the PC that runs this app (`127.0.0.1` if the NVR is on the same machine). Replace `CameraName` with the name shown in the UI (spaces become `_`).

Always use the **`/hd`** path unless you have a reason for `/sd`.

## Agent DVR

Add camera → RTSP:

```
rtsp://BRIDGE_IP:8554/CameraName/hd
```

Transport: TCP. Do not enable a second Tuya integration on the same cameras (it steals the WebRTC session).

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

Detect fps can stay at 5 even if the source is ~10. Record uses the same HD URL.

See also `examples/frigate.yml`.

## go2rtc

```yaml
streams:
  cam1: rtsp://BRIDGE_IP:8554/CameraName/hd
```

Do **not** mix `tuya://` (password login) with this QR bridge on the same device.

## Home Assistant

Generic camera or go2rtc add-on with the same RTSP URL. Still no ONVIF.

## VLC (debug only)

```
vlc --rtsp-tcp rtsp://127.0.0.1:8554/CameraName/hd
```

If the window is black, try ffplay or Agent — not another Tuya app.
