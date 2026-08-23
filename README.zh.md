# 涂鸦 RTSP 网桥

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**把任意涂鸦 / Smart Life / iSmartLife 摄像机变成普通 RTSP 摄像机**，供 Frigate、Agent DVR、go2rtc、Home Assistant 或 VLC 使用。

不用刷机。原厂固件**没有 ONVIF**。扫一次二维码，复制一条 RTSP 地址即可。

| 你是… | 从这里开始 |
|---|---|
| 只想先用起来 | [五分钟安装](#五分钟安装) |
| 家庭实验室 / NVR | [docs/nvr.md](docs/nvr.md) |
| 开发者 | [docs/architecture.md](docs/architecture.md) |

本仓库**不含**任何账号、设备 ID 或家庭 IP。

## 为什么便宜的涂鸦摄像机需要它

二三十欧的「Smart Life」摄像头看起来像网络摄像机，其实不是。原厂固件：**没有 ONVIF**，**没有 RTSP 开关**。看直播只能走厂家 App 和你无法控制的云。第二部手机或「云录像」往往要订阅——或者抢走唯一的直播会话。

传感器装在**你的**墙上，录像应落在**你的**硬盘上。

本程序是本地小网桥：用你已有的 App 扫码，之后每台摄像机都有普通地址：

```
rtsp://<本机>:8554/<摄像机名>/hd
```

信令仍走涂鸦。从这台电脑观看时，视频通常留在局域网。详见 [docs/zh/why.md](docs/zh/why.md)。

### 界面

首次运行 — 语言、区域、二维码，在 Smart Life 中确认：

![欢迎界面。空列表，尚无二维码，仅 localhost。](docs/images/ui-welcome.png)

登录后 — 仅为演示名称。文档中预览故意为黑（无实况画面）：

![两台占位摄像机，高清 RTSP 指向 127.0.0.1。](docs/images/ui-ready.png)

## 致谢

RTSP 引擎是 **[seydx](https://github.com/seydx)** 的 **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)**（MIT，提交 `d65b3e9`）。见 [CREDITS.md](CREDITS.md)、[NOTICE.md](NOTICE.md)。

## 你得到什么

- 高清：`rtsp://<本机>:8554/<名称>/hd`（多为 HEVC 1080p）
- 标清：`…/sd`（H.264）
- 所有摄像机共用**一个**网桥 IP，只改路径
- 安装 [VLC](https://www.videolan.org/) 可预览
- 语言：English、Deutsch、Nederlands、Français、Español、Português、Italiano、Polski、Čeština、Русский、Українська、Bahasa Indonesia、简体中文、हिन्दी

## 实话实说的限制

- 无 ONVIF，摄像机本身无 RTSP
- 很多型号高清大约 **10 帧**——这是摄像机决定的
- VLC 3 播 HEVC/RTSP 经常黑屏；请用 Agent DVR / Frigate
- 录像请放在你的 NVR，不要放在网桥上

登录区域：西欧/东欧、美国西/东、中国、印度。

## 五分钟安装

1. Windows 10/11 **或 Arch Linux**
2. 已能在 Smart Life / 涂鸦智能 里看到摄像机的账号

Windows 不必另装 Python、VLC 或 ffmpeg，都在安装包里。

Windows：[Releases](../../releases) 里的 `TuyaRtspBridge-Setup.exe`，下一步即可。说明：[docs/windows.md](docs/windows.md)。  
Arch：[docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

登录：生成二维码 → Smart Life 扫描 → **确认** → 复制 `rtsp://127.0.0.1:8554/<名称>/hd`。

会话：Windows 在 `%APPDATA%\TuyaRtspBridge\`，Linux 在 `~/.local/share/tuya-rtsp-bridge/`。

## 许可

我们的代码：MIT。内嵌引擎：MIT，Copyright (c) 2025 seydx。与涂鸦智能无隶属关系。
