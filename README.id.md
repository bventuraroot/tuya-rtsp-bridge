# Jembatan RTSP Tuya

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**Ubah kamera Tuya / Smart Life / iSmartLife apa pun menjadi kamera RTSP biasa** — untuk Frigate, Agent DVR, go2rtc, Home Assistant, atau VLC.

Tanpa flash firmware. Tanpa ONVIF (firmware pabrik tidak punya). Pindai QR, salin URL RTSP.

| Anda… | Mulai di sini |
|---|---|
| Hanya ingin berjalan | [Dalam 5 menit](#pemasangan-dalam-5-menit) |
| Homelab / NVR | [docs/nvr.md](docs/nvr.md) |
| Pengembang | [docs/architecture.md](docs/architecture.md) |

Repositori ini **tidak** berisi akun, ID perangkat, atau IP rumah.

## Mengapa kamera Tuya murah membutuhkannya

Kamera «Smart Life» seharga 20–40 € tampak seperti kamera IP. Bukan. Firmware pabrik: **tanpa ONVIF**, **tanpa kotak RTSP**. Tayangan langsung lewat aplikasi pabrik dan awan yang tidak Anda kendalikan. Ponsel kedua atau «NVR awan» sering berarti langganan — atau mencuri satu-satunya sesi langsung.

Anda membayar sensor di dinding *Anda*. Rekaman harus ke disk *Anda*.

Aplikasi ini adalah jembatan lokal: pindai QR di aplikasi yang sudah Anda miliki, lalu setiap kamera punya URL biasa:

```
rtsp://<pc-ini>:8554/<NamaKamera>/hd
```

Pensinyalan tetap di Tuya. Dari PC ini video biasanya tetap di LAN. Teks panjang: [docs/id/why.md](docs/id/why.md).

### Aplikasinya

Pertama kali — bahasa, wilayah, QR, konfirmasi di Smart Life:

![Layar selamat datang. Daftar kosong, belum ada QR, hanya localhost.](docs/images/ui-welcome.png)

Setelah masuk — hanya nama demo. Pratinjau di dokumentasi sengaja hitam (tanpa video langsung):

![Dua kamera contoh, RTSP HD di 127.0.0.1.](docs/images/ui-ready.png)

## Baru di 1.2.4+

- Login QR: kanvas tetap **320×320** (bug celah Windows diperbaiki)
- **Add-on Home Assistant OS:** [homeassistant/tuya_rtsp_bridge/](homeassistant/tuya_rtsp_bridge/) (host network)
- Docker/HA: [docs/docker.md](docs/docker.md)
- PTZ: LAN dulu (TCP 6668), opsional **cloud PTZ** setelah email/password — tanpa kunci IoT developer
- Sesi protect: auto-relogin dengan password tersimpan

## Kredit

Mesin RTSP adalah **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** milik **[seydx](https://github.com/seydx)** (MIT, komit `d65b3e9`). Lihat [CREDITS.md](CREDITS.md) dan [NOTICE.md](NOTICE.md).

## Yang Anda dapatkan

- HD: `rtsp://<pc-ini>:8554/<Nama>/hd` (sering HEVC 1080p)
- SD: `…/sd` (H.264)
- Semua kamera berbagi **satu** IP jembatan; hanya jalur yang berubah
- Pratinjau jika [VLC](https://www.videolan.org/) terpasang
- Bahasa: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## Batas yang jujur

- Tanpa ONVIF, tanpa RTSP asli di kamera
- Banyak model HD sekitar **10 fps** — itu kameranya
- VLC 3 sering hitam pada HEVC/RTSP; pakai Agent DVR / Frigate
- Rekam di NVR Anda, bukan di jembatan

Wilayah: Eropa Barat/Timur, AS Barat/Timur, Tiongkok, India.

## Pemasangan dalam 5 menit

1. Windows 10/11 **atau Arch Linux**
2. Akun Smart Life / Tuya Smart yang sudah melihat kameranya

Di Windows tidak perlu memasang Python, VLC, atau ffmpeg — semuanya di Setup.

Windows: `TuyaRtspBridge-Setup.exe` dari [Releases](../../releases) — berikutnya, berikutnya, selesai. Rincian: [docs/windows.md](docs/windows.md).  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

Masuk: buat QR → pindai di Smart Life → **konfirmasi** → salin `rtsp://127.0.0.1:8554/<Nama>/hd`.

Sesi: `%APPDATA%\TuyaRtspBridge\` (Windows) atau `~/.local/share/tuya-rtsp-bridge/` (Linux).

## Lisensi

Kode kami: MIT. Mesin bawaan: MIT, Copyright (c) 2025 seydx. Tidak terafiliasi dengan Tuya Inc.

Nama, data lokal, lisensi yang dibundel: [docs/legal.md](docs/legal.md).
