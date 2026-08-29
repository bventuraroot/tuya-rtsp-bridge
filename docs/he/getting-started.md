# התחלה

מצלמות ב-**Tuya Smart**, **Smart Life** או **iSmartLife**.

## הרצה ראשונה
1. Windows: Setup מ-Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. הפעילו **Tuya RTSP Bridge** (או `http://<host>:8787`).
3. אותו אזור כמו בטלפון.
4. Create QR → סריקה → **אישור**. QR קבוע **320×320**.
5. העתיקו URL HD ל-NVR.

## PTZ
חצים ב-UI. **LAN:** TCP **6668**. **מחוץ לרשת:** cloud אחרי email+סיסמה (`POST /api/cloud/auth`) — בלי מפתחות IoT.

## תצוגה מקדימה
Windows Setup = VLC. Linux = ffmpeg MJPEG. RTSP לא צריך אותה.
