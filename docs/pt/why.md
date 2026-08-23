# Por que existe

Câmeras Tuya / Smart Life / iSmartLife baratas são fáceis de comprar e difíceis de *possuir*.

O firmware de fábrica **não tem ONVIF** nem RTSP nativo. O ao vivo vai pela nuvem do fabricante. Um segundo espectador muitas vezes rouba a sessão.

Você pagou um sensor na *sua* parede. Grave no *seu* disco.

**Tuya RTSP Bridge**: um QR no app que você já tem, depois

```
rtsp://<este-pc>:8554/<NomeCamera>/hd
```

no Frigate, Agent DVR, go2rtc, VLC ou Home Assistant.

A sinalização continua na Tuya. Neste PC o vídeo em geral fica na LAN.

## O que não é

Não é flash de firmware, não é ONVIF, não promete 60 fps (muitas vezes ~10 fps HD). Motor: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Capturas: [docs/images](../images/) — demo sem contas nem vídeo.
