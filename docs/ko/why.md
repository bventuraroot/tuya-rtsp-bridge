# 왜 만들었나

싼 Tuya / Smart Life / iSmartLife 카메라는 사기 쉽다. 진짜로 *갖는* 건 귀찮다.

상자에는 IP 카메라처럼 보인다. 쓸 만한 기능은 제조사 클라우드 뒤에 잠겨 있다.

- 순정에 **ONVIF가 없다**
- Frigate나 Agent DVR에 붙여 넣을 **카메라 자체 RTSP도 없다**
- 공식 앱은 계정, 폰, 내가 못 만지는 서버를 요구한다
- 두 번째 폰이나 "클라우드 NVR"은 구독이거나, 유일한 라이브를 훔친다

벽에 붙인 센서는 내가 산 거다. 녹화는 내 디스크에.

**Tuya RTSP 브리지**는 작은 로컬 프로그램이다. 쓰던 앱에서 QR을 한 번 읽는다. 그다음 각 카메라는 평범한 주소가 된다.

```
rtsp://<이-PC>:8554/<카메라이름>/hd
```

신호(로그인)는 여전히 Tuya. 이 PC에서 볼 때 영상은 대개 카메라 → 이 기계 LAN에 남는다. 싼 하드웨어, 집 녹화. 그게 목적이다.

## 이게 아닌 것

- 펌웨어 플래시도, 탈옥도, ONVIF도 아니다
- 60fps 약속이 아니다. 많은 기종은 HD HEVC로 **초당 10장**. 카메라 이야기다
- 폰 앱을 죽이는 것도 아니다. NVR용 *로컬* 길이다
- Tuya Inc.와는 무관하다. 엔진은 [seydx/tuya-ipc-terminal](https://github.com/seydx/tuya-ipc-terminal) (MIT)

다음: [getting-started.md](getting-started.md) · [FAQ](faq.md)
