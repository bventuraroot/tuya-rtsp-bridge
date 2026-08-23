# Pont RTSP Tuya

[![Licence : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md)

**Transformez n’importe quelle caméra Tuya / Smart Life / iSmartLife en caméra RTSP normale** — pour Frigate, Agent DVR, go2rtc, Home Assistant ou VLC.

Pas de flash firmware. Pas d’ONVIF (le firmware d’origine n’en a pas). Un QR à scanner, puis une URL RTSP à copier.

| Vous êtes… | Commencez ici |
|---|---|
| Vous voulez que ça marche | [En 5 minutes](#installation-en-5-minutes) |
| Labo / NVR | [docs/nvr.md](docs/nvr.md) |
| Développeur | [docs/architecture.md](docs/architecture.md) |

Ce dépôt ne contient **aucun** compte, identifiant d’appareil ou IP personnelle.

## Pourquoi les caméras Tuya bon marché en ont besoin

Ces caméras « Smart Life » à 20–40 € ressemblent à des caméras IP. Elles n’en sont pas. Firmware d’origine : **pas d’ONVIF**, **pas de case RTSP**. Le direct passe par l’appli du fabricant et un cloud que vous ne contrôlez pas. Un second téléphone ou un « NVR cloud » veut souvent un abonnement — ou vole l’unique session live.

Vous avez payé un capteur sur *votre* mur. L’enregistrement doit aller sur *votre* disque.

Cette appli est un petit pont local : scannez un QR dans l’appli que vous avez déjà, puis chaque caméra a une URL normale :

```
rtsp://<ce-pc>:8554/<NomCamera>/hd
```

La signalisation reste chez Tuya. Depuis ce PC, la vidéo reste en général sur le LAN. Texte long : [docs/fr/why.md](docs/fr/why.md).

### L’application

Premier lancement — langue, région, QR, confirmation dans Smart Life :

![Écran d’accueil. Liste vide, pas de QR, localhost seulement.](docs/images/ui-welcome.png)

Après connexion — noms de démo uniquement. Les aperçus restent noirs dans la doc (pas d’image live) :

![Deux caméras fictives, RTSP HD sur 127.0.0.1.](docs/images/ui-ready.png)

## Crédits

Le moteur RTSP est **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** de **[seydx](https://github.com/seydx)** (MIT), commit `d65b3e9`. Voir [CREDITS.md](CREDITS.md) et [NOTICE.md](NOTICE.md).

## Ce que vous obtenez

- HD : `rtsp://<ce-pc>:8554/<NomCamera>/hd` (souvent HEVC 1080p)
- SD : `…/sd` (H.264)
- Toutes les caméras partagent **une** IP de pont ; seul le chemin change
- Aperçu si [VLC](https://www.videolan.org/) est installé
- Langues : English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Limites honnêtes

- Pas d’ONVIF, pas de RTSP natif sur la caméra
- Beaucoup de modèles sortent environ **10 im/s** en HD — c’est la caméra
- VLC 3 est souvent noir en HEVC/RTSP ; Agent DVR / Frigate sont les clients visés
- L’enregistrement se fait dans votre NVR, pas sur le pont

Régions : Europe de l’Ouest/Est, USA Ouest/Est, Chine, Inde.

## Installation en 5 minutes

1. Windows 10/11 **ou Arch Linux**
2. Un compte Smart Life / Tuya Smart qui voit déjà les caméras

Sous Windows : pas besoin d’installer Python, VLC ni ffmpeg. C’est dans le Setup.

Windows : `TuyaRtspBridge-Setup.exe` dans [Releases](../../releases) — suivant, suivant, terminer. Détails : [docs/windows.md](docs/windows.md).  
Arch : [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Connexion : créer le QR → scanner dans Smart Life → **confirmer** → copier `rtsp://127.0.0.1:8554/<Nom>/hd`.

Sessions : `%APPDATA%\TuyaRtspBridge\` (Windows) ou `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Licence

Notre code : MIT. Moteur vendu : MIT, Copyright (c) 2025 seydx. Non affilié à Tuya Inc.
