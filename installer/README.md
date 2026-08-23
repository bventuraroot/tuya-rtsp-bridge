# Build the Windows installer

Needs [Inno Setup 6](https://jrsoftware.org/isinfo.php) (free for non-commercial use).

```bat
cd vendor\tuya-ipc-terminal
go build -o ..\..\bin\tuya-ipc-terminal.exe .
cd ..\..\installer
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" TuyaRtspBridge.iss
```

Output: `installer\output\TuyaRtspBridge-Setup.exe`

The wizard language (English / Deutsch) also writes `%APPDATA%\TuyaRtspBridge\config.json`.
