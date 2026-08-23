# Why this exists

Cheap Tuya / Smart Life / iSmartLife cameras are easy to buy and painful to *own*.

The box looks like a normal IP camera. In practice the manufacturer locked the useful bits behind their cloud:

- There is **no ONVIF** on stock firmware.
- There is **no camera-native RTSP** you can paste into Frigate, Agent DVR, go2rtc, or Home Assistant.
- The official app wants an account, a phone, and a path through servers you do not control.
- A second phone or a “cloud NVR” often means a subscription — or a second viewer that steals the live session.

You paid for a sensor on *your* wall. You should be able to record it on *your* disk.

**Tuya RTSP Bridge** is a small local program (Windows or Arch Linux) that turns those cameras into ordinary RTSP cameras. You scan a QR code once with the same app you already use. After that, every camera has a normal URL:

```
rtsp://<this-pc>:8554/<CameraName>/hd
```

Drop that into Frigate, Agent DVR, go2rtc, VLC, or Home Assistant. Motion, archive, and notifications stay in software *you* picked.

## What you gain

| Without this | With this |
|---|---|
| Cloud-only live view | Local RTSP, same LAN |
| App lock-in | Any NVR that speaks RTSP |
| No ONVIF | You do not need ONVIF |
| Extra cloud viewer = extra lag / lost session | One engine, many local clients |
| Recordings on someone else’s storage | Recordings on your NAS / Frigate / Agent |
| “It works until the vendor changes the app” | You keep the RTSP URL |

Signaling (login, handshake) still uses Tuya’s servers. When you watch from this PC, the **video** typically stays camera → your machine on the LAN. That is the point: cheap hardware, local archive.

## What this is not

- Not a firmware flash, not a jailbreak, not ONVIF.
- Not a promise of 60 fps — many of these cams emit about **10 fps** HD HEVC. That is the camera.
- Not a cloud killer for the phone app. The phone can stay. This is the *local* path for your NVR.
- Not affiliated with Tuya Inc. The RTSP engine is [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

## Who it is for

- **Anyone** who bought a “Smart Life” camera and then asked “where is the RTSP checkbox?”
- **Home-lab people** wiring Frigate / Agent DVR / Home Assistant.
- **Developers** who want a readable local API (`:8787`) and an MIT tree they can fork.

## How it looks

First run — pick language and region, create a QR, scan it in Smart Life, confirm:

![Welcome screen of Tuya RTSP Bridge. Empty camera list, no QR yet, only localhost.](images/ui-welcome.png)

After login — placeholder camera *names* only (no live picture, no real device IDs). You copy the HD URL into your NVR:

![Ready screen with two demo cameras, black preview panes, RTSP URLs on 127.0.0.1.](images/ui-ready.png)

Screenshots are taken from a demo session. They do not contain accounts, serials, or video.

Next: [getting-started.md](getting-started.md) · [FAQ](faq.md) · [NVR recipes](nvr.md)
