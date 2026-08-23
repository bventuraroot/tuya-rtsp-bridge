# Primi passi

Funziona con le telecamere visibili in **Tuya Smart**, **Smart Life** o **iSmartLife**.

1. Windows: `TuyaRtspBridge-Setup.exe` da Releases (include Python/VLC/ffmpeg). Linux: `./launch.sh`.
2. Avvia **Tuya RTSP Bridge**.
3. Scegli la stessa regione del telefono.
4. Crea QR → scansiona → **conferma**.
5. Copia l’URL HD nel NVR.

Sessioni: `%APPDATA%\TuyaRtspBridge` o `~/.local/share/tuya-rtsp-bridge/`.

Nuova Wi‑Fi: **non** cancellare le telecamere dall’account. Cambia la rete nell’app sul posto, avvia il ponte, cambia solo l’IP del PC nel NVR.

PTZ: tieni premuta una freccia = muovi, rilascia = stop. Protocollo locale TCP **6668**.
