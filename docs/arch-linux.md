# Arch Linux / Garuda / Manjaro

Two ways. Both need a Tuya Smart / Smart Life account that already sees the cameras.

## A. System package (PKGBUILD) — recommended

```bash
sudo pacman -S --needed base-devel go
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge/packaging/arch
makepkg -si
tuya-rtsp-bridge
```

What you get:

| Path | Purpose |
|---|---|
| `/usr/bin/tuya-rtsp-bridge` | GUI (default) or `--server` headless |
| `/usr/lib/tuya-rtsp-bridge/` | App + RTSP engine binary |
| `~/.local/share/tuya-rtsp-bridge/` | Sessions / device data (never in git) |
| `~/.config/tuya-rtsp-bridge/config.json` | Config |

Headless + autostart for your user:

```bash
systemctl --user enable --now tuya-rtsp-bridge.service
```

Optional (preview + watchdog probe):

```bash
sudo pacman -S --needed vlc ffmpeg
```

`makepkg` pulls `tinytuya` and `python-vlc` as private wheels into the package (not global pip). Everything else is official `[extra]` packages.

Rebuild after a major Python bump:

```bash
cd packaging/arch && makepkg -si -f
```

## B. From a git clone (dev / no install)

```bash
sudo pacman -S --needed python python-pip tk go vlc ffmpeg
git clone https://github.com/DanEng1982/tuya-rtsp-bridge.git
cd tuya-rtsp-bridge
chmod +x launch.sh
./launch.sh            # GUI
./launch.sh --server   # headless API + RTSP only
```

Creates a local `.venv` and builds `bin/tuya-ipc-terminal` on first run.

## Wayland

Desktop preview uses libVLC + the Tk window id (`set_xwindow`). On pure Wayland, start under XWayland (Tk usually does). RTSP itself needs no display — use `--server` on a headless box or NVR host.

## Firewall

Open TCP **8554** (RTSP) and optionally **8787** (local HTTP API) if other LAN machines should reach this PC.

## Uninstall

```bash
sudo pacman -Rns tuya-rtsp-bridge
# optional user data:
# rm -rf ~/.local/share/tuya-rtsp-bridge ~/.config/tuya-rtsp-bridge
```
