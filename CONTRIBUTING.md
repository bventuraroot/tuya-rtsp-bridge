# Contributing

Thanks for helping people get local RTSP out of Tuya cameras.

## Rules

1. Do **not** commit `%APPDATA%\TuyaRtspBridge`, cookies, `localKey`, device IDs, or LAN IPs.
2. English or German UI strings go in `src/i18n.py`.
3. The engine lives in `vendor/tuya-ipc-terminal` (upstream MIT — keep LICENSE).
4. Say which **camera model** and **phone app** (Smart Life vs Tuya Smart) you tested.
5. No exploit write-ups against Tuya cloud.

## Dev setup

```bat
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
cd vendor\tuya-ipc-terminal
go build -o ..\..\bin\tuya-ipc-terminal.exe .
```

Run `launch.bat`. PRs welcome for Linux/macOS, extra regions, and camera-specific notes.

## Code of conduct

Be decent. No harassment. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
