# Warum es das gibt

Billige Tuya-/Smart-Life-/iSmartLife-Kameras sind leicht zu kaufen und schwer zu *besitzen*.

Die Box sieht aus wie eine normale IP-Kamera. Praktisch hat der Hersteller die nützlichen Teile hinter der Cloud verriegelt:

- **Kein ONVIF** auf Stock-Firmware.
- **Kein kameranatives RTSP**, das du in Frigate, Agent DVR, go2rtc oder Home Assistant pasten kannst.
- Die offizielle App will Account, Handy und einen Pfad über Server, die du nicht kontrollierst.
- Zweites Handy oder „Cloud-NVR“ heißt oft Abo — oder ein zweiter Viewer, der die Live-Session stiehlt.

Du hast für einen Sensor an *deiner* Wand bezahlt. Aufzeichnung gehört auf *deine* Platte.

**Tuya RTSP Bridge** ist ein kleines lokales Programm (Windows oder Arch Linux), das diese Kameras zu normalen RTSP-Kameras macht. Einmal QR mit der App scannen, die du schon hast. Danach hat jede Kamera eine normale URL:

```
rtsp://<dieser-pc>:8554/<CameraName>/hd
```

Das in Frigate, Agent DVR, go2rtc, VLC oder Home Assistant. Motion, Archiv und Benachrichtigungen bleiben in Software, *die du* wählst.

## Was du gewinnst

| Ohne das | Mit dem |
|---|---|
| Nur Cloud-Liveview | Lokales RTSP, gleiches LAN |
| App-Lock-in | Jeder NVR mit RTSP |
| Kein ONVIF | Du brauchst kein ONVIF |
| Extra Cloud-Viewer = Lag / verlorene Session | Eine Engine, viele lokale Clients |
| Aufnahmen auf fremdem Storage | Aufnahmen auf NAS / Frigate / Agent |
| „Geht, bis der Vendor die App ändert“ | Du behältst die RTSP-URL |

Signaling (Login, Handshake) nutzt weiter Tuya-Server. Wenn du von diesem PC schaust, bleibt das **Video** typisch Kamera → deine Maschine im LAN. Punkt: billige Hardware, lokales Archiv.

## Was das nicht ist

- Kein Firmware-Flash, kein Jailbreak, kein ONVIF.
- Kein Versprechen von 60 fps — viele Cams liefern ca. **10 fps** HD-HEVC. Das ist die Kamera.
- Kein Cloud-Killer für die Handy-App. Das Handy darf bleiben. Das ist der *lokale* NVR-Pfad.
- Nicht affiliated mit Tuya Inc. Die RTSP-Engine ist [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

## Für wen

- **Jeden**, der eine „Smart Life“-Cam gekauft hat und „wo ist die RTSP-Checkbox?“ gefragt hat.
- **Homelab** mit Frigate / Agent DVR / Home Assistant.
- **Entwickler** mit lokaler API (`:8787`) und MIT-Tree zum Forken.

## So sieht’s aus

Erster Start — Sprache und Region, QR erzeugen, in Smart Life scannen, bestätigen:

![Willkommensbildschirm Tuya RTSP Bridge. Leere Kameraliste, noch kein QR, nur localhost.](../images/ui-welcome.png)

Nach Login — nur Platzhalter-Kameranamen (kein Livebild, keine echten Device-IDs). HD-URL in den NVR kopieren:

![Bereit-Screen mit zwei Demo-Kameras, schwarzen Preview-Fenstern, RTSP-URLs auf 127.0.0.1.](../images/ui-ready.png)

Screenshots aus einer Demo-Session. Keine Accounts, Seriennummern oder Video.

Weiter: [getting-started.md](getting-started.md) · [FAQ](faq.md) · [NVR](nvr.md)
