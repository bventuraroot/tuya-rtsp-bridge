# Windows installer (noob / foolproof)

Double-click **TuyaRtspBridge-Setup.exe** from [Releases](../../releases). Next, Next, Finish.

You do **not** need to install Python, VLC, ffmpeg, or Git. The Setup copies a private runtime into `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## After install

1. Start **Tuya RTSP Bridge** from the Start menu or desktop icon (no black console).
2. Pick the same region as the phone app.
3. Create QR → confirm in Smart Life / Tuya Smart.
4. Copy `rtsp://<this-pc>:8554/<CameraName>/hd` into Frigate / Agent DVR / go2rtc.

Logins stay in `%APPDATA%\TuyaRtspBridge\` — never inside the install folder.

## What is inside the Setup

| Piece | Why |
|---|---|
| Private CPython 3.12 + tkinter + pip wheels | GUI and login, no system Python |
| `tuya-ipc-terminal.exe` | RTSP engine (MIT, seydx) |
| Official VideoLAN VLC 3 (64-bit) | In-app preview (`libvlc`) |
| ffmpeg essentials (LGPL, Gyan) | Watchdog probe |

Licenses: `NOTICE.md`, `DEPENDENCIES.md`, plus `bin/FFMPEG-LICENSE.txt` and VLC's own COPYING inside `vlc\`.

## SmartScreen

The Setup is not Authenticode-signed. Windows may say “Windows protected your PC”. **More info → Run anyway**. That is the unsigned-open-source tax, not a virus.

## Rebuild the Setup

Needs Inno Setup 6 and a network connection (downloads Python / VLC / ffmpeg once, then caches them).

```bat
python packaging\windows\build_bundle.py
```

Output: `installer\output\TuyaRtspBridge-Setup.exe`

The script does not commit the runtime. Only the Setup.exe belongs on the GitHub Release.

## Source checkout (developers)

`launch.bat` still creates a `.venv` if `runtime\` is missing. Preview then needs a system VLC.
