# Getting started

Works with cameras that show up in **Tuya Smart**, **Smart Life**, or **iSmartLife**. Brand names on the box (LSC, Nous, BlitzWolf, generic “Tuya”) are fine as long as the phone app is one of those.

## First run

1. Windows: `TuyaRtspBridge-Setup.exe` from Releases (Python/VLC/ffmpeg included). Linux: `./launch.sh` or the Arch package. Docker / HA OS: [docker.md](docker.md).
2. Start **Tuya RTSP Bridge** (or open `http://<host>:8787` for headless).
3. Choose the region that matches the phone app.
4. Create QR → scan → **confirm** in the phone. The QR is a fixed **320×320** square so phones can read it.
5. Copy the HD URL into your NVR.

Sessions survive reboots (`%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`). Only scan again if Tuya kicks the session — with a saved email/password the bridge can refresh the protect session automatically.

## Moving house / new Wi‑Fi

Device IDs stay the same if you **do not** delete the cameras from the account and **do not** factory-reset them.

1. At the new place, join the cameras to the new SSID from the phone (pairing / “change network”).
2. Start the bridge on a PC on that same LAN.
3. Point Agent/Frigate at the **new PC IP**; keep the path (`/CameraName/hd`).

Do not push a remote SSID from another city — the camera can hold only one network and will go offline.

## PTZ

Hold an arrow in the desktop UI = move. Release = stop.

- **On LAN:** local Tuya protocol on **TCP 6668** (same subnet as the cameras; VPN interfaces are skipped).
- **Off-site / no LAN path:** optional **cloud PTZ** via reverse Smart Life / Tuya app API after you store email+password once (`POST /api/cloud/auth`). No IoT Platform Access ID/Secret.

Not every model exposes PTZ data points.

## Preview

Windows Setup already includes VLC. On Linux the GUI uses an ffmpeg live MJPEG pipe (no X11 VLC embed). Fullscreen is a button; Esc goes back.

Preview is optional. RTSP for Frigate/Agent works without it.

## Autostart

Windows: shortcut to `launch-hidden.vbs` in the Startup folder. That starts the API/engine with no window. Use `launch.bat` when you want the desktop UI.

Linux (user systemd after Arch package): `systemctl --user enable --now tuya-rtsp-bridge.service tuya-rtsp-gui.service`.
