# 常见问题

### 登录后摄像头列表为空
区域选错。德文 App 里的「西欧」是 **EU**，不是 WE。

### QR 一直不完成
保持窗口打开，并在手机上**确认**。

### QR 极小 / 一条缝 / 扫不了（Windows）
**1.2.4+** 已修：固定 **320×320** 画布（NEAREST）。请更新应用。点 Create QR 前显示 «No QR» 正常。

### 连接被拒绝（WinError 10061）
界面会自动拉起 API（`:8787`）。再点一次 Create QR。

### VLC 黑屏
VLC 3 常在 HEVC/RTSP 上失败。流其实还在。用 Agent/Frigate。Linux 用 ffmpeg MJPEG。

### 想要 60 fps
很多机型 HD 大约 **10 fps**。

### 是 ONVIF 吗？
不是。只有 RTSP。

### 视频会离开家里吗？
信令走 Tuya。本地观看通常是 摄像头→本机。

### 不在局域网时的 Cloud PTZ？
优先局域网 PTZ（TCP **6668**）。异地：保存一次 email+密码（`POST /api/cloud/auth`）走云端 — 不需要 IoT 开发者密钥。

### Home Assistant 插件？
有 — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/)。需要 host 网络。Docker：[docker.md](../docker.md)。

### Linux / macOS？
`./launch.sh`。Arch：[arch-linux.md](../arch-linux.md)。数据：`~/.local/share/tuya-rtsp-bridge/`。
