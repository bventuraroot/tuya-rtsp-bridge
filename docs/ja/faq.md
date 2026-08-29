# よくある質問

### ログイン後カメラ一覧が空
リージョン違い。ドイツ語アプリの「西ヨーロッパ」は **EU**（WEではない）。

### QRが終わらない
ウィンドウを開いたままスマホで**確認**。

### QRが極小／スリット／読めない (Windows)
**1.2.4+** で修正：固定 **320×320** キャンバス（NEAREST）。アプリを更新。「No QR」は Create QR 前は正常。

### 接続拒否 (WinError 10061)
UI が API (`:8787`) を自動起動。Create QR を再試行。

### VLC が黒い
VLC 3 は HEVC/RTSP で失敗しがち。ストリームは生きている。Agent/Frigate。Linux は ffmpeg MJPEG。

### 60 fps が欲しい
多くの機種は HD で約 **10 fps**。

### ONVIF？
いいえ。RTSP のみ。

### 映像は家の外へ？
シグナリングは Tuya。ローカルでは通常カメラ→この PC。

### LAN 外の Cloud PTZ？
先に LAN PTZ (TCP **6668**)。遠隔は email+password を一度 (`POST /api/cloud/auth`) — IoT developer キー不要。

### Home Assistant アドオン？
あり — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/)。ホストネット。Docker: [docker.md](../docker.md)。

### Linux / macOS？
`./launch.sh`。Arch: [arch-linux.md](../arch-linux.md)。データ: `~/.local/share/tuya-rtsp-bridge/`。
