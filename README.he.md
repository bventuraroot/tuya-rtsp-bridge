# גשר RTSP של Tuya

<p align="center">
  <img src="docs/images/logo.png" width="128" alt="Tuya RTSP Bridge">
</p>

<div dir="rtl" lang="he">

[![רישיון: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![English](README.md)](README.md) [![Deutsch](README.de.md)](README.de.md) [![Nederlands](README.nl.md)](README.nl.md) [![Français](README.fr.md)](README.fr.md) [![Español](README.es.md)](README.es.md) [![Português](README.pt.md)](README.pt.md) [![Italiano](README.it.md)](README.it.md) [![Polski](README.pl.md)](README.pl.md) [![Čeština](README.cs.md)](README.cs.md) [![Русский](README.ru.md)](README.ru.md) [![Українська](README.uk.md)](README.uk.md) [![Bahasa Indonesia](README.id.md)](README.id.md) [![简体中文](README.zh.md)](README.zh.md) [![हिन्दी](README.hi.md)](README.hi.md) [![日本語](README.ja.md)](README.ja.md) [![한국어](README.ko.md)](README.ko.md) [![עברית](README.he.md)](README.he.md) [![ייִדיש](README.yi.md)](README.yi.md)

**מצלמות Tuya / Smart Life / iSmartLife זולות הופכות למצלמות RTSP רגילות.** ל-Frigate, Agent DVR, go2rtc, Home Assistant או VLC.

בלי לפרוץ קושחה. בלי ONVIF (בקושחה המקורית אין דבר כזה). סורקים QR פעם אחת ומעתיקים כתובת.

| מי אתם | התחלה |
|---|---|
| רק שזה יעבוד | [בחמש דקות](#בחמש-דקות) |
| NVR בבית | [docs/nvr.md](docs/nvr.md) |
| מפתחים | [docs/architecture.md](docs/architecture.md) |

במאגר **אין** חשבונות, מזהי מכשירים או כתובות בית.

## למה המצלמות הזולות צריכות את זה

מצלמת Smart Life ב־80 שקל נראית כמו מצלמת IP. היא לא. בקושחה המקורית **אין ONVIF** ו**אין תיבת RTSP**. השידור חי דרך האפליקציה של היצרן וענן שאתם לא שולטים בו. טלפון שני או "NVR בענן" זה בדרך כלל מנוי — או גניבת הסשן החי היחיד.

שילמתם על חיישן על *הקיר שלכם*. ההקלטה שייכת ל*דיסק שלכם*.

התוכנית הזאת היא גשר מקומי קטן. קוראים QR באפליקציה שכבר יש. אחר כך לכל מצלמה יש כתובת רגילה:

</div>

```
rtsp://<המחשב-הזה>:8554/<שם-המצלמה>/hd
```

<div dir="rtl" lang="he">

הכניסה נשארת אצל Tuya. כשצופים מהמחשב הזה, הווידאו נשאר בדרך כלל ברשת הבית. הטקסט הארוך: [docs/he/why.md](docs/he/why.md).

## גבולות ישרים

- אין ONVIF, אין RTSP מובנה במצלמה
- הרבה דגמים מוציאים בערך **10 פריימים לשנייה** ב-HD — זו המצלמה
- VLC 3 לעתים קרובות שחור ב-HEVC/RTSP; Agent DVR / Frigate הם הלקוחות הנכונים
- מקליטים ב-NVR, לא על הגשר

אזורי כניסה: מערב אירופה, מזרח אירופה, מערב/מזרח ארה״ב, סין, הודו.

## בחמש דקות

1. Windows 10/11 וחשבון Smart Life שכבר רואה את המצלמות. בלי Python, VLC או ffmpeg בנפרד.
2. `TuyaRtspBridge-Setup.exe` מ-[Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). הבא, הבא, סיום. פירוט: [docs/windows.md](docs/windows.md).
3. מפעילים את האפליקציה → אותו אזור כמו בטלפון → יוצרים QR → סורקים ומאשרים
4. מדביקים את כתובת ה-HD ב-Agent DVR / Frigate: `rtsp://127.0.0.1:8554/<שם>/hd`

רשימת מצלמות ריקה = לרוב אזור לא נכון. ה-QR "לא עושה כלום" = עוד לא אישרתם. מחכים.

נתונים: `%APPDATA%\TuyaRtspBridge\`. תוכנית: `%LOCALAPPDATA%\Programs\TuyaRtspBridge`.

## רישיון

הקוד שלנו MIT. המנוע MIT, Copyright (c) 2025 seydx. לא קשור ל-Tuya Inc.

</div>

שמות, נתונים מקומיים, רישיונות מצורפים: [docs/legal.md](docs/legal.md).

## חדש ב-1.2.4+

- כניסת QR: קנבס קבוע **320×320** (תוקן באג הסדק ב-Windows)
- **תוסף Home Assistant OS:** [homeassistant/tuya_rtsp_bridge/](homeassistant/tuya_rtsp_bridge/) (host network)
- Docker/HA: [docs/docker.md](docs/docker.md)
- PTZ: קודם LAN (TCP 6668), אופציונלי **cloud PTZ** אחרי email/סיסמה — בלי מפתחות IoT developer
- סשן protect: התחברות מחדש אוטומטית עם סיסמה שמורה

