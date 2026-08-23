# FAQ

### The camera list is empty after login

Wrong region. “Western Europe” in the German app is **EU** (`protect-eu`), not WE. Try the other cluster in the same continent.

### The QR never finishes

Keep the window open and confirm in the phone. A pending poll (`result: true` without a user id) is normal.

### VLC is black / the preview is a slit

VLC 3 often fails on HEVC over RTSP. That does **not** mean the stream is dead. Use Agent DVR, Frigate, or ffplay. The desktop preview needs a current VLC install.

### I expected 60 fps

Many Tuya IPC models emit about **10 fps** in the HD HEVC stream. This bridge does not invent frames.

### Is this ONVIF?

No. Stock Tuya firmware does not speak ONVIF. This project is RTSP-only.

### Is video leaving my house?

Signaling (login, WebRTC handshake) goes to Tuya. When you view through this PC, the video medium is typically camera → this PC on the LAN. A phone on mobile data is a **second** viewer and uses the cloud path.

### Can I use go2rtc `tuya://` instead?

That needs a Tuya Smart **email/password**, not a Smart Life QR. Different login.

### HLS / VLC HTTP?

Optional and expensive (x264 transcode). Off by default. Agent/Frigate should use RTSP `/hd`.

### Where is my login stored?

`%APPDATA%\TuyaRtspBridge\` — cookies and camera list. Do not put that folder in git or in a screenshot.

### Linux / macOS?

The engine is Go and can be built elsewhere. The desktop GUI and installer are Windows-first. Help welcome.
