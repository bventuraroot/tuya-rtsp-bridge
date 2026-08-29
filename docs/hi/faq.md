# अक्सर पूछे जाने वाले प्रश्न

### लॉगिन के बाद कैमरा सूची खाली
गलत रीजन। जर्मन ऐप में «Western Europe» = **EU**, WE नहीं।

### QR पूरा नहीं होता
विंडो खुली रखें और फोन पर **confirm** करें।

### QR बहुत छोटा / स्लिट / स्कैन नहीं (Windows)
**1.2.4+** में ठीक: स्थिर **320×320** canvas (NEAREST)। ऐप अपडेट करें। Create QR से पहले «No QR» सामान्य है।

### कनेक्शन अस्वीकृत (WinError 10061)
UI API (`:8787`) खुद शुरू करता है। फिर Create QR।

### VLC काला
VLC 3 अक्सर HEVC/RTSP पर फेल। स्ट्रीम जीवित। Agent/Frigate। Linux: ffmpeg MJPEG।

### 60 fps चाहिए था
कई मॉडल HD में ~**10 fps** देते हैं।

### क्या यह ONVIF है?
नहीं। केवल RTSP।

### क्या वीडियो घर से बाहर जाता है?
सिग्नलिंग Tuya को। लोकल आमतौर पर कैमरा → यह PC।

### LAN के बाहर Cloud PTZ?
पहले LAN PTZ (TCP **6668**)। बाहर: एक बार email+password (`POST /api/cloud/auth`) — बिना IoT developer keys।

### Home Assistant add-on?
हाँ — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/)। Host network। Docker: [docker.md](../docker.md)।

### Linux / macOS?
`./launch.sh`। Arch: [arch-linux.md](../arch-linux.md)। डेटा: `~/.local/share/tuya-rtsp-bridge/`।
