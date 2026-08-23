# Arch Linux

Two ways. Both need a Tuya Smart / Smart Life account.

## A. From a git clone (fastest)

```bash
sudo pacman -S --needed python python-pip tk go vlc ffmpeg
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
chmod +x launch.sh
./launch.sh
```

`--server` starts only the API + RTSP engine (no GUI).

Data: `~/.local/share/tuya-rtsp-bridge/`  
Config: `~/.config/tuya-rtsp-bridge/config.json`

## B. PKGBUILD (system package)

Needs tag `v1.1.0` (or newer) on GitHub.

```bash
sudo pacman -S --needed base-devel go git
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge/packaging/arch
makepkg -si
tuya-rtsp-bridge
```

Headless + autostart for your user:

```bash
systemctl --user enable --now tuya-rtsp-bridge.service
```

Preview needs `vlc`. Watchdog probe needs `ffmpeg`.

## Wayland

The desktop preview uses libVLC + the Tk window id (`set_xwindow`). On pure Wayland, start the app with XWayland (`GDK`/Tk usually does this). RTSP itself does not need a display.
