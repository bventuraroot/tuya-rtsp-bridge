# 시작하기

**Tuya Smart**, **Smart Life**, **iSmartLife**에 보이는 카메라.

## 첫 실행
1. Windows: Releases Setup. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. **Tuya RTSP Bridge** 실행 (또는 `http://<host>:8787`).
3. 폰과 같은 지역.
4. Create QR → 스캔 → **확인**. QR **320×320**.
5. HD URL을 NVR에 복사.

## PTZ
UI 화살표. **LAN:** TCP **6668**. **원격:** email+password 한 번 (`POST /api/cloud/auth`) — IoT 키 불필요.

## 미리보기
Windows Setup = VLC. Linux = ffmpeg MJPEG. RTSP에는 필요 없음.
