# RTSP-міст Tuya

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md)

**Перетворіть будь-яку камеру Tuya / Smart Life / iSmartLife на звичайну RTSP-камеру** — для Frigate, Agent DVR, go2rtc, Home Assistant або VLC.

Без прошивки. Без ONVIF (заводська прошивка його не дає). Один QR — і звичайна RTSP-адреса.

| Ви… | Почніть тут |
|---|---|
| Просто хочете, щоб запрацювало | [За 5 хвилин](#встановлення-за-5-хвилин) |
| Лабораторія / NVR | [docs/nvr.md](docs/nvr.md) |
| Розробник | [docs/architecture.md](docs/architecture.md) |

У репозиторії **немає** облікових записів, ID пристроїв і домашніх IP.

## Навіщо це дешевим камерам Tuya

Камери «Smart Life» за 20–40 € виглядають як IP-камери. Це не так. Заводська прошивка: **немає ONVIF**, **немає галочки RTSP**. Живе відео йде через додаток виробника й хмару, якою ви не керуєте. Другий телефон або «хмаровий NVR» часто хоче підписку — або краде єдиний живий сеанс.

Ви заплатили за датчик на *своїй* стіні. Запис має йти на *ваш* диск.

Це локальний міст: відскануйте QR у вже встановленому додатку — і кожна камера має звичайну адресу:

```
rtsp://<цей-пк>:8554/<НазваКамери>/hd
```

Сигналізація лишається в Tuya. З цього ПК відео зазвичай лишається в LAN. Докладніше: [docs/uk/why.md](docs/uk/why.md).

### Програма

Перший запуск — мова, регіон, QR, підтвердження в Smart Life:

![Екран вітання. Порожній список, немає QR, лише localhost.](docs/images/ui-welcome.png)

Після входу — лише демо-назви. Попередній перегляд у документації навмисно чорний (без живого відео):

![Дві умовні камери, HD RTSP на 127.0.0.1.](docs/images/ui-ready.png)

## Подяки

RTSP-рушій — **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** від **[seydx](https://github.com/seydx)** (MIT, коміт `d65b3e9`). Див. [CREDITS.md](CREDITS.md) і [NOTICE.md](NOTICE.md).

## Що ви отримуєте

- HD: `rtsp://<цей-пк>:8554/<Назва>/hd` (зазвичай HEVC 1080p)
- SD: `…/sd` (H.264)
- Усі камери ділять **одну** IP моста; змінюється лише шлях
- Попередній перегляд, якщо встановлено [VLC](https://www.videolan.org/)
- Мови: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Чесні обмеження

- Немає ONVIF, немає рідного RTSP на камері
- Багато моделей у HD дають близько **10 кадр/с** — так влаштована камера
- VLC 3 часто чорний на HEVC/RTSP; використовуйте Agent DVR / Frigate
- Пишіть на свій NVR, не на міст

Регіони: Західна/Східна Європа, США Захід/Схід, Китай, Індія.

## Встановлення за 5 хвилин

1. Windows 10/11 **або Arch Linux**
2. Обліковий запис Smart Life / Tuya Smart, де камери вже видно

У Windows не ставте Python, VLC і ffmpeg окремо — вони в Setup.

Windows: `TuyaRtspBridge-Setup.exe` у [Releases](../../releases) — далі, далі, готово. Подробиці: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Вхід: створити QR → сканувати в Smart Life → **підтвердити** → скопіювати `rtsp://127.0.0.1:8554/<Назва>/hd`.

Сеанси: `%APPDATA%\TuyaRtspBridge\` (Windows) або `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Ліцензія

Наш код: MIT. Вбудований рушій: MIT, Copyright (c) 2025 seydx. Не пов’язано з Tuya Inc.
