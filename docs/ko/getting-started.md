# 시작하기

**Tuya Smart** / **Smart Life** / **iSmartLife**.

## 첫 실행
1. Windows Setup: [Releases](https://github.com/DanEng1982/tuya-rtsp-bridge/releases). Linux: `./launch.sh`. Docker/HA: [docker.md](docker.md).
2. **Tuya RTSP Bridge** 또는 `http://<host>:8787`.
3. 폰과 같은 지역.
4. Create QR → 스캔 → **확인**. QR **320×320**.
5. HD URL을 NVR에 복사.

세션: `%APPDATA%\TuyaRtspBridge` / `~/.local/share/tuya-rtsp-bridge/`.

## 이사 / 새 Wi‑Fi
계정에서 카메라 삭제 금지. 앱에서 새 SSID, 새 LAN에서 bridge, NVR은 PC IP만 변경.

## PTZ / 미리보기 / 자동 시작
LAN **TCP 6668**; cloud: `POST /api/cloud/auth`. Windows VLC; Linux ffmpeg MJPEG.
