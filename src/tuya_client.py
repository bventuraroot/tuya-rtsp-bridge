"""Tuya IPC-Terminal Web-API (QR-Login, Kameras, Session)."""
from __future__ import annotations

import json
import random
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import requests

REGIONS = {
    "eu": {
        "key": "eu-central",
        "host": "protect-eu.ismartlife.me",
        "label": "Western Europe (EU)",
    },
    "we": {
        "key": "eu-east",
        "host": "protect-we.ismartlife.me",
        "label": "Eastern Europe (WE)",
    },
    "us": {
        "key": "us-west",
        "host": "protect-us.ismartlife.me",
        "label": "USA West",
    },
    "ue": {
        "key": "us-east",
        "host": "protect-ue.ismartlife.me",
        "label": "USA East",
    },
    "cn": {
        "key": "china",
        "host": "protect.ismartlife.me",
        "label": "China",
    },
    "in": {
        "key": "india",
        "host": "protect-in.ismartlife.me",
        "label": "India",
    },
}

CAMERA_CATEGORIES = {"sp", "dghsxj"}
QR_PAYLOAD_PREFIX = "tuyaSmart--qrLogin?token="


def _utc_iso(ts: Optional[float] = None) -> str:
    if ts is None:
        return datetime.now(timezone.utc).isoformat()
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def _user_key(region_key: str, email: str) -> str:
    safe = email.replace("@", "_at_").replace(".", "_")
    return f"{region_key}_{safe}"


def _rtsp_path(name: str, device_id: str) -> str:
    safe = re.sub(r"[\s/\\]+", "_", name).strip("_")
    if not safe:
        safe = device_id
    return f"/{safe}"


class TuyaClient:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
        self.region_id = "eu"
        self.host = REGIONS["eu"]["host"]
        self.region_key = REGIONS["eu"]["key"]
        self.token: Optional[str] = None
        self.login: Optional[dict] = None
        self.cameras: list[dict] = []
        self.last_error: Optional[str] = None
        self.last_poll: Optional[str] = None
        self.poll_count = 0
        self.generation = 0

    def set_region(self, region_id: str) -> None:
        if region_id not in REGIONS:
            raise ValueError(f"Unbekannte Region: {region_id}")
        info = REGIONS[region_id]
        self.region_id = region_id
        self.host = info["host"]
        self.region_key = info["key"]
        self.session = requests.Session()
        self.token = None
        self.login = None
        self.cameras = []

    def _url(self, path: str) -> str:
        return f"https://{self.host}{path}"

    def _headers(self, referer: str = "/login") -> dict:
        origin = f"https://{self.host}"
        return {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "*/*",
            "Origin": origin,
            "Referer": origin + referer,
            "X-Requested-With": "XMLHttpRequest",
        }

    def _post(self, path: str, payload: Any = None, referer: str = "/login") -> dict:
        data = None if payload is None else json.dumps(payload)
        resp = self.session.post(
            self._url(path),
            data=data,
            headers=self._headers(referer),
            timeout=30,
        )
        resp.raise_for_status()
        body = resp.json()
        if not body.get("success"):
            raise RuntimeError(body.get("errorMsg") or body.get("msg") or "Tuya-API-Fehler")
        return body

    def generate_qr(self) -> str:
        self.session.get(self._url("/login"), timeout=20)
        body = self._post("/api/login/security/QCtoken", payload=None)
        token = body.get("result")
        if not token or not isinstance(token, str):
            raise RuntimeError("Kein QR-Token erhalten")
        self.token = token
        self.login = None
        self.last_error = None
        self.last_poll = "QR erzeugt, warte auf Scan …"
        self.poll_count = 0
        self.generation += 1
        return token

    def qr_payload(self) -> str:
        if not self.token:
            raise RuntimeError("Kein QR-Token")
        return QR_PAYLOAD_PREFIX + self.token

    def _as_login(self, result) -> Optional[dict]:
        if isinstance(result, str):
            try:
                result = json.loads(result)
            except Exception:
                return None
        if isinstance(result, dict) and (
            result.get("uid")
            or result.get("sid")
            or result.get("ecode")
            or result.get("username")
            or result.get("email")
        ):
            return result
        return None

    def fetch_user_info(self) -> Optional[dict]:
        for path, payload in (
            ("/api/common/user/info", {}),
            ("/api/customized/web/app/info", None),
        ):
            try:
                body = self._post(path, payload=payload, referer="/playback")
            except Exception:
                continue
            login = self._as_login(body.get("result"))
            if login:
                return login
        return None

    def poll_once(self) -> Optional[dict]:
        if not self.token:
            return None
        url = self._url("/api/login/poll")
        resp = self.session.post(
            url,
            data=json.dumps({"token": self.token}),
            headers=self._headers("/login"),
            timeout=30,
        )
        raw = resp.text
        self.poll_count += 1
        self.last_poll = raw[:8000]
        resp.raise_for_status()
        body = resp.json()
        login = self._as_login(body.get("result"))
        if login:
            self.login = login
            return login
        if body.get("success"):
            via_session = self.fetch_user_info()
            if via_session:
                self.login = via_session
                return via_session
        return None

    def wait_login(self, timeout_s: int = 300, interval_s: float = 1.0, generation: Optional[int] = None) -> Optional[dict]:
        deadline = time.time() + timeout_s
        gen = self.generation if generation is None else generation
        while time.time() < deadline:
            if self.generation != gen:
                return None
            try:
                got = self.poll_once()
            except Exception as exc:
                self.last_error = str(exc)
                self.last_poll = f"poll-fehler: {exc}"
                time.sleep(interval_s)
                continue
            if got:
                return got
            time.sleep(interval_s)
        return None

    def _cookie_dump(self) -> list[dict]:
        out = []
        for c in self.session.cookies:
            rest = getattr(c, "rest", None) or getattr(c, "_rest", None) or {}
            if not isinstance(rest, dict):
                rest = {}
            expires = "0001-01-01T00:00:00Z"
            if getattr(c, "expires", None):
                try:
                    expires = _utc_iso(float(c.expires))
                except Exception:
                    pass
            out.append(
                {
                    "name": getattr(c, "name", ""),
                    "value": getattr(c, "value", ""),
                    "domain": getattr(c, "domain", None) or self.host,
                    "path": getattr(c, "path", None) or "/",
                    "expires": expires,
                    "secure": bool(getattr(c, "secure", False)),
                    "httpOnly": bool(rest.get("HttpOnly") or rest.get("httponly")),
                }
            )
        return out

    def save_session(self) -> Path:
        if not self.login:
            raise RuntimeError("Nicht eingeloggt")
        email = self.login.get("email") or self.login.get("username") or self.login.get("uid")
        try:
            cookies = self._cookie_dump()
        except Exception:
            cookies = []
        session = {
            "region": self.region_key,
            "email": email,
            "lastRefresh": _utc_iso(),
            "userKey": _user_key(self.region_key, email),
            "sessionData": {
                "loginResult": self.login,
                "cookies": cookies,
                "lastValidated": _utc_iso(),
                "serverHost": self.host,
                "region": self.region_key,
                "userEmail": email,
            },
        }
        path = self.data_dir / f"user_{session['userKey']}.json"
        path.write_text(json.dumps(session, indent=2, ensure_ascii=False), encoding="utf-8")
        return path

    def load_latest_session(self) -> bool:
        files = sorted(self.data_dir.glob("user_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not files:
            return False
        data = json.loads(files[0].read_text(encoding="utf-8"))
        sd = data.get("sessionData") or {}
        host = sd.get("serverHost")
        if not host:
            return False
        self.host = host
        self.region_key = data.get("region") or sd.get("region") or self.region_key
        for rid, info in REGIONS.items():
            if info["host"] == host or info["key"] == self.region_key:
                self.region_id = rid
                break
        self.login = sd.get("loginResult")
        self.session = requests.Session()
        for c in sd.get("cookies") or []:
            self.session.cookies.set(
                c.get("name", ""),
                c.get("value", ""),
                domain=(c.get("domain") or host).lstrip("."),
                path=c.get("path") or "/",
            )
        cam_file = self.data_dir / "cameras.json"
        if cam_file.exists():
            registry = json.loads(cam_file.read_text(encoding="utf-8"))
            self.cameras = registry.get("cameras") or []
        return bool(self.login)

    def discover_cameras(self) -> list[dict]:
        if not self.login:
            raise RuntimeError("Nicht eingeloggt")
        self._post("/api/customized/web/app/info", payload=None, referer="/playback")
        devices: list[dict] = []
        seen: set[str] = set()

        try:
            homes = self._post("/api/new/common/homeList", payload=None, referer="/playback")
        except Exception:
            homes = {"result": []}

        for home in homes.get("result") or []:
            gid = home.get("gid")
            if gid is None:
                continue
            try:
                rooms = self._post(
                    "/api/new/common/roomList",
                    payload={"homeId": str(gid)},
                    referer="/playback",
                )
            except Exception:
                continue
            for room in rooms.get("result") or []:
                for device in room.get("deviceList") or []:
                    did = device.get("deviceId")
                    if device.get("category") in CAMERA_CATEGORIES and did and did not in seen:
                        seen.add(did)
                        devices.append(device)

        try:
            shared = self._post("/api/new/playback/shareList", payload=None, referer="/playback")
        except Exception:
            shared = {}
        for sh in ((shared.get("result") or {}).get("securityWebCShareInfoList") or []):
            for device in sh.get("deviceInfoList") or []:
                did = device.get("deviceId")
                if device.get("category") in CAMERA_CATEGORIES and did and did not in seen:
                    seen.add(did)
                    devices.append(device)

        email = self.login.get("email") or self.login.get("username") or self.login.get("uid")
        user_key = _user_key(self.region_key, email)
        cameras = []
        for device in devices:
            did = device["deviceId"]
            skill = ""
            try:
                cfg = self._post(
                    "/api/jarvis/config",
                    payload={
                        "devId": did,
                        "clientTraceId": f"{random.randrange(1 << 62):x}",
                    },
                    referer="/playback",
                )
                skill = (cfg.get("result") or {}).get("skill") or ""
            except Exception:
                continue
            name = device.get("deviceName") or did
            cameras.append(
                {
                    "userKey": user_key,
                    "deviceId": did,
                    "deviceName": name,
                    "category": device.get("category") or "",
                    "rtspPath": _rtsp_path(name, did),
                    "productId": device.get("productId") or "",
                    "uuid": device.get("uuid") or "",
                    "skill": skill,
                }
            )
        self.cameras = cameras
        registry = {"cameras": cameras, "lastUpdated": _utc_iso()}
        (self.data_dir / "cameras.json").write_text(
            json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        return cameras

    def logout(self) -> None:
        for f in self.data_dir.glob("user_*.json"):
            f.unlink(missing_ok=True)
        cam = self.data_dir / "cameras.json"
        if cam.exists():
            cam.unlink()
        self.session = requests.Session()
        self.token = None
        self.login = None
        self.cameras = []
        self.last_error = None


def slug(name: str) -> str:
    s = (name or "").replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()
    s = re.sub(r"[^a-zA-Z0-9_-]+", "_", s)
    return s.strip("_") or "kamera"
