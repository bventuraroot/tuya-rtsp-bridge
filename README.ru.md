# RTSP-мост Tuya

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**Превратите любую камеру Tuya / Smart Life / iSmartLife в обычную RTSP-камеру** — для Frigate, Agent DVR, go2rtc, Home Assistant или VLC.

Без прошивки. Без ONVIF (заводская прошивка его не даёт). Один QR — и обычный RTSP-адрес.

| Вы… | Начните здесь |
|---|---|
| Просто хотите, чтобы заработало | [За 5 минут](#установка-за-5-минут) |
| Лаборатория / NVR | [docs/nvr.md](docs/nvr.md) |
| Разработчик | [docs/architecture.md](docs/architecture.md) |

В репозитории **нет** аккаунтов, ID устройств и домашних IP.

## Зачем это дешёвым камерам Tuya

Камеры «Smart Life» за 20–40 € выглядят как IP-камеры. Это не так. Заводская прошивка: **нет ONVIF**, **нет галочки RTSP**. Живое видео идёт через приложение производителя и облако, которым вы не управляете. Второй телефон или «облачный NVR» часто требует подписку — или крадёт единственную живую сессию.

Вы заплатили за датчик на *своей* стене. Запись должна идти на *ваш* диск.

Это локальный мост: отсканируйте QR в уже установленном приложении — и у каждой камеры обычный адрес:

```
rtsp://<этот-пк>:8554/<ИмяКамеры>/hd
```

Сигнализация остаётся у Tuya. С этого ПК видео обычно остаётся в LAN. Подробнее: [docs/ru/why.md](docs/ru/why.md).

### Приложение

Первый запуск — язык, регион, QR, подтверждение в Smart Life:

![Экран приветствия. Пустой список, нет QR, только localhost.](docs/images/ui-welcome.png)

После входа — только демо-имена. Превью в документации нарочно чёрные (без живого видео):

![Две условные камеры, HD RTSP на 127.0.0.1.](docs/images/ui-ready.png)

## Новое в 1.2.4+

- QR-вход: фиксированный холст **320×320** (исправлен щелевой баг Windows)
- **Аддон Home Assistant OS:** [homeassistant/tuya_rtsp_bridge/](homeassistant/tuya_rtsp_bridge/) (host network)
- Docker/HA: [docs/docker.md](docs/docker.md)
- PTZ: сначала LAN (TCP 6668), опционально **cloud PTZ** после email/пароля — без IoT developer keys
- Protect-сессия: авто-relogin с сохранённым паролем

## Благодарности

RTSP-движок — **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** от **[seydx](https://github.com/seydx)** (MIT, коммит `d65b3e9`). См. [CREDITS.md](CREDITS.md) и [NOTICE.md](NOTICE.md).

## Что вы получаете

- HD: `rtsp://<этот-пк>:8554/<Имя>/hd` (обычно HEVC 1080p)
- SD: `…/sd` (H.264)
- Все камеры делят **один** IP моста; меняется только путь
- Превью, если установлен [VLC](https://www.videolan.org/)
- Языки: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Честные ограничения

- Нет ONVIF, нет нативного RTSP на камере
- Многие модели в HD дают около **10 кадр/с** — так устроена камера
- VLC 3 часто чёрный на HEVC/RTSP; используйте Agent DVR / Frigate
- Пишите на свой NVR, не на мост

Регионы: Западная/Восточная Европа, США Запад/Восток, Китай, Индия.

## Установка за 5 минут

1. Windows 10/11 **или Arch Linux**
2. Аккаунт Smart Life / Tuya Smart, где камеры уже видны

В Windows не ставьте Python, VLC и ffmpeg отдельно — они в Setup.

Windows: `TuyaRtspBridge-Setup.exe` в [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases) — далее, далее, готово. Подробности: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Вход: создать QR → сканировать в Smart Life → **подтвердить** → скопировать `rtsp://127.0.0.1:8554/<Имя>/hd`.

Сессии: `%APPDATA%\TuyaRtspBridge\` (Windows) или `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Лицензия

Наш код: MIT. Встроенный движок: MIT, Copyright (c) 2025 seydx. Не связано с Tuya Inc.

Имена, локальные данные, прилагаемые лицензии: [docs/legal.md](docs/legal.md).
