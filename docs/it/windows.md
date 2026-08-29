# Installer Windows

Doppio clic **TuyaRtspBridge-Setup.exe** da [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases).

Niente Python/VLC/ffmpeg/Git separati. Runtime: `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

1. Avvia app.
2. Regione = telefono.
3. Create QR (**320×320**).
4. Connection refused una volta → attendi e riprova.
5. `rtsp://<pc>:8554/<CameraName>/hd`.

Login: `%APPDATA%\TuyaRtspBridge\`. SmartScreen: Altre info → Esegui comunque.

```bat
python packaging\windows\build_bundle.py
```
