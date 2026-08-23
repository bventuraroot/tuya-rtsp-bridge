# Waarom dit bestaat

Goedkope Tuya- / Smart Life- / iSmartLife-camera’s (vaak Action / LSC) zijn makkelijk te kopen en moeilijk te *bezitten*.

Fabrieksfirmware heeft **geen ONVIF** en geen eigen RTSP. Live beeld gaat via de cloud van de fabrikant. Een tweede kijker steelt vaak de sessie.

Jij hebt een sensor op *jouw* muur betaald. Neem op op *jouw* schijf.

**Tuya RTSP Bridge**: één QR in de app die je al hebt, daarna

```
rtsp://<deze-pc>:8554/<Cameranaam>/hd
```

in Frigate, Agent DVR, go2rtc, VLC of Home Assistant.

Signaling blijft bij Tuya. Vanaf deze pc blijft de video meestal op het LAN.

## Wat het niet is

Geen firmware-flash, geen ONVIF, geen belofte van 60 fps (vaak ~10 fps HD). Engine: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Schermafbeeldingen: [docs/images](../images/) — demo zonder accounts of video.
