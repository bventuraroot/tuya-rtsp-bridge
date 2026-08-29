# Windows instalátor

Dvojklik **TuyaRtspBridge-Setup.exe** z [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases).

Bez samostatného Python/VLC/ffmpeg/Git. Runtime: `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

1. Spusťte app.
2. Region = telefon.
3. Create QR (**320×320**).
4. Connection refused jednou → počkejte, znovu.
5. `rtsp://<pc>:8554/<CameraName>/hd`.

Login: `%APPDATA%\TuyaRtspBridge\`. SmartScreen: Další informace → Přesto spustit.

```bat
python packaging\windows\build_bundle.py
```
