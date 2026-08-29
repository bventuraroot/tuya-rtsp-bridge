# Tuya RTSP 브리지

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**싼 Tuya / Smart Life / iSmartLife 카메라를 그냥 RTSP 카메라로 만든다.** Frigate, Agent DVR, go2rtc, Home Assistant, VLC용.

펌웨어는 안 깐다. ONVIF도 없다(순정에 원래 없음). QR 한 번 찍고 URL을 복사하면 된다.

| 누구냐면 | 여기부터 |
|---|---|
| 일단 돌아가게 | [5분이면 된다](#5분이면-된다) |
| 집 NVR | [docs/nvr.md](docs/nvr.md) |
| 개발 | [docs/architecture.md](docs/architecture.md) |

이 저장소에는 계정, 기기 ID, 집 IP가 **없다**.

## 왜 싼 카메라에 이게 필요한가

2만 원짜리 Smart Life 카메라는 IP 카메라처럼 생겼다. 아니다. 순정에는 **ONVIF 없고**, **RTSP 칸도 없다**. 화면은 제조사 앱과, 내가 못 만지는 클라우드를 탄다. 두 번째 폰이나 "클라우드 NVR"은 구독이거나, 유일한 라이브를 훔친다.

벽에 붙인 센서는 내가 산 거다. 녹화는 내 디스크에.

이 프로그램은 작은 로컬 다리. 쓰던 앱에서 QR을 읽는다. 그다음 각 카메라는 평범한 주소가 된다.

```
rtsp://<이-PC>:8554/<카메라이름>/hd
```

로그인 신호는 여전히 Tuya. 이 PC에서 볼 때 영상은 대개 LAN에 남는다. 긴 글: [docs/ko/why.md](docs/ko/why.md).

## 솔직한 한계

- ONVIF 없음, 카메라 자체 RTSP 없음
- HD는 대개 **초당 10장**. 앱이 깎는 게 아니다
- VLC 3는 HEVC/RTSP에서 검은 화면이 많다. Agent DVR / Frigate를 봐라
- 녹화는 NVR에서. 다리에 쌓지 마라

로그인 지역: 서유럽, 동유럽, 미국 서/동, 중국, 인도.

## 5분이면 된다

1. Windows 10/11과, 이미 카메라가 보이는 Smart Life 계정. Python, VLC, ffmpeg는 따로 안 깔아도 된다.
2. [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases)의 `TuyaRtspBridge-Setup.exe`. 다음, 다음, 마침. 설명: [docs/windows.md](docs/windows.md).
3. 앱 실행 → 폰과 같은 지역 → QR 만들기 → 앱에서 찍고 **확인**
4. HD 주소를 Agent DVR / Frigate에 붙인다: `rtsp://127.0.0.1:8554/<이름>/hd`

카메라 목록이 비면 대개 지역이 틀린 거다. QR이 안 끝나면 아직 확인을 안 한 거다. 기다려라.

데이터: `%APPDATA%\TuyaRtspBridge\`. 프로그램: `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## 라이선스

우리 코드는 MIT. 엔진은 MIT, Copyright (c) 2025 seydx. Tuya Inc.와는 무관하다.

이름, 로컬 데이터, 동봉 라이선스: [docs/legal.md](docs/legal.md).

## 1.2.4+ 신규

- QR 로그인: 고정 **320×320** 캔버스 (Windows 슬릿 버그 수정)
- **Home Assistant OS 애드온:** [homeassistant/tuya_rtsp_bridge/](homeassistant/tuya_rtsp_bridge/) (호스트 네트워크)
- Docker/HA: [docs/docker.md](docs/docker.md)
- PTZ: 먼저 LAN (TCP 6668), 선택 **클라우드 PTZ** (email/password 한 번) — IoT developer 키 불필요
- Protect 세션: 저장 비밀번호로 자동 재로그인

