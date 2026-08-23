# Puente RTSP Tuya

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**Convierte cualquier cámara Tuya / Smart Life / iSmartLife en una cámara RTSP normal** — para Frigate, Agent DVR, go2rtc, Home Assistant o VLC.

Sin flashear firmware. Sin ONVIF (el firmware de fábrica no lo trae). Escanea un QR y copia una URL RTSP.

| Tú eres… | Empieza aquí |
|---|---|
| Solo quieres que funcione | [En 5 minutos](#instalación-en-5-minutos) |
| Laboratorio / NVR | [docs/nvr.md](docs/nvr.md) |
| Desarrollador | [docs/architecture.md](docs/architecture.md) |

Este repositorio **no** incluye cuentas, IDs de dispositivos ni IPs de casa.

## Por qué las cámaras Tuya baratas lo necesitan

Esas cámaras «Smart Life» de 20–40 € parecen IP. No lo son. Firmware de fábrica: **sin ONVIF**, **sin casilla RTSP**. El directo va por la app del fabricante y una nube que no controlas. Un segundo teléfono o un «NVR en la nube» suele ser una suscripción — o roba la única sesión en vivo.

Pagaste un sensor en *tu* pared. La grabación debe ir a *tu* disco.

Esta app es un puente local: escanea un QR en la app que ya tienes y cada cámara tiene una URL normal:

```
rtsp://<este-pc>:8554/<NombreCamara>/hd
```

La señalización sigue en Tuya. Desde este PC el vídeo suele quedarse en la LAN. Texto largo: [docs/es/why.md](docs/es/why.md).

### La aplicación

Primer arranque — idioma, región, QR, confirmar en Smart Life:

![Pantalla de bienvenida. Lista vacía, sin QR, solo localhost.](docs/images/ui-welcome.png)

Tras el login — solo nombres de demo. Las vistas previas están negras a propósito (sin vídeo en la documentación):

![Dos cámaras de ejemplo, RTSP HD en 127.0.0.1.](docs/images/ui-ready.png)

## Créditos

El motor RTSP es **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** de **[seydx](https://github.com/seydx)** (MIT, commit `d65b3e9`). Ver [CREDITS.md](CREDITS.md) y [NOTICE.md](NOTICE.md).

## Qué obtienes

- HD: `rtsp://<este-pc>:8554/<Nombre>/hd` (suele ser HEVC 1080p)
- SD: `…/sd` (H.264)
- Todas las cámaras comparten **una** IP de puente; solo cambia la ruta
- Vista previa si instalas [VLC](https://www.videolan.org/)
- Idiomas: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Límites honestos

- Sin ONVIF, sin RTSP nativo en la cámara
- Muchos modelos sacan unos **10 fps** en HD — es la cámara
- VLC 3 a menudo se pone negro con HEVC/RTSP; usa Agent DVR / Frigate
- Graba en tu NVR, no en el puente

Regiones: Europa Occidental/Oriental, EE. UU. Oeste/Este, China, India.

## Instalación en 5 minutos

1. Windows 10/11 **o Arch Linux**
2. Una cuenta Smart Life / Tuya Smart que ya vea las cámaras

En Windows no instales Python, VLC ni ffmpeg: van en el Setup.

Windows: `TuyaRtspBridge-Setup.exe` en [Releases](../../releases) — siguiente, siguiente, finalizar. Detalles: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Login: crear QR → escanear en Smart Life → **confirmar** → copiar `rtsp://127.0.0.1:8554/<Nombre>/hd`.

Sesiones: `%APPDATA%\TuyaRtspBridge\` (Windows) o `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Licencia

Nuestro código: MIT. Motor incluido: MIT, Copyright (c) 2025 seydx. No afiliado a Tuya Inc.

Nombres, datos locales, licencias incluidas: [docs/legal.md](docs/legal.md).
