#!/usr/bin/env bash
# Run from a git clone on Linux (Arch, Debian, …).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
export TUYA_BRIDGE_ROOT="$ROOT"
export PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}"

need() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing: $1"
    echo "Arch: sudo pacman -S python python-pip tk go vlc ffmpeg"
    exit 1
  fi
}

need python3

if [[ ! -x "$ROOT/.venv/bin/python" ]]; then
  python3 -m venv "$ROOT/.venv"
  "$ROOT/.venv/bin/pip" install -U pip
  "$ROOT/.venv/bin/pip" install -r "$ROOT/requirements.txt"
fi

ENG="$ROOT/bin/tuya-ipc-terminal"
if [[ ! -x "$ENG" ]]; then
  need go
  mkdir -p "$ROOT/bin"
  (cd "$ROOT/vendor/tuya-ipc-terminal" && go build -o "$ENG" .)
fi

if [[ "${1:-}" == "--server" || "${1:-}" == "--headless" ]]; then
  exec "$ROOT/.venv/bin/python" -u "$ROOT/src/server.py"
fi
exec "$ROOT/.venv/bin/python" -u "$ROOT/src/gui.py"
