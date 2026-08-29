# 자주 묻는 질문

### 로그인 후 목록이 비어 있음
지역 오류. 독일어 앱 «서유럽» = **EU**, WE 아님.

### QR이 끝나지 않음
창을 연 채 폰에서 **확인**.

### QR 슬릿 (Windows)
**1.2.4+** 수정: 고정 **320×320** 캔버스 (NEAREST). Setup 업데이트.

### WinError 10061
UI가 API `:8787` 자동 시작. Create QR 재시도.

### VLC 검정
스트림은 살아 있음. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps?
많은 기종 HD 약 **10 fps**.

### ONVIF?
아니오. RTSP만.

### 영상이 집 밖으로?
시그널링은 Tuya. 로컬은 보통 카메라→이 PC.

### go2rtc `tuya://`?
Tuya Smart email/password. Smart Life QR 아님.

### LAN 밖 Cloud PTZ?
먼저 LAN TCP **6668**. 원격: `POST /api/cloud/auth`, `cloud_auth.json` mode 600.

### 로그인 위치
`%APPDATA%\TuyaRtspBridge\` 또는 `~/.local/share/tuya-rtsp-bridge/`.

### HA 애드온?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). [docker.md](docker.md).

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md).
