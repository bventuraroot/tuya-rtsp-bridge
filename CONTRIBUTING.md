# Contributing

Thank you. Every cheap Tuya camera that gets a real RTSP URL is a win — PRs, camera reports, and translations all count.

## First time here?

Good first contributions:

- Add or fix a language in `src/i18n.py` (keys must match `en`)
- Confirm a **camera model** + phone app works (open a [camera issue](../../issues/new?template=camera.yml))
- Improve docs in `docs/nl`, `docs/fr`, `docs/es`, `docs/pt`, `docs/it`, `docs/pl`, `docs/cs`, `docs/ru`, `docs/uk`, `docs/id`, `docs/zh`, `docs/hi`, `docs/ja`, `docs/ko`, `docs/he`, `docs/yi`, or English
- Linux packaging, Docker, macOS notes, Home Assistant examples

Open an issue before large refactors.

## Rules

1. Do **not** commit `%APPDATA%\\TuyaRtspBridge`, cookies, `localKey`, device IDs, or LAN IPs.
2. UI strings live in `src/i18n.py`. All listed languages must keep the same keys.
3. Engine source is `vendor/tuya-ipc-terminal` (MIT, seydx). Prefer upstream for generic engine fixes.
4. Say which **camera model** and **app** (Smart Life vs Tuya Smart) you tested.
5. No exploit write-ups against Tuya cloud.

## Dev setup

Windows:

```bat
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
cd vendor\tuya-ipc-terminal
go build -o ..\..\bin\tuya-ipc-terminal.exe .
cd ..\..
launch.bat
```

Foolproof Setup.exe (bundles CPython + VLC + ffmpeg + engine):

```bat
python packaging\windows\build_bundle.py
```

Output: `installer\output\TuyaRtspBridge-Setup.exe`. See [docs/windows.md](docs/windows.md).

Linux / Arch: `./launch.sh` (see [docs/arch-linux.md](docs/arch-linux.md)).

## Checks

```bash
python -m py_compile src/*.py
python tests/test_i18n.py
python tests/test_paths.py
```

CI runs the same on every PR.

## Code of conduct

Be decent. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
