# Por qué existe

Las cámaras Tuya / Smart Life / iSmartLife baratas son fáciles de comprar y difíciles de *poseer*.

El firmware de fábrica **no tiene ONVIF** ni RTSP nativo. El directo va por la nube del fabricante. Un segundo espectador a menudo roba la sesión.

Pagaste un sensor en *tu* pared. Graba en *tu* disco.

**Tuya RTSP Bridge**: un QR en la app que ya tienes, luego

```
rtsp://<este-pc>:8554/<NombreCamara>/hd
```

en Frigate, Agent DVR, go2rtc, VLC o Home Assistant.

La señalización sigue en Tuya. Desde este PC el vídeo suele quedarse en la LAN.

## Qué no es

No es un flasheo, no es ONVIF, no promete 60 fps (a menudo ~10 fps HD). Motor: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Capturas: [docs/images](../images/) — demo sin cuentas ni vídeo.
