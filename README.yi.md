# Tuya RTSP בריק

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

<div dir="rtl" lang="yi">

[![ליצענץ: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**ביליקע Tuya- / Smart Life- / iSmartLife-קאַמערעס ווערן אַ נאָרמאַלע RTSP-קאַמערע.** פֿאַר Frigate, Agent DVR, go2rtc, Home Assistant אָדער VLC.

קיין פֿירמווער-פֿלעש. קיין ONVIF (אויפֿן אָריגינעלן פֿירמווער איז דאָס נישטאָ). איין מאָל אַ QR סקאַנירן, דערנאָך אַ URL קאָפּירן.

| ווער איר זענט | דאָ אָנהייבן |
|---|---|
| ס׳זאָל פּשוט גיין | [אין 5 מינוט](#אין-5-מינוט) |
| היים-NVR | [docs/nvr.md](docs/nvr.md) |
| אַנטוויקלער | [docs/architecture.md](docs/architecture.md) |

אין דעם רעפּאָ זענען **נישטאָ** קיין חשבונות, קיין אַפּאַראַט-IDס און קיין היים-IPס.

## פֿאַרוואָס די ביליקע קאַמערעס דאַרפֿן דאָס

אַ Smart Life-קאַמערע פֿאַר אַ פּאָר צענדליק אייראָ זעט אויס ווי אַן IP-קאַמערע. זי איז עס נישט. אויפֿן אָריגינעלן פֿירמווער: **קיין ONVIF**, **קיין RTSP-קעסטל**. דער לעבעדיקער בילד גייט דורך דער פֿאַבריקאַנט-אַפּ און אַ וואָלקן וואָס איר קאָנטראָלירט נישט. אַ צווייט טעלעפֿאָן אָדער אַ „וואָלקן-NVR“ הייסט אָפֿט אַן אַבאָנעמענט — אָדער עס גנבֿעט די איינציקע לעבעדיקע סעסיע.

איר האָט באַצאָלט פֿאַר אַ סענסאָר אויף *אײַער* וואַנט. רעקאָרדירן געהערט אויף *אײַער* דיסק.

דאָס פּראָגראַם איז אַ קליינע לאָקאַלע בריק. מע לייענט אַ QR אין דער אַפּ וואָס איר האָט שוין. דערנאָך האָט יעדע קאַמערע אַ נאָרמאַלן אַדרעס:

</div>

```
rtsp://<דער-קאָמפּיוטער>:8554/<קאַמערע-נאָמען>/hd
```

<div dir="rtl" lang="yi">

די אַרײַנלאָגין-סיגנאַלן בלײַבן בײַ Tuya. ווען מע קוקט פֿון דעם קאָמפּיוטער, בלײַבט דאָס ווידעאָ מערסטנס אויפֿן היים-נעץ. לענגער: [docs/yi/why.md](docs/yi/why.md).

## ערלעכע גרענעצן

- קיין ONVIF, קיין אייגן RTSP אויף דער קאַמערע
- אַ סך מאָדעלן גיבן בערך **10 בילדער אַ סעקונדע** אין HD — דאָס איז די קאַמערע
- VLC 3 ווײַזט HEVC/RTSP אָפֿט שוואַרץ; Agent DVR / Frigate זענען די ריכטיקע קליענטן
- רעקאָרדירן טוט דער NVR, נישט די בריק

לאָגין-ראַיאָנען: מערב־אייראָפּע, מיזרח־אייראָפּע, אַמעריקע מערב/מיזרח, כינע, אינדיע.

## אין 5 מינוט

1. Windows 10/11 און אַ Smart Life-חשבון וואָס זעט שוין די קאַמערעס. קיין באַזונדער Python, VLC אָדער ffmpeg.
2. `TuyaRtspBridge-Setup.exe` פֿון [Releases](../../releases). ווײַטער, ווײַטער, פֿאַרטיק. פּרטים: [docs/windows.md](docs/windows.md).
3. עפֿענען די אַפּ → דער זעלבער ראַיאָן ווי אויפֿן טעלעפֿאָן → מאַכן אַ QR → סקאַנירן און **באַשטעטיקן**
4. קלעפּן דעם HD-אַדרעס אין Agent DVR / Frigate: `rtsp://127.0.0.1:8554/<נאָמען>/hd`

אַ ליידיקע רשימה = אָפֿט דער פֿאַלשער ראַיאָן. דער QR „טוט גאָרנישט“ = נאָך נישט באַשטעטיקט. וואַרטן.

דאַטן: `%APPDATA%\TuyaRtspBridge\`. פּראָגראַם: `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## ליצענץ

אונדזער קאָד: MIT. דער מאָטאָר: MIT, Copyright (c) 2025 seydx. נישט פֿאַרבונדן מיט Tuya Inc.

</div>

נעמען, לאָקאַלע דאַטן, בײַגעלייגטע ליצענצן: [docs/legal.md](docs/legal.md).

## נײַ אין 1.2.4+

- QR לאָגין: פֿיקסירט **320×320** קאַנוועס (Windows שפּאַלט־באַג פֿאַרריכט)
- **Home Assistant OS add-on:** [homeassistant/tuya_rtsp_bridge/](homeassistant/tuya_rtsp_bridge/) (host network)
- Docker/HA: [docs/docker.md](docs/docker.md)
- PTZ: ערשט LAN (TCP 6668), אָפּציאָנעל **cloud PTZ** נאָך email/פּאַראָל — אָן IoT developer keys
- Protect סעסיע: auto-relogin מיט געהיטן פּאַראָל

