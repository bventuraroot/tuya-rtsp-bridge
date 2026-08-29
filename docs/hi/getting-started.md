# शुरू करें

**Tuya Smart**, **Smart Life** या **iSmartLife** में दिखने वाले कैमरे।

## पहली बार
1. Windows: Releases से Setup. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. **Tuya RTSP Bridge** चलाएँ (या `http://<host>:8787`).
3. फोन जैसा ही रीजन।
4. Create QR → स्कैन → **confirm**। QR **320×320**।
5. HD URL NVR में कॉपी करें।

## PTZ
UI तीर। **LAN:** TCP **6668**। **बाहर:** email+password एक बार (`POST /api/cloud/auth`) — बिना IoT keys।

## प्रीव्यू
Windows Setup = VLC. Linux = ffmpeg MJPEG. RTSP के लिए ज़रूरी नहीं।
