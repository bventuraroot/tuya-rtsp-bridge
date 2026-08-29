# Instalador Windows

Doble clic **TuyaRtspBridge-Setup.exe** en [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases).

No instales Python/VLC/ffmpeg/Git. Runtime en `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## Después
1. Inicia la app.
2. Región = móvil.
3. Create QR (**320×320**).
4. Si hay connection refused: espera y reintenta.
5. `rtsp://<pc>:8554/<CameraName>/hd`.

Login: `%APPDATA%\TuyaRtspBridge\`. SmartScreen: **Más información → Ejecutar de todas formas**.

```bat
python packaging\windows\build_bundle.py
```
