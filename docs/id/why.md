# Mengapa ini ada

Kamera Tuya / Smart Life / iSmartLife murah mudah dibeli dan sulit *dimiliki*.

Firmware pabrik **tidak punya ONVIF** maupun RTSP sendiri. Tayangan langsung lewat awan pabrik. Penonton kedua sering mencuri sesi.

Anda membayar sensor di dinding *Anda*. Rekam ke disk *Anda*.

**Tuya RTSP Bridge**: satu QR di aplikasi yang sudah Anda miliki, lalu

```
rtsp://<pc-ini>:8554/<NamaKamera>/hd
```

di Frigate, Agent DVR, go2rtc, VLC, atau Home Assistant.

Pensinyalan tetap di Tuya. Dari PC ini video biasanya tetap di LAN.

## Bukan apa

Bukan flash firmware, bukan ONVIF, bukan janji 60 fps (sering ~10 fps HD). Mesin: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Cuplikan: [docs/images](../images/) — demo tanpa akun dan tanpa video.
