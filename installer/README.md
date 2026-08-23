# Build the Windows installer

Needs [Inno Setup 6](https://jrsoftware.org/isinfo.php) and a network connection the first time.

```bat
python packaging\windows\build_bundle.py
```

That downloads (and caches) official CPython, VideoLAN VLC, and LGPL ffmpeg, copies `bin\tuya-ipc-terminal.exe`, then runs ISCC.

Output: `installer\output\TuyaRtspBridge-Setup.exe`

The wizard language also writes `%APPDATA%\TuyaRtspBridge\config.json`.

See [docs/windows.md](../docs/windows.md).
