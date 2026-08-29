# שאלות נפוצות

### רשימת מצלמות ריקה
אזור שגוי. «מערב אירופה» באפליקציה הגרמנית = **EU**, לא WE.

### ה-QR לא מסתיים
השאירו חלון פתוח ו**אשרו** בטלפון.

### QR סדק (Windows)
תוקן ב-**1.2.4+**: קנבס **320×320** (NEAREST). עדכנו Setup.

### WinError 10061
ה-UI מפעיל API `:8787` לבד. נסו Create QR שוב.

### VLC שחור
הסטרים חי. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps?
לעיתים קרובות ~**10 fps** HD.

### ONVIF?
לא. רק RTSP.

### האם הווידאו יוצא מהבית?
סיגנלינג ל-Tuya. מקומית: מצלמה → המחשב הזה.

### go2rtc `tuya://`?
Email/סיסמה של Tuya Smart, לא QR של Smart Life.

### Cloud PTZ מחוץ ל-LAN?
קודם LAN TCP **6668**. מרחוק: `POST /api/cloud/auth`, `cloud_auth.json` mode 600.

### איפה הלוגין?
`%APPDATA%\TuyaRtspBridge\` או `~/.local/share/tuya-rtsp-bridge/`.

### תוסף HA?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). [docker.md](docker.md).

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md).
