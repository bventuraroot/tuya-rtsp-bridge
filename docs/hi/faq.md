# अक्सर पूछे जाने वाले प्रश्न

### लॉगिन के बाद सूची खाली
गलत रीजन। जर्मन ऐप में «Western Europe» = **EU**, WE नहीं।

### QR पूरा नहीं होता
विंडो खुली रखें और फोन पर **confirm** करें।

### QR स्लिट (Windows)
**1.2.4+** में ठीक: **320×320** canvas (NEAREST)। Setup अपडेट करें।

### WinError 10061
UI API `:8787` खुद शुरू करता है। Create QR दोबारा।

### VLC काला
स्ट्रीम जीवित। Agent/Frigate। Linux: ffmpeg MJPEG।

### 60 fps?
अक्सर ~**10 fps** HD।

### ONVIF?
नहीं। केवल RTSP।

### वीडियो घर से बाहर?
सिग्नलिंग Tuya को। लोकल: कैमरा → यह PC।

### go2rtc `tuya://`?
Email/password, QR नहीं।

### LAN के बाहर Cloud PTZ?
पहले LAN TCP **6668**। फिर `POST /api/cloud/auth`, `cloud_auth.json` mode 600।

### लॉगिन कहाँ?
`%APPDATA%\TuyaRtspBridge\` या `~/.local/share/tuya-rtsp-bridge/`।

### HA add-on?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/)। [docker.md](docker.md)।

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md)।
