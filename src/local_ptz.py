"""Lokale PTZ-Steuerung über Tuya-DPs (Port 6668). Keine Keys loggen."""
from __future__ import annotations

import json
import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Optional

import tinytuya

DIR = {
    "up": "0",
    "upright": "1",
    "right": "2",
    "downright": "3",
    "down": "4",
    "downleft": "5",
    "left": "6",
    "upleft": "7",
}
PTZ_DP = "119"
STOP_DP = "116"
LAN_CACHE = "lan.json"
VERS = (3.5, 3.4, 3.3)


def _local_ipv4() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()


def _scan_6668(prefix: str | None = None) -> list[str]:
    if not prefix:
        ip = _local_ipv4()
        parts = ip.split(".")
        if len(parts) != 4 or parts[0] in ("127",):
            return []
        prefix = ".".join(parts[:3]) + "."
    found: list[str] = []

    def chk(i: int) -> Optional[str]:
        ip = f"{prefix}{i}"
        s = socket.socket()
        s.settimeout(0.35)
        try:
            if s.connect_ex((ip, 6668)) == 0:
                return ip
        except Exception:
            return None
        finally:
            s.close()
        return None

    with ThreadPoolExecutor(max_workers=64) as ex:
        for ip in ex.map(chk, range(1, 255)):
            if ip:
                found.append(ip)
    return found


class LocalPtz:
    def __init__(self, data_dir: Path, tuya_client) -> None:
        self.data_dir = data_dir
        self.client = tuya_client
        self._lock = threading.Lock()
        self._map: dict[str, dict] = {}
        self._load_cache()

    def _load_cache(self) -> None:
        p = self.data_dir / LAN_CACHE
        if not p.exists():
            return
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                self._map = {
                    k: v for k, v in data.items() if isinstance(v, dict) and v.get("ip")
                }
        except Exception:
            self._map = {}

    def _save_cache(self) -> None:
        out = {did: {"ip": v["ip"], "version": v["version"]} for did, v in self._map.items() if v.get("ip")}
        (self.data_dir / LAN_CACHE).write_text(json.dumps(out, indent=2), encoding="utf-8")

    def _local_key(self, device_id: str) -> str:
        body = self.client._post(
            "/api/jarvis/config",
            payload={"devId": device_id, "clientTraceId": "ptz"},
            referer="/playback",
        )
        key = (body.get("result") or {}).get("localKey") or ""
        if not key:
            raise RuntimeError("kein localKey")
        return key

    def _probe(self, device_id: str, ip: str, key: str, ver: float) -> bool:
        d = tinytuya.Device(device_id, ip, key, version=ver)
        d.set_socketTimeout(3)
        try:
            st = d.status()
        except Exception:
            return False
        if not isinstance(st, dict):
            return False
        if st.get("Error") or st.get("Err"):
            return False
        return "dps" in st or "DPS" in st

    def ensure(self, device_id: str) -> dict:
        with self._lock:
            hit = self._map.get(device_id)
            if hit and hit.get("ip") and hit.get("key") and hit.get("version"):
                return hit
            cached_ip = (hit or {}).get("ip")
            cached_ver = (hit or {}).get("version")
        key = self._local_key(device_id)
        me = _local_ipv4()
        same = lambda ip: ip and ip.rsplit(".", 1)[0] == me.rsplit(".", 1)[0]
        if cached_ip and not same(cached_ip):
            cached_ip = None
        if cached_ip:
            vers = (cached_ver,) if cached_ver else VERS
            for ver in vers:
                if self._probe(device_id, cached_ip, key, float(ver)):
                    rec = {"ip": cached_ip, "version": float(ver), "key": key}
                    with self._lock:
                        self._map[device_id] = rec
                        self._save_cache()
                    return rec
        with self._lock:
            ips: list[str] = []
            hit = self._map.get(device_id) or {}
            if hit.get("ip"):
                ips.append(hit["ip"])
            ips.extend(v.get("ip") for v in self._map.values() if v.get("ip") and v.get("ip") not in ips)
        scanned = _scan_6668()
        for ip in scanned:
            if ip not in ips:
                ips.append(ip)
        last = ""
        for ip in ips:
            for ver in VERS:
                if self._probe(device_id, ip, key, ver):
                    rec = {"ip": ip, "version": ver, "key": key}
                    with self._lock:
                        self._map[device_id] = rec
                        self._save_cache()
                    return rec
                last = f"{ip} v{ver}"
        raise RuntimeError(f"Kamera {device_id} nicht auf LAN (letzter Versuch {last})")

    def warmup(self, device_ids: list[str]) -> None:
        def run() -> None:
            for did in device_ids:
                try:
                    self.ensure(did)
                except Exception:
                    pass

        threading.Thread(target=run, daemon=True).start()

    def _device(self, device_id: str):
        rec = self.ensure(device_id)
        d = tinytuya.Device(device_id, rec["ip"], rec["key"], version=rec["version"])
        d.set_socketTimeout(5)
        return d

    def move(self, device_id: str, direction: str) -> dict:
        direction = (direction or "").lower().strip()
        if direction == "stop":
            return self.stop(device_id)
        if direction not in DIR:
            raise ValueError(f"unbekannte Richtung {direction}")
        d = self._device(device_id)
        res = d.set_value(PTZ_DP, DIR[direction])
        return {"via": "lan", "dp": PTZ_DP, "value": DIR[direction], "result": res}

    def stop(self, device_id: str) -> dict:
        rec = self.ensure(device_id)
        d = tinytuya.Device(device_id, rec["ip"], rec["key"], version=rec["version"])
        d.set_socketTimeout(2.0)
        res = None
        try:
            res = d.set_value(STOP_DP, True)
        except Exception as exc:
            res = {"error": str(exc)}
        return {"via": "lan", "dp": STOP_DP, "value": True, "result": res}
