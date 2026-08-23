# Dlaczego to istnieje

Tanie kamery Tuya / Smart Life / iSmartLife łatwo kupić i trudno nimi *władać*.

Fabryczny firmware **nie ma ONVIF** ani własnego RTSP. Podgląd idzie przez chmurę producenta. Drugi widz często kradnie sesję.

Zapłaciłeś za czujnik na *swojej* ścianie. Nagrywaj na *swoim* dysku.

**Tuya RTSP Bridge**: jeden QR w aplikacji, którą już masz, potem

```
rtsp://<ten-pc>:8554/<NazwaKamery>/hd
```

w Frigate, Agent DVR, go2rtc, VLC lub Home Assistant.

Sygnalizacja zostaje u Tuya. Z tego PC wideo zwykle zostaje w LAN.

## Czym to nie jest

To nie flash firmware, nie ONVIF i nie obietnica 60 kl./s (często ~10 kl./s HD). Silnik: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Zrzuty: [docs/images](../images/) — demo bez kont i wideo.
