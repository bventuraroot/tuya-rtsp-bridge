# 入门

**Tuya Smart** / **Smart Life** / **iSmartLife** 中能看到的摄像头。

## 首次运行
1. Windows：从 [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases) 安装。Linux：`./launch.sh`。Docker/HA：[docker.md](docker.md)。
2. 启动 **Tuya RTSP Bridge** 或 `http://<host>:8787`。
3. 区域与手机一致。
4. Create QR → 扫描 → **确认**。QR 固定 **320×320**。
5. 把 HD URL 复制到 NVR。

会话：`%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`。保存邮箱/密码后可自动重新登录。

## 搬家 / 新 Wi‑Fi
不要从账号删除摄像头。在 App 里换新 SSID，在新局域网跑 bridge，NVR 只改 PC IP。

## PTZ
界面方向键。局域网 **TCP 6668**。异地 cloud：`POST /api/cloud/auth`。

## 预览 / 自启
Windows Setup 含 VLC。Linux 用 ffmpeg MJPEG。`launch-hidden.vbs` / user systemd。
