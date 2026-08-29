# Installateur Windows

Double-clic **TuyaRtspBridge-Setup.exe** depuis les [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Suivant ×3.

Pas besoin d’installer Python/VLC/ffmpeg/Git. Runtime dans `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## Après install
1. Démarrer l’app (menu Démarrer / bureau).
2. Région = téléphone.
3. Create QR — case **320×320**.
4. Si connexion refusée une fois : attendre et réessayer (l’UI démarre l’API).
5. `rtsp://<pc>:8554/<CameraName>/hd` vers Frigate/Agent.

Logins : `%APPDATA%\TuyaRtspBridge\` (`cloud_auth.json` optionnel, mode 600).

## Contenu
CPython 3.12 privé, `tuya-ipc-terminal.exe`, VLC 3, ffmpeg essentials.

## SmartScreen
Non signé Authenticode → **Plus d’infos → Exécuter quand même**.

## Rebuild
```bat
python packaging\windows\build_bundle.py
```
