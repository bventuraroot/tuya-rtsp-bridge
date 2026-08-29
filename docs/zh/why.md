# 为什么需要它

便宜的 Tuya 摄像头没有 ONVIF、没有原生 RTSP，只能走厂商云。

**Tuya RTSP Bridge**：扫一次 QR，变成普通 RTSP：

```
rtsp://<本机>:8554/<CameraName>/hd
```

信令仍走 Tuya；在本机观看时视频通常是 摄像头→局域网本机。不是刷机，也不保证 60 fps。引擎 MIT：[seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)。

下一步：[getting-started.md](getting-started.md) · [FAQ](faq.md) · [NVR](nvr.md)

![Welcome](../images/ui-welcome.png)
![Ready](../images/ui-ready.png)
