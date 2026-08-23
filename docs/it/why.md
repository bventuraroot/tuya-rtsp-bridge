# Perché esiste

Le telecamere Tuya / Smart Life / iSmartLife economiche sono facili da comprare e difficili da *possedere*.

Il firmware di serie **non ha ONVIF** né RTSP nativo. Il live passa dal cloud del produttore. Un secondo spettatore spesso ruba la sessione.

Hai pagato un sensore sul *tuo* muro. Registra sul *tuo* disco.

**Tuya RTSP Bridge**: un QR nell’app che hai già, poi

```
rtsp://<questo-pc>:8554/<NomeTelecamera>/hd
```

in Frigate, Agent DVR, go2rtc, VLC o Home Assistant.

La segnalazione resta su Tuya. Da questo PC il video di solito resta sulla LAN.

## Cosa non è

Non è un flash firmware, non è ONVIF, non promette 60 fps (spesso ~10 fps HD). Motore: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Schermate: [docs/images](../images/) — demo senza account né video.
