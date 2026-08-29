# Pourquoi ce projet existe

Les caméras Tuya / Smart Life bon marché sont faciles à acheter et dures à *posséder* : pas d’ONVIF, pas de RTSP natif, app cloud, second viewer = session volée.

**Tuya RTSP Bridge** : QR une fois, puis RTSP local :

```
rtsp://<ce-pc>:8554/<CameraName>/hd
```

Signaling via Tuya ; la vidéo depuis ce PC reste en général caméra → machine sur le LAN.

Pas un flash firmware, pas 60 fps (~10 fps HD), pas affilié à Tuya Inc. Engine MIT : [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal).

Suite : [getting-started.md](getting-started.md) · [FAQ](faq.md) · [NVR](nvr.md)

![Welcome](../images/ui-welcome.png)
![Ready](../images/ui-ready.png)
