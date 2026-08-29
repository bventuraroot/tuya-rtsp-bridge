# Waarom dit bestaat

Goedkope Tuya-/Smart Life-/iSmartLife-camera’s zijn makkelijk te kopen en lastig te *bezitten*.

De doos lijkt op een normale IP-camera. In de praktijk zit het nuttige achter de cloud:
- **Geen ONVIF** op stock-firmware.
- **Geen camera-native RTSP** voor Frigate/Agent/go2rtc/HA.
- Officiële app wil account, telefoon en servers die jij niet beheert.
- Tweede telefoon of «cloud-NVR» = vaak abonnement of gestolen live-sessie.

Je betaalde voor een sensor aan *jouw* muur. Opnames horen op *jouw* schijf.

**Tuya RTSP Bridge** is een klein lokaal programma dat die camera’s gewone RTSP-camera’s maakt. Eén QR met de app die je al hebt. Daarna:

```
rtsp://<deze-pc>:8554/<CameraName>/hd
```

## Wat je wint
| Zonder | Met |
|---|---|
| Alleen cloud-live | Lokaal RTSP, zelfde LAN |
| App-lock-in | Elke RTSP-NVR |
| Geen ONVIF | ONVIF niet nodig |
| Extra cloud-viewer = lag/sessie kwijt | Eén engine, veel lokale clients |
| Opnames op andermans storage | Opnames op NAS/Frigate/Agent |

Signaling gebruikt nog Tuya. Video vanaf deze pc blijft typisch camera → jouw machine op LAN.

## Wat het niet is
Geen firmware-flash, geen jailbreak, geen ONVIF. Geen 60 fps-belofte (~**10 fps** HD HEVC is de camera). Geen cloud-killer voor de telefoon-app. Niet affiliated met Tuya Inc. Engine: [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Volgende: [getting-started.md](getting-started.md) · [FAQ](faq.md) · [NVR](nvr.md)

![Welcome](../images/ui-welcome.png)
![Ready](../images/ui-ready.png)
