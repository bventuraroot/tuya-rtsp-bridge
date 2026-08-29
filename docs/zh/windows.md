# Windows 安装包

Double-click **TuyaRtspBridge-Setup.exe** from [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Next, Next, Finish.

No separate Python, VLC, ffmpeg, or Git. Private runtime → `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## After install
1. Start **Tuya RTSP Bridge** (Start menu / desktop).
2. Same region as the phone app.
3. Create QR — fixed **320×320** square.
4. If connection refused once: wait and retry (UI starts API `:8787`).
5. Copy `rtsp://<this-pc>:8554/<CameraName>/hd` into Frigate / Agent / go2rtc.

Logins: `%APPDATA%\TuyaRtspBridge\` (optional `cloud_auth.json` mode 600). Never in the install folder.

## Inside the Setup
Private CPython 3.12 + tkinter, `tuya-ipc-terminal.exe`, VLC 3, ffmpeg essentials.

## SmartScreen
Not Authenticode-signed → **More info → Run anyway**.

## Rebuild
```bat
python packaging\windows\build_bundle.py
```
Output: `installer\output\TuyaRtspBridge-Setup.exe`
