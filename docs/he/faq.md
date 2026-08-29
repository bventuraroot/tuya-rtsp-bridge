# שאלות נפוצות

### רשימת המצלמות ריקה
אזור שגוי. «מערב אירופה» באפליקציה הגרמנית הוא **EU**, לא WE.

### ה-QR לא מסתיים
השאירו את החלון פתוח ו**אשרו** בטלפון.

### QR זעיר / חריץ / לא נסרק (Windows)
תוקן ב-**1.2.4+**: קנבס קבוע **320×320** (NEAREST). עדכנו את האפליקציה. «No QR» לפני Create QR הוא תקין.

### חיבור נדחה (WinError 10061)
ה-UI מפעיל את ה-API (`:8787`) לבד. נסו שוב Create QR.

### VLC שחור
VLC 3 נכשל לעיתים ב-HEVC/RTSP. הסטרים חי. Agent/Frigate. בלינוקס: ffmpeg MJPEG.

### ציפיתי ל-60 fps
דגמים רבים נותנים כ-**10 fps** ב-HD.

### זה ONVIF?
לא. רק RTSP.

### האם הווידאו יוצא מהבית?
סיגנלינג ל-Tuya. מקומית בדרך כלל מצלמה → המחשב הזה.

### Cloud PTZ מחוץ ל-LAN?
LAN PTZ (TCP **6668**) קודם. מרחוק: cloud אחרי email+סיסמה פעם אחת (`POST /api/cloud/auth`) — בלי מפתחות IoT developer.

### תוסף Home Assistant?
כן — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). נתונים: `~/.local/share/tuya-rtsp-bridge/`.
