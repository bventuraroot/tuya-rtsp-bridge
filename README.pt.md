# Ponte RTSP Tuya

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**Transforme qualquer câmera Tuya / Smart Life / iSmartLife numa câmera RTSP normal** — para Frigate, Agent DVR, go2rtc, Home Assistant ou VLC.

Sem flash de firmware. Sem ONVIF (o firmware de fábrica não tem). Leia um QR e copie um URL RTSP.

| Você é… | Comece aqui |
|---|---|
| Só quer que funcione | [Em 5 minutos](#instalação-em-5-minutos) |
| Laboratório / NVR | [docs/nvr.md](docs/nvr.md) |
| Desenvolvedor | [docs/architecture.md](docs/architecture.md) |

Este repositório **não** inclui contas, IDs de aparelhos nem IPs de casa.

## Por que câmeras Tuya baratas precisam disso

Essas câmeras «Smart Life» de 20–40 € parecem câmeras IP. Não são. Firmware de fábrica: **sem ONVIF**, **sem caixa RTSP**. O ao vivo vai pelo app do fabricante e uma nuvem que você não controla. Um segundo celular ou um «NVR na nuvem» costuma ser assinatura — ou rouba a única sessão ao vivo.

Você pagou um sensor na *sua* parede. A gravação deve ir para o *seu* disco.

Este app é uma ponte local: leia um QR no app que você já tem e cada câmera ganha um URL normal:

```
rtsp://<este-pc>:8554/<NomeCamera>/hd
```

A sinalização continua na Tuya. Neste PC o vídeo em geral fica na LAN. Texto longo: [docs/pt/why.md](docs/pt/why.md).

### O aplicativo

Primeira execução — idioma, região, QR, confirmar no Smart Life:

![Tela inicial. Lista vazia, sem QR, só localhost.](docs/images/ui-welcome.png)

Depois do login — só nomes de demonstração. As prévias ficam pretas de propósito (sem vídeo na documentação):

![Duas câmeras de exemplo, RTSP HD em 127.0.0.1.](docs/images/ui-ready.png)

## Novo em 1.2.4+

- Login QR: canvas fixo **320×320** (bug da fenda no Windows corrigido)
- **Add-on Home Assistant OS:** [homeassistant/tuya_rtsp_bridge/](homeassistant/tuya_rtsp_bridge/) (host network)
- Docker/HA: [docs/docker.md](docs/docker.md)
- PTZ: LAN primeiro (TCP 6668), **cloud PTZ** opcional após email/password — sem chaves IoT developer
- Sessão protect: re-login automático com password guardada

## Créditos

O motor RTSP é o **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** de **[seydx](https://github.com/seydx)** (MIT, commit `d65b3e9`). Ver [CREDITS.md](CREDITS.md) e [NOTICE.md](NOTICE.md).

## O que você ganha

- HD: `rtsp://<este-pc>:8554/<Nome>/hd` (geralmente HEVC 1080p)
- SD: `…/sd` (H.264)
- Todas as câmeras compartilham **um** IP da ponte; só o caminho muda
- Prévia se o [VLC](https://www.videolan.org/) estiver instalado
- Idiomas: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Limites honestos

- Sem ONVIF, sem RTSP nativo na câmera
- Muitos modelos saem a cerca de **10 fps** em HD — é a câmera
- VLC 3 muitas vezes fica preto em HEVC/RTSP; use Agent DVR / Frigate
- Grave no seu NVR, não na ponte

Regiões: Europa Ocidental/Oriental, EUA Oeste/Leste, China, Índia.

## Instalação em 5 minutos

1. Windows 10/11 **ou Arch Linux**
2. Uma conta Smart Life / Tuya Smart que já veja as câmeras

No Windows não instale Python, VLC nem ffmpeg: já vão no Setup.

Windows: `TuyaRtspBridge-Setup.exe` em [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases) — seguinte, seguinte, concluir. Detalhes: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Login: criar QR → ler no Smart Life → **confirmar** → copiar `rtsp://127.0.0.1:8554/<Nome>/hd`.

Sessões: `%APPDATA%\TuyaRtspBridge\` (Windows) ou `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Licença

Nosso código: MIT. Motor incluso: MIT, Copyright (c) 2025 seydx. Não afiliado à Tuya Inc.

Nomes, dados locais, licenças incluídas: [docs/legal.md](docs/legal.md).
