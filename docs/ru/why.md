# Зачем это нужно

Дешёвые Tuya/Smart Life камеры: нет ONVIF, нет нативного RTSP, cloud-приложение, второй viewer крадёт live-сессию.

**Tuya RTSP Bridge** — локальная программа: один QR, затем обычный RTSP:

```
rtsp://<этот-пк>:8554/<CameraName>/hd
```

Сигнализация через Tuya; видео с этого ПК обычно камера → ваша машина в LAN. Не прошивка, не 60 fps (~10 fps HD), не affiliated с Tuya Inc. Engine: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Далее: [getting-started.md](getting-started.md) · [FAQ](faq.md) · [NVR](nvr.md)

![Welcome](../images/ui-welcome.png)
![Ready](../images/ui-ready.png)
