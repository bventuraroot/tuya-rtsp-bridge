# 시작하기

**Tuya Smart**, **Smart Life**, **iSmartLife**에 보이는 카메라면 된다. 상자 브랜드(LSC, Nous, BlitzWolf, 이름 없는 "Tuya")는 상관없다. 폰 앱이 그중 하나면 된다.

1. Windows: Releases의 `TuyaRtspBridge-Setup.exe` (Python/VLC/ffmpeg 포함). Linux: `./launch.sh`.
2. **Tuya RTSP 브리지**를 켠다.
3. 폰 앱과 같은 지역을 고른다.
4. QR 만들기 → 찍기 → 폰에서 **확인**.
5. HD 주소를 NVR에 붙인다.

세션은 재부팅 뒤에도 남는다(`%APPDATA%\TuyaRtspBridge`). Tuya가 차기 전까지 다시 찍을 필요 없다.

이사: 계정에서 카메라를 지우지 않고 초기화하지 않으면 기기 ID는 같다. 새 SSID는 가서 앱으로. NVR에서는 PC IP만 바꾼다. 경로는 그대로.

PTZ: 화살표를 누르고 있는 동안만 움직인다. 손을 떼면 멈춘다. 클라우드가 아니라 LAN TCP 6668. 모든 기종에 있는 건 아니다.
