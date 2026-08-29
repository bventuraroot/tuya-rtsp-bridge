# Perguntas frequentes

### Lista de câmeras vazia
Região errada. «Europa Ocidental» na app DE = **EU**, não WE.

### O QR não termina
Mantenha a janela aberta e **confirme** no telemóvel.

### QR minúsculo / fenda / ilegível (Windows)
Corrigido em **1.2.4+**: canvas fixo **320×320** (NEAREST). Atualize a app. «No QR» antes de Create QR é normal.

### Ligação recusada (WinError 10061)
A UI arranca a API (`:8787`) sozinha. Tente Create QR de novo.

### VLC preto
VLC 3 falha frequentemente em HEVC/RTSP. O stream vive. Agent/Frigate. Linux: pipe MJPEG ffmpeg.

### Esperava 60 fps
Muitos modelos dão ~**10 fps** em HD.

### É ONVIF?
Não. Só RTSP.

### O vídeo sai de casa?
Sinalização para a Tuya. Em local costuma ser câmara → este PC.

### Cloud PTZ fora da LAN?
Primeiro PTZ LAN (TCP **6668**). Remoto: cloud após email+password uma vez (`POST /api/cloud/auth`) — sem chaves IoT developer.

### Add-on Home Assistant?
Sim — [`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). Host network. Docker: [docker.md](../docker.md).

### Linux / macOS?
`./launch.sh`. Arch: [arch-linux.md](../arch-linux.md). Dados: `~/.local/share/tuya-rtsp-bridge/`.
