# Proč to existuje

Levné kamery Tuya / Smart Life / iSmartLife se snadno koupí a těžko *vlastní*.

Tovární firmware **nemá ONVIF** ani nativní RTSP. Živý náhled jde přes cloud výrobce. Druhý divák často ukradne relaci.

Zaplatili jste senzor na *vaší* zdi. Nahrávejte na *váš* disk.

**Tuya RTSP Bridge**: jeden QR v aplikaci, kterou už máte, pak

```
rtsp://<tento-pc>:8554/<NazevKamery>/hd
```

ve Frigate, Agent DVR, go2rtc, VLC nebo Home Assistant.

Signaling zůstává u Tuya. Z tohoto PC video obvykle zůstane v LAN.

## Co to není

Není to flash firmwaru, není to ONVIF, neslibuje 60 fps (často ~10 fps HD). Engine: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Snímky: [docs/images](../images/) — demo bez účtů a videa.
