# 入门

**Tuya Smart** / **Smart Life** / **iSmartLife** 中能看到的摄像头。

## 首次运行
1. Windows：Releases 安装包。Linux：`./launch.sh` / Arch。Docker/HA：[docker.md](../docker.md)。
2. 启动 **Tuya RTSP Bridge**（或 `http://<host>:8787`）。
3. 区域与手机一致。
4. Create QR → 扫描 → **确认**。QR 固定 **320×320**。
5. 把 HD URL 复制到 NVR。

## PTZ
界面方向键。**局域网：** TCP **6668**。**异地：** 保存一次 email+密码（`POST /api/cloud/auth`）走云端 — 无需 IoT 密钥。

## 预览
Windows Setup = VLC。Linux = ffmpeg MJPEG。RTSP 不依赖预览。
