# 为什么要做这个

便宜的涂鸦 / Smart Life / iSmartLife 摄像机好买、难真正“拥有”。

原厂固件**没有 ONVIF**，也**没有**可粘贴到 Frigate、Agent DVR、go2rtc、Home Assistant 的摄像机自带 RTSP。直播走厂家 App 和你控制不了的云。第二部手机或“云录像”常常要订阅，或抢走唯一直播会话。

传感器在**你的**墙上，录像应在**你的**盘上。

**涂鸦 RTSP 网桥**：用现有 App 扫一次码，然后每台摄像机都有普通地址：

```
rtsp://<本机>:8554/<名称>/hd
```

信令仍走涂鸦。从这台电脑看时，视频通常留在局域网。

## 它不是什么

不是刷机，不是 ONVIF，也不保证 60 帧（很多型号高清约 10 帧）。引擎：[seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)（MIT）。

截图见 [docs/images](../images/)，为演示，无账号、无实况。
