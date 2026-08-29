# टुया RTSP ब्रिज

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**किसी भी टुया / Smart Life / iSmartLife कैमरे को सामान्य RTSP कैमरा बनाएँ** — Frigate, Agent DVR, go2rtc, Home Assistant या VLC के लिए।

कोई फर्मवेयर फ्लैश नहीं। स्टॉक फर्मवेयर पर **ONVIF नहीं** है। एक बार QR स्कैन करें, फिर RTSP पता कॉपी करें।

| आप हैं… | यहाँ से शुरू करें |
|---|---|
| बस चलाना है | [५ मिनट में सेटअप](#५-मिनट-में-सेटअप) |
| होम-लैब / NVR | [docs/nvr.md](docs/nvr.md) |
| डेवलपर | [docs/architecture.md](docs/architecture.md) |

इस रिपॉजिटरी में **कोई** खाता, डिवाइस ID या घर का IP नहीं है।

## सस्ते टुया कैमरों को इसकी ज़रूरत क्यों है

२०–४० यूरो वाले «Smart Life» कैमरे IP कैमरे जैसे दिखते हैं। हैं नहीं। स्टॉक फर्मवेयर: **कोई ONVIF नहीं**, **कोई RTSP विकल्प नहीं**। लाइव व्यू कंपनी के ऐप और उस क्लाउड से जाता है जिसे आप नहीं चलाते। दूसरा फ़ोन या «क्लाउड NVR» अक्सर सदस्यता माँगता है — या अकेली लाइव सेशन चुरा लेता है।

सेंसर **आपकी** दीवार पर है। रिकॉर्डिंग **आपकी** डिस्क पर जानी चाहिए।

यह ऐप एक छोटा स्थानीय ब्रिज है: उसी ऐप में QR स्कैन करें जो आपके पास पहले से है। उसके बाद हर कैमरे का सामान्य पता:

```
rtsp://<यह-पीसी>:8554/<कैमरानाम>/hd
```

सिग्नलिंग टुया पर रहती है। इस पीसी से देखने पर वीडियो आमतौर पर LAN पर रहता है। पूरा लेख: [docs/hi/why.md](docs/hi/why.md)।

### ऐप कैसी दिखती है

पहली बार — भाषा, क्षेत्र, QR, Smart Life में पुष्टि:

![स्वागत स्क्रीन। खाली सूची, अभी QR नहीं, केवल localhost।](docs/images/ui-welcome.png)

लॉगिन के बाद — केवल डेमो नाम। दस्तावेज़ में पूर्वावलोकन जानबूझकर काला है (कोई लाइव चित्र नहीं):

![दो प्लेसहोल्डर कैमरे, HD RTSP 127.0.0.1 पर।](docs/images/ui-ready.png)

## श्रेय

RTSP इंजन **[seydx](https://github.com/seydx)** का **[tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal)** है (MIT, कमिट `d65b3e9`)। देखें [CREDITS.md](CREDITS.md), [NOTICE.md](NOTICE.md)।

## आपको क्या मिलता है

- HD: `rtsp://<यह-पीसी>:8554/<नाम>/hd` (अक्सर HEVC 1080p)
- SD: `…/sd` (H.264)
- सभी कैमरे **एक** ब्रिज IP साझा करते हैं; केवल पथ बदलता है
- पूर्वावलोकन के लिए [VLC](https://www.videolan.org/)
- भाषाएँ: English, Deutsch, Nederlands, Français, Español, Português, Italiano, Polski, Čeština, Русский, Українська, Bahasa Indonesia, 简体中文, हिन्दी

## ईमानदार सीमाएँ

- ONVIF नहीं, कैमरे पर मूल RTSP नहीं
- कई मॉडल HD में लगभग **10 fps** देते हैं — यह कैमरा है
- VLC 3 पर HEVC/RTSP अक्सर काला; Agent DVR / Frigate इस्तेमाल करें
- रिकॉर्डिंग आपके NVR पर हो, ब्रिज पर नहीं

लॉगिन क्षेत्र: पश्चिमी/पूर्वी यूरोप, USA पश्चिम/पूर्व, चीन, भारत।

## ५ मिनट में सेटअप

1. Windows 10/11 **या Arch Linux**
2. Smart Life / Tuya Smart खाता जिसमें कैमरे पहले से दिखते हैं

Windows पर अलग से Python, VLC या ffmpeg नहीं चाहिए — Setup में है।

Windows: [Releases](../../releases) से `TuyaRtspBridge-Setup.exe` — अगला, अगला, समाप्त। विवरण: [docs/windows.md](docs/windows.md)।  
Arch: [docs/arch-linux.md](docs/arch-linux.md) — `./launch.sh`

लॉगिन: QR बनाएँ → Smart Life से स्कैन → **पुष्टि** → `rtsp://127.0.0.1:8554/<नाम>/hd` कॉपी करें।

सत्र: Windows पर `%APPDATA%\TuyaRtspBridge\`, Linux पर `~/.local/share/tuya-rtsp-bridge/`।

## लाइसेंस

हमारा कोड: MIT। वेंडर इंजन: MIT, Copyright (c) 2025 seydx। Tuya Inc. से संबद्ध नहीं।

नाम, स्थानीय डेटा, बंडल लाइसेंस: [docs/legal.md](docs/legal.md)।

## 1.2.4+ में नया

- QR लॉगिन: स्थिर **320×320** canvas (Windows स्लिट बग ठीक)
- **Home Assistant OS add-on:** [homeassistant/tuya_rtsp_bridge/](homeassistant/tuya_rtsp_bridge/) (host network)
- Docker/HA: [docs/docker.md](docs/docker.md)
- PTZ: पहले LAN (TCP 6668), वैकल्पिक **cloud PTZ** email/password के बाद — बिना IoT developer keys
- Protect सत्र: सहेजे पासवर्ड से auto-relogin

