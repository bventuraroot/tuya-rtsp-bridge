# はじめに

**Tuya Smart** / **Smart Life** / **iSmartLife** に出るカメラ。

## 初回
1. Windows: Releases の Setup。Linux: `./launch.sh` / Arch。Docker/HA: [docker.md](../docker.md)。
2. **Tuya RTSP Bridge** を起動（または `http://<host>:8787`）。
3. スマホと同じリージョン。
4. Create QR → スキャン → **確認**。QR は **320×320**。
5. HD URL を NVR に。

## PTZ
UI の矢印。**LAN:** TCP **6668**。**遠隔:** email+password を一度 (`POST /api/cloud/auth`) — IoT キー不要。

## プレビュー
Windows Setup = VLC。Linux = ffmpeg MJPEG。RTSP には不要。
