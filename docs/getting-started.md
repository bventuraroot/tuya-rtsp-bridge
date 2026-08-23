# Getting started

Works with cameras that show up in **Tuya Smart**, **Smart Life**, or **iSmartLife**. Brand names on the box (LSC, Nous, BlitzWolf, generic “Tuya”) are fine as long as the phone app is one of those.

## First run

1. Windows: `TuyaRtspBridge-Setup.exe` from Releases (Python/VLC/ffmpeg included). Linux: `./launch.sh`.
2. Start **Tuya RTSP Bridge**.
3. Choose the region that matches the phone app.
4. Create QR → scan → **confirm** in the phone.
5. Copy the HD URL into your NVR.

Sessions survive reboots (`%APPDATA%\TuyaRtspBridge`). Only scan again if Tuya kicks the session.

## Moving house / new Wi‑Fi

Device IDs stay the same if you **do not** delete the cameras from the account and **do not** factory-reset them.

1. At the new place, join the cameras to the new SSID from the phone (pairing / “change network”).
2. Start the bridge on a PC on that same LAN.
3. Point Agent/Frigate at the **new PC IP**; keep the path (`/CameraName/hd`).

Do not push a remote SSID from another city — the camera can hold only one network and will go offline.

## PTZ

Hold an arrow in the desktop UI = move. Release = stop.

This uses the local Tuya protocol on **TCP 6668**, not the cloud. The camera must be on the same LAN. Not every model exposes PTZ DPs.

## Preview

Install [VLC](https://www.videolan.org/). Fullscreen is a button; Esc goes back.

Preview is optional. RTSP for Frigate/Agent works without VLC.

## Autostart

Windows: shortcut to `launch-hidden.vbs` in the Startup folder. That starts the API/engine with no window. Use `launch.bat` when you want the desktop UI.
