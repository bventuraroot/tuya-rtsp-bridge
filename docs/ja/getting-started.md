# はじめに

**Tuya Smart** / **Smart Life** / **iSmartLife**。

## 初回
1. Windows Setup: [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases)。Linux: `./launch.sh`。Docker/HA: [docker.md](docker.md)。
2. **Tuya RTSP Bridge** または `http://<host>:8787`。
3. スマホと同じリージョン。
4. Create QR → スキャン → **確認**。QR は **320×320**。
5. HD URL を NVR へ。

セッション: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`。

## 引越し / 新しい Wi‑Fi
アカウントからカメラを削除しない。アプリで新 SSID、新 LAN で bridge、NVR は PC IP のみ変更。

## PTZ
UI 矢印。LAN **TCP 6668**。遠隔 cloud: `POST /api/cloud/auth`。

## プレビュー / 自動起動
Windows = VLC。Linux = ffmpeg MJPEG。`launch-hidden.vbs` / systemd user。
