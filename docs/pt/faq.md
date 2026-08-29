# Perguntas frequentes

### Lista de câmeras vazia
Região errada. «Europa Ocidental» na app DE = **EU** (`protect-eu`), não WE.

### O QR não termina
Mantenha a janela aberta e **confirme** no telemóvel.

### QR minúsculo / fenda (Windows)
Corrigido em **1.2.4+**: canvas fixo **320×320** (NEAREST). Atualize o Setup.

### Ligação recusada (WinError 10061)
A UI arranca a API (`:8787`) sozinha. Tente Create QR de novo.

### VLC preto
O stream vive. Agent/Frigate. Linux: ffmpeg MJPEG.

### 60 fps?
Muitas vezes ~**10 fps** HD.

### ONVIF?
Não. Só RTSP.

### O vídeo sai de casa?
Sinalização à Tuya. Local: câmara → este PC.

### go2rtc `tuya://`?
Email/password Tuya Smart, não QR Smart Life.

### Cloud PTZ fora da LAN?
LAN TCP **6668** primeiro. Remoto: `POST /api/cloud/auth` → `cloud_auth.json` mode 600. Sem chaves IoT developer.

### Onde está o login?
`%APPDATA%\TuyaRtspBridge\` ou `~/.local/share/tuya-rtsp-bridge/`.

### Add-on Home Assistant?
[`homeassistant/tuya_rtsp_bridge/`](../../homeassistant/tuya_rtsp_bridge/). [docker.md](docker.md).

### Linux?
`./launch.sh` · [arch-linux.md](../arch-linux.md).
