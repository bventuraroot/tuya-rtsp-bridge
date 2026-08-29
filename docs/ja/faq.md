# よくある質問

### ログイン後カメラ一覧が空
リージョン違い。ドイツ語アプリの「西ヨーロッパ」は **EU**（WEではない）。

### QRが終わらない
ウィンドウを開いたままスマホで**確認**。

### QRが極小／スリット（Windows）
**1.2.4+** 修正：固定 **320×320** キャンバス（NEAREST）。Setup を更新。

### WinError 10061
UI が API (`:8787`) を自動起動。Create QR を再試行。

### VLC が黒い
ストリームは生きている。Agent/Frigate。Linux は ffmpeg MJPEG。

### 60 fps？
多くの機種は HD で約 **10 fps**。

### ONVIF？
いいえ。RTSP のみ。

### 映像は家の外へ？
シグナリングは Tuya。ローカルでは通常カメラ→この PC。

### go2rtc `tuya://`？
Tuya Smart の email/password。Smart Life QR ではない。

### LAN 外の Cloud PTZ？
先に LAN TCP **6668**。遠隔は `POST /api/cloud/auth` → `cloud_auth.json` mode 600。IoT 開発者キー不要。

### ログインの保存場所
`%APPDATA%\TuyaRtspBridge\` または `~/.local/share/tuya-rtsp-bridge/`。

### HA アドオン？
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/)。[docker.md](docker.md)。

### Linux？
`./launch.sh` · [arch-linux.md](../arch-linux.md)。
