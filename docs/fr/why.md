# Pourquoi ça existe

Les caméras Tuya / Smart Life / iSmartLife bon marché sont faciles à acheter et pénibles à *posséder*.

Le firmware d’origine **n’a pas d’ONVIF** ni de RTSP natif. Le direct passe par le cloud du fabricant. Un second spectateur vole souvent la session.

Vous avez payé un capteur sur *votre* mur. Enregistrez sur *votre* disque.

**Tuya RTSP Bridge** : un QR dans l’appli déjà installée, puis

```
rtsp://<ce-pc>:8554/<NomCamera>/hd
```

dans Frigate, Agent DVR, go2rtc, VLC ou Home Assistant.

La signalisation reste chez Tuya. Depuis ce PC, la vidéo reste en général sur le LAN.

## Ce que ce n’est pas

Pas un flash firmware, pas de l’ONVIF, pas une promesse de 60 im/s (souvent ~10 im/s HD). Moteur : [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT).

Captures d’écran : [docs/images](../images/) — démo sans comptes ni vidéo.
