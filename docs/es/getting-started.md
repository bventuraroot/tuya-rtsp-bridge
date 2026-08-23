# Primeros pasos

Funciona con cámaras que aparecen en **Tuya Smart**, **Smart Life** o **iSmartLife**.

1. Windows: `TuyaRtspBridge-Setup.exe` de Releases (incluye Python/VLC/ffmpeg). Linux: `./launch.sh`.
2. Abre **Tuya RTSP Bridge**.
3. Elige la misma región que en el teléfono.
4. Crear QR → escanear → **confirmar**.
5. Copia la URL HD en el NVR.

Sesiones: `%APPDATA%\TuyaRtspBridge` o `~/.local/share/tuya-rtsp-bridge/`.

Wi‑Fi nuevo: **no** borres las cámaras de la cuenta. Cambia la red en la app en el nuevo sitio, arranca el puente, cambia solo la IP del PC en el NVR.

PTZ: mantener una flecha = mover, soltar = parar. Protocolo local TCP **6668**.
