# 자주 묻는 질문

### 로그인 후 카메라 목록이 비어 있음
지역이 틀림. 독일어 앱의 «서유럽»은 **EU** (WE 아님).

### QR이 끝나지 않음
창을 연 채로 폰에서 **확인**.

### QR이 너무 작음 / 틈 / 스캔 불가 (Windows)
**1.2.4+** 수정: 고정 **320×320** 캔버스 (NEAREST). 앱 업데이트. Create QR 전 «No QR»은 정상.

### 연결 거부 (WinError 10061)
UI가 API (`:8787`)를 자동 시작. Create QR 재시도.

### VLC 검정
VLC 3는 HEVC/RTSP에서 자주 실패. 스트림은 살아 있음. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps를 기대함
많은 기종이 HD에서 약 **10 fps**.

### ONVIF인가?
아니오. RTSP만.

### 영상이 집 밖으로 나가나?
시그널링은 Tuya. 로컬은 보통 카메라→이 PC.

### LAN 밖 Cloud PTZ?
먼저 LAN PTZ (TCP **6668**). 원격은 email+password 한 번 (`POST /api/cloud/auth`) — IoT developer 키 불필요.

### Home Assistant 애드온?
예 — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). 호스트 네트워크. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). 데이터: `~/.local/share/tuya-rtsp-bridge/`.
