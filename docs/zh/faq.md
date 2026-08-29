# 常见问题

### 登录后摄像头列表为空
区域选错。德文 App 的「西欧」是 **EU**（`protect-eu`），不是 WE。

### QR 一直不完成
保持窗口打开，并在手机上**确认**。

### QR 极小 / 一条缝（Windows）
**1.2.4+** 已修：固定 **320×320** 画布（NEAREST）。请更新 Setup。点 Create QR 前显示 «No QR» 正常。

### 连接被拒绝（WinError 10061）
界面会自动拉起 API（`:8787`）。再点一次 Create QR。

### VLC 黑屏
流其实还在。用 Agent/Frigate。Linux 用 ffmpeg MJPEG。

### 想要 60 fps
很多机型 HD 大约 **10 fps**。

### 是 ONVIF 吗？
不是。只有 RTSP。

### 视频会离开家里吗？
信令走 Tuya。本地观看通常是摄像头→本机。手机 4G 是第二个云端观看者。

### 能用 go2rtc `tuya://` 吗？
需要 Tuya Smart 邮箱/密码，不是 Smart Life QR。

### 不在局域网时的 Cloud PTZ？
优先局域网 TCP **6668**。异地：`POST /api/cloud/auth` → `cloud_auth.json`（mode 600）。不需要 IoT 开发者密钥。

### 登录存在哪？
`%APPDATA%\TuyaRtspBridge\` 或 `~/.local/share/tuya-rtsp-bridge/`。不要进 git/截图。

### Home Assistant 插件？
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/)。需要 host 网络。[docker.md](docker.md)。

### Linux / macOS？
`./launch.sh`。Arch：[arch-linux.md](../arch-linux.md)。
