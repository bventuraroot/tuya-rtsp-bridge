# Legal notes

This is not a lawyer letter. It is how this project is meant to be used.

## What this software is

A local helper on **your** PC. You scan a QR in Smart Life / Tuya Smart / iSmartLife, then this machine offers RTSP on your LAN.

It is **not** an official Tuya product. Tuya, Smart Life, iSmartLife, and related logos belong to their owners. We use those names only to say which cameras the tool talks to.

The phone login still goes through Tuya’s servers. Their terms apply to **your** account. If that is not acceptable, do not scan.

## What we do not do

- No telemetry, no crash phone-home, no ads
- No accounts, device IDs, or video in git or in the Setup
- Session cookies and the camera list stay in `%APPDATA%\TuyaRtspBridge\` (Windows) or `~/.local/share/tuya-rtsp-bridge/` (Linux)
- We do not flash firmware and we do not claim ONVIF

## Your data

This program does not operate a cloud. Whatever Tuya already sees (login, signaling) they still see. Video you watch through this PC usually stays camera → this PC on the LAN. A phone on mobile data is a second viewer and uses Tuya’s path.

Delete the data folder to wipe the local session.

## Licenses in the Windows Setup

Our code is MIT. The RTSP engine is MIT (seydx). Details and full texts: [NOTICE.md](../NOTICE.md), [DEPENDENCIES.md](../DEPENDENCIES.md).

The Setup also copies **unmodified** third-party binaries next to the app (not statically linked into our Python):

| Binary | License of that binary | Corresponding source |
|---|---|---|
| Official VideoLAN VLC 3 (win64 zip) | GPL-2.0 for the player; libVLC is LGPL-2.1+ | https://www.videolan.org |
| ffmpeg 9.0.1 essentials (Gyan, `--enable-gpl`) | GPL-3.0 | https://ffmpeg.org and https://www.gyan.dev/ffmpeg/builds/ |
| Private CPython 3.12 | PSF | https://www.python.org |

ffmpeg is started as its own process. VLC is loaded as `libvlc` for the optional preview. You may replace either binary with another official build.

Inno Setup is only the compiler that builds the Setup.exe. It is not shipped as a library. This project is given away (MIT, no paid edition).

## Warranty

MIT: as-is. No promise that a given camera, region, or Tuya API change will keep working. Recording belongs in your NVR.

## Contact

Issues and security: the GitHub repo. Do not send cookies, `localKey`, or live video.
