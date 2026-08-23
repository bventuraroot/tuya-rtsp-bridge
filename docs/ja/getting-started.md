# はじめ方

**Tuya Smart**、**Smart Life**、**iSmartLife** に出るカメラなら動く。箱のブランド（LSC、Nous、BlitzWolf、無名の「Tuya」）は問わない。スマホのアプリがどれかならよい。

1. Windows: Releasesの `TuyaRtspBridge-Setup.exe`（Python/VLC/ffmpeg込み）。Linux: `./launch.sh`。
2. **Tuya RTSP ブリッジ** を起動する。
3. スマホアプリと同じ地域を選ぶ。
4. QRを作る → 読む → スマホで **確認**。
5. HDのURLをNVRに貼る。

セッションは再起動後も残る（`%APPDATA%\TuyaRtspBridge`）。Tuyaが蹴るまで、もう一度読む必要はない。

引っ越し: アカウントからカメラを消さず、初期化もしなければ機器IDは同じ。新しいSSIDは現地のアプリで。NVRではPCのIPだけ変える。パスはそのまま。

PTZ: 矢印を押している間だけ動く。離すと止まる。クラウドではなくLANのTCP 6668。全機種があるわけではない。
