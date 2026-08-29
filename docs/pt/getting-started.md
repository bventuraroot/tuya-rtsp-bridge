# Primeiros passos

Câmeras em **Tuya Smart**, **Smart Life** ou **iSmartLife**.

## Primeira execução
1. Windows: Setup dos Releases. Linux: `./launch.sh` / Arch. Docker/HA: [docker.md](../docker.md).
2. Inicie **Tuya RTSP Bridge** (ou `http://<host>:8787`).
3. Mesma região do telemóvel.
4. Create QR → ler → **confirmar**. QR fixo **320×320**.
5. Copie o URL HD para o NVR.

## PTZ
Setas na UI. **LAN:** TCP **6668**. **Fora da rede:** cloud após email+password uma vez (`POST /api/cloud/auth`) — sem chaves IoT.

## Pré-visualização
Windows Setup = VLC. Linux = ffmpeg MJPEG. O RTSP não precisa dela.
