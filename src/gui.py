"""Native Desktop-GUI für die Tuya-Brücke. Backend bleibt :8787 / :8554."""
from __future__ import annotations

import json
import os
import socket
import subprocess
import threading
import time
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path

import tkinter as tk
from PIL import Image, ImageTk

from preview import VlcPreview
from paths import install_root, user_data
from i18n import LANG_LABELS, current_label, is_rtl, lang_from_label, t

ROOT = install_root()
API = "http://127.0.0.1:8787"
BG, PANEL, INK, DIM, LINE = "#0c100c", "#141a14", "#c8e6b8", "#6f8a62", "#2a3628"
AMBER, OK, BAD = "#e2b13c", "#7dce6a", "#d36b58"


def _nowin() -> int:
    return subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0


def port_up(port: int) -> bool:
    s = socket.socket()
    s.settimeout(0.4)
    try:
        return s.connect_ex(("127.0.0.1", port)) == 0
    except OSError:
        return False
    finally:
        s.close()


def ensure_backend() -> None:
    if port_up(8787):
        return
    import sys
    from procutil import python_exe

    server = Path(__file__).resolve().parent / "server.py"
    env = os.environ.copy()
    env["PYTHONPATH"] = str(server.parent) + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.Popen(
        [str(python_exe()), "-u", str(server)],
        cwd=str(user_data()),
        env=env,
        creationflags=_nowin(),
    )
    for _ in range(40):
        if port_up(8787):
            return
        time.sleep(0.25)


def api(path: str, body: dict | None = None) -> dict:
    data = None
    headers = {}
    method = "GET"
    if body is not None:
        method = "POST"
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(API + path, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=20) as res:
        return json.loads(res.read().decode("utf-8"))


class BridgeGui(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(t("app_title"))
        self.configure(bg=BG)
        self.geometry("1920x1080+0+0")
        self.minsize(1280, 800)
        self._apply_icon()
        self.qr_img = None
        self._last_qr = ""
        self._busy = False
        self._cards: dict[str, dict] = {}
        self._fs: tk.Toplevel | None = None
        self._fs_prev: VlcPreview | None = None
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._build()
        self.after(200, self.refresh)

    def _apply_icon(self) -> None:
        ico = ROOT / "web" / "favicon.ico"
        png = ROOT / "web" / "logo.png"
        if ico.exists():
            try:
                self.iconbitmap(default=str(ico))
            except tk.TclError:
                pass
        if png.exists():
            try:
                self._wm_icon = ImageTk.PhotoImage(Image.open(png))
                self.iconphoto(True, self._wm_icon)
            except Exception:
                pass

    def _build(self) -> None:
        top = tk.Frame(self, bg=PANEL, height=64)
        top.pack(fill="x")
        top.pack_propagate(False)
        logo_path = ROOT / "web" / "logo.png"
        if logo_path.exists():
            try:
                self._banner_logo = ImageTk.PhotoImage(Image.open(logo_path).resize((32, 32)))
                tk.Label(top, image=self._banner_logo, bg=PANEL).pack(side="left", padx=(18, 0), pady=14)
            except Exception:
                pass
        self.lbl_banner = tk.Label(
            top, text=t("app_banner"), fg=AMBER, bg=PANEL,
            font=("Segoe UI", 18, "bold"),
        )
        self.lbl_banner.pack(side="left", padx=22)
        self.chips = {}
        for key in ("rtsp", "wd", "hls", "phase"):
            lb = tk.Label(top, text=key.upper(), fg=DIM, bg=BG, bd=1, relief="solid",
                          font=("Consolas", 10), padx=10, pady=6)
            lb.pack(side="right", padx=6, pady=14)
            self.chips[key] = lb

        body = tk.Frame(self, bg=BG)
        body.pack(fill="both", expand=True)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        left = tk.Frame(body, bg=PANEL, width=360)
        left.grid(row=0, column=0, sticky="nsw")
        left.grid_propagate(False)
        mid = tk.Frame(body, bg=BG)
        mid.grid(row=0, column=1, sticky="nsew")
        right = tk.Frame(body, bg="#101610", width=380)
        right.grid(row=0, column=2, sticky="nse")
        right.grid_propagate(False)

        self.lbl_lang = tk.Label(left, text=t("lang_heading"), fg=DIM, bg=PANEL, font=("Segoe UI", 9))
        self.lbl_lang.pack(anchor="w", padx=18, pady=(14, 4))
        self.lang_var = tk.StringVar(value=current_label())
        lang_box = tk.OptionMenu(left, self.lang_var, *LANG_LABELS.values(), command=self._set_lang)
        lang_box.config(bg="#0e140e", fg=INK, highlightthickness=0, width=32)
        lang_box.pack(fill="x", padx=18)

        self.lbl_server = tk.Label(left, text=t("server"), fg=DIM, bg=PANEL, font=("Segoe UI", 9))
        self.lbl_server.pack(anchor="w", padx=18, pady=(18, 4))
        self.region = tk.StringVar()
        self.region_box = tk.OptionMenu(left, self.region, "")
        self.region_box.config(bg="#0e140e", fg=INK, highlightthickness=0, width=32)
        self.region_box.pack(fill="x", padx=18)
        self.qr_label = tk.Label(left, text=t("qr_none"), bg="#ffffff", fg="#666", width=32, height=14)
        self.qr_label.pack(padx=18, pady=14, fill="x")
        self.hint = tk.Label(left, text=t("hint"), fg=DIM, bg=PANEL,
                             wraplength=310, justify="right" if is_rtl() else "left")
        self.hint.pack(anchor="w", padx=18)
        btns = tk.Frame(left, bg=PANEL)
        btns.pack(fill="x", padx=18, pady=12)
        self.btn_qr = tk.Button(btns, text=t("btn_qr"), command=self.do_qr, bg=AMBER, fg="#1a1404",
                  relief="flat", padx=12, pady=8)
        self.btn_qr.pack(side="left")
        self.btn_logout = tk.Button(btns, text=t("btn_logout"), command=self.do_logout, bg=PANEL, fg=INK,
                  relief="flat", padx=12, pady=8)
        self.btn_logout.pack(side="left", padx=8)
        self.user = tk.Label(left, text="", fg=INK, bg=PANEL, justify="left")
        self.user.pack(anchor="w", padx=18, pady=8)

        head = tk.Frame(mid, bg=BG)
        head.pack(fill="x", padx=20, pady=16)
        self.lbl_cams = tk.Label(head, text=t("cameras"), fg=DIM, bg=BG, font=("Segoe UI", 9))
        self.lbl_cams.pack(side="left")
        self.cam_count = tk.Label(head, text="", fg=DIM, bg=BG, font=("Consolas", 10))
        self.cam_count.pack(side="left", padx=12)
        self.btn_refresh = tk.Button(head, text=t("cameras_refresh"), command=self.do_refresh, bg=PANEL, fg=INK,
                  relief="flat", padx=10, pady=6)
        self.btn_refresh.pack(side="right")
        self.cam_box = tk.Frame(mid, bg=BG)
        self.cam_box.pack(fill="both", expand=True, padx=20)
        self.yaml = tk.Text(mid, height=3, bg="#0e140e", fg=INK, insertbackground=INK,
                            relief="flat", font=("Consolas", 10))
        self.yaml.pack(fill="x", padx=20, pady=(8, 6))
        self.btn_yaml = tk.Button(mid, text=t("yaml_copy"), command=self.copy_yaml, bg=PANEL, fg=INK,
                  relief="flat", padx=10, pady=6)
        self.btn_yaml.pack(anchor="e", padx=20, pady=(0, 10))

        self.lbl_sw = tk.Label(right, text=t("switches"), fg=DIM, bg="#101610", font=("Segoe UI", 9))
        self.lbl_sw.pack(anchor="w", padx=20, pady=(18, 8))
        self.vars = {
            "rtsp": tk.BooleanVar(value=True),
            "watchdog": tk.BooleanVar(value=True),
            "hls": tk.BooleanVar(value=False),
            "archive": tk.BooleanVar(value=False),
        }
        self.flag_btns: dict[str, tk.Checkbutton] = {}
        self.flag_subs: dict[str, tk.Label] = {}
        for key, title_k, sub_k in (
            ("rtsp", "rtsp_engine", "rtsp_engine_d"),
            ("watchdog", "watchdog", "watchdog_d"),
            ("hls", "hls", "hls_d"),
            ("archive", "archive", "archive_d"),
        ):
            fr = tk.Frame(right, bg="#101610")
            fr.pack(fill="x", padx=20, pady=4)
            cb = tk.Checkbutton(
                fr, variable=self.vars[key], command=self.push_flags,
                text=t(title_k), fg=INK, bg="#101610", selectcolor=BG,
                activebackground="#101610", activeforeground=AMBER,
                font=("Segoe UI", 12, "bold"), anchor="w",
            )
            cb.pack(fill="x")
            sub = tk.Label(fr, text=t(sub_k), fg=DIM, bg="#101610", font=("Segoe UI", 10))
            sub.pack(anchor="w", padx=22)
            self.flag_btns[key] = cb
            self.flag_subs[key] = sub

        self.lbl_rst = tk.Label(right, text=t("restart"), fg=DIM, bg="#101610", font=("Segoe UI", 9))
        self.lbl_rst.pack(anchor="w", padx=20, pady=(22, 8))
        self.btn_rst_e = tk.Button(right, text=t("rst_engine"), command=self.do_rst_rtsp, bg=PANEL, fg=INK, relief="flat", pady=10)
        self.btn_rst_e.pack(fill="x", padx=20, pady=4)
        self.btn_rst_u = tk.Button(right, text=t("rst_ui"), command=self.do_rst_ui, bg=PANEL, fg=INK, relief="flat", pady=10)
        self.btn_rst_u.pack(fill="x", padx=20, pady=4)
        self.btn_rst_a = tk.Button(right, text=t("rst_all"), command=self.do_rst_all, bg=PANEL, fg=INK, relief="flat", pady=10)
        self.btn_rst_a.pack(fill="x", padx=20, pady=4)
        self.status = tk.Label(right, text="", fg=DIM, bg="#101610", wraplength=330, justify="left")
        self.status.pack(anchor="w", padx=20, pady=16)

    def _chip(self, key: str, text: str, ok: bool | None) -> None:
        lb = self.chips[key]
        lb.config(text=text, fg=OK if ok else (BAD if ok is False else DIM))

    def _thread(self, fn) -> None:
        threading.Thread(target=fn, daemon=True).start()

    def refresh(self) -> None:
        if self._busy:
            self.after(2500, self.refresh)
            return
        try:
            st = api("/api/state")
            self._paint(st)
        except Exception as exc:
            self._chip("phase", t("chip_api_off"), False)
            self.status.config(text=str(exc))
        self.after(2500, self.refresh)

    def _paint(self, s: dict) -> None:
        running = bool((s.get("rtsp") or {}).get("running"))
        self._chip("rtsp", f"RTSP :{(s.get('rtsp') or {}).get('port', '')}" if running else t("chip_rtsp_off"), running or None)
        self._chip("wd", t("chip_wd_on") if s.get("watchdogRunning") else t("chip_wd_off"), bool(s.get("watchdogRunning")) or None)
        self._chip("hls", t("chip_hls_on") if s.get("hlsRunning") else t("chip_hls_off"), False if s.get("hlsRunning") else None)
        phase = {"idle": (t("phase_idle"), None), "waiting": (t("phase_wait"), None), "logged_in": (t("phase_in"), True), "error": (t("phase_err"), False)}
        lab, ok = phase.get(s.get("phase"), (s.get("phase") or "?", None))
        self._chip("phase", lab, ok)
        self.hint.config(text=s.get("message") or t("hint"), justify="right" if is_rtl() else "left")
        user = s.get("user")
        self.user.config(text=(f"{user.get('nickname') or t('account')}\n{user.get('email') or user.get('uid') or ''}" if user else ""))

        regions = s.get("regions") or {}
        if not getattr(self, "_regions_ready", False):
            menu = self.region_box["menu"]
            menu.delete(0, "end")
            for rid, meta in regions.items():
                menu.add_command(
                    label=f"{meta.get('label')} — {meta.get('host')}",
                    command=lambda v=rid: self.region.set(v),
                )
            self._regions_ready = True
        if s.get("region") and (not self.region.get()):
            self.region.set(s["region"])

        if s.get("hasQr") and s.get("qrId") != self._last_qr:
            self._last_qr = s.get("qrId") or ""
            self._load_qr()
        elif not s.get("hasQr"):
            self.qr_label.config(image="", text=t("qr_session") if s.get("loggedIn") else t("qr_none"))
            self.qr_img = None

        flags = s.get("flags") or {}
        for k, var in self.vars.items():
            if not self._busy:
                var.set(bool(flags.get(k)))

        cams = s.get("cameras") or []
        self.cam_count.config(text=f"{len(cams)}  ·  {s.get('lanIp')}:{(s.get('rtsp') or {}).get('port')}")
        self._sync_cards(cams, bool(running))

        y = t("yaml_empty")
        if cams:
            y = "mqtt:\n  enabled: false\n\ncameras:\n"
            for cam in cams:
                y += f"  {cam.get('frigateId')}:\n    ffmpeg:\n      inputs:\n        - path: {cam.get('rtspHd')}\n          roles: [detect, record]\n"
        cur = self.yaml.get("1.0", "end").strip()
        if cur != y.strip():
            self.yaml.delete("1.0", "end")
            self.yaml.insert("1.0", y)

    def _local_url(self, url: str) -> str:
        if not url:
            return ""
        try:
            from urllib.parse import urlparse, urlunparse
            p = urlparse(url)
            if p.scheme == "rtsp":
                host = "127.0.0.1"
                netloc = f"{host}:{p.port}" if p.port else host
                return urlunparse((p.scheme, netloc, p.path, p.params, p.query, p.fragment))
        except Exception:
            pass
        return url

    def _sync_cards(self, cams: list, rtsp_up: bool) -> None:
        ids = [str(c.get("deviceId") or c.get("deviceName") or i) for i, c in enumerate(cams)]
        for did in list(self._cards):
            if did not in ids:
                rec = self._cards.pop(did)
                rec["preview"].stop()
                rec["frame"].destroy()
        if not cams:
            if "empty" not in self._cards:
                lb = tk.Label(self.cam_box, text=t("empty_cams"), fg=DIM, bg=BG)
                lb.pack(anchor="w")
                self._cards["empty"] = {"frame": lb, "preview": VlcPreview(), "url": ""}
            return
        if "empty" in self._cards:
            self._cards.pop("empty")["frame"].destroy()
        for cam in cams:
            did = str(cam.get("deviceId") or cam.get("deviceName"))
            url = cam.get("rtspHd") or ""
            if did not in self._cards:
                self._cards[did] = self._make_card(cam)
            rec = self._cards[did]
            rec["name"].config(text=cam.get("deviceName") or t("camera"))
            rec["id"].config(text=cam.get("deviceId") or "")
            rec["url_l"].config(text=url)
            rec["url"] = url
            rec["copy"].config(command=lambda u=url: self._clip(u))
            if self._fs is not None:
                continue
            local = self._local_url(url)
            prev: VlcPreview = rec["preview"]
            if rtsp_up and local and not prev.running:
                rec["thumb"].update_idletasks()
                prev.start(local, int(rec["thumb"].winfo_id()), cache_ms=150)
            elif not rtsp_up and prev.running:
                prev.stop()
                rec["thumb"].itemconfig(rec["txt_id"], text=t("no_stream"))

    def _make_card(self, cam: dict) -> dict:
        did = str(cam.get("deviceId") or "")
        url = cam.get("rtspHd") or ""
        card = tk.Frame(self.cam_box, bg=PANEL, bd=1, relief="solid")
        card.pack(fill="x", pady=6)
        thumb = tk.Canvas(card, width=480, height=270, bg="#050705", highlightthickness=0, cursor="hand2")
        thumb.pack(side="left", padx=8, pady=8)
        txt_id = thumb.create_text(240, 135, text=t("fs_hint"), fill=DIM, font=("Segoe UI", 11))
        rec: dict = {"frame": card, "thumb": thumb, "txt_id": txt_id, "url": url}
        prev = VlcPreview()
        rec["preview"] = prev
        thumb.bind("<Button-1>", lambda e, d=did: self._open_fullscreen(d))

        right = tk.Frame(card, bg=PANEL)
        right.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        rec["name"] = tk.Label(right, text=cam.get("deviceName") or t("camera"), fg=INK, bg=PANEL,
                               font=("Segoe UI", 14, "bold"))
        rec["name"].pack(anchor="w")
        rec["id"] = tk.Label(right, text=did, fg=DIM, bg=PANEL, font=("Consolas", 9))
        rec["id"].pack(anchor="w")
        rec["url_l"] = tk.Label(right, text=url, fg=INK, bg=PANEL, font=("Consolas", 10),
                                wraplength=420, justify="left")
        rec["url_l"].pack(anchor="w", pady=4)
        rec["copy"] = tk.Button(right, text=t("copy_hd"), command=lambda u=url: self._clip(u),
                                bg=BG, fg=AMBER, relief="flat")
        rec["copy"].pack(anchor="w", side="left")
        rec["fsbtn"] = tk.Button(right, text=t("fullscreen"), command=lambda d=did: self._open_fullscreen(d),
                  bg=BG, fg=INK, relief="flat")
        rec["fsbtn"].pack(anchor="w", side="left", padx=8)
        ptz = tk.Frame(right, bg=PANEL)
        ptz.pack(anchor="w", pady=8)

        def cell(r: int, c: int, lab: str, d: str) -> None:
            b = tk.Button(ptz, text=lab, width=3, bg=BG, fg=INK, relief="flat")
            b.grid(row=r, column=c, padx=3, pady=3)
            if d == "stop":
                b.config(command=lambda: self._ptz(did, "stop"))
                return
            b.bind("<ButtonPress-1>", lambda e, dd=d: self._ptz(did, dd))
            b.bind("<ButtonRelease-1>", lambda e: self._ptz(did, "stop"))

        cell(0, 1, "↑", "up")
        cell(1, 0, "←", "left")
        cell(1, 1, "■", "stop")
        cell(1, 2, "→", "right")
        cell(2, 1, "↓", "down")
        return rec

    def _open_fullscreen(self, did: str) -> None:
        rec = self._cards.get(did)
        if not rec or self._fs is not None:
            return
        url = self._local_url(rec["url"])
        self.after(80, lambda: self._fs_go(rec, url))

    def _fs_go(self, rec: dict, url: str) -> None:
        if self._fs is not None:
            return
        win = tk.Toplevel(self)
        win.title(rec["name"].cget("text"))
        win.configure(bg="black")
        win.attributes("-fullscreen", True)
        bar = tk.Frame(win, bg="#111", height=36)
        bar.pack(fill="x")
        tk.Button(bar, text=t("back"), command=self._close_fullscreen,
                  bg="#222", fg=INK, relief="flat", padx=14).pack(side="left", padx=8, pady=4)
        cv = tk.Frame(win, bg="black")
        cv.pack(fill="both", expand=True)
        win.update()
        self._fs = win
        prev = VlcPreview()
        self._fs_prev = prev
        prev.start(url, int(cv.winfo_id()), cache_ms=150)
        win.bind("<Escape>", lambda e: self._close_fullscreen())
        win.protocol("WM_DELETE_WINDOW", self._close_fullscreen)
        win.focus_force()

    def _close_fullscreen(self, resume: bool = True) -> None:
        fs = self._fs
        prev = self._fs_prev
        self._fs = None
        self._fs_prev = None

        def cleanup() -> None:
            if prev:
                prev.stop()
            if fs:
                try:
                    fs.destroy()
                except tk.TclError:
                    pass

        self.after(30, cleanup)

    def _on_close(self) -> None:
        self._close_fullscreen(resume=False)
        for rec in self._cards.values():
            rec["preview"].stop()
        self.destroy()

    def _load_qr(self) -> None:
        try:
            with urllib.request.urlopen(API + "/api/qr.png", timeout=8) as res:
                img = Image.open(BytesIO(res.read())).resize((280, 280))
            self.qr_img = ImageTk.PhotoImage(img)
            self.qr_label.config(image=self.qr_img, text="")
        except Exception:
            self.qr_label.config(image="", text=t("qr_error"))

    def _clip(self, text: str) -> None:
        self.clipboard_clear()
        self.clipboard_append(text)
        self.status.config(text=t("copied"))

    def copy_yaml(self) -> None:
        self._clip(self.yaml.get("1.0", "end").strip())

    def _ptz(self, device_id: str, direction: str) -> None:
        self._thread(lambda: api("/api/ptz/move", {"deviceId": device_id, "direction": direction}))

    def push_flags(self) -> None:
        body = {k: bool(v.get()) for k, v in self.vars.items()}
        self._busy = True

        def go() -> None:
            try:
                st = api("/api/flags", body)
                self.after(0, lambda: self._paint(st))
            except Exception as exc:
                self.after(0, lambda: self.status.config(text=str(exc)))
            finally:
                self._busy = False

        self._thread(go)

    def _set_lang(self, choice: str) -> None:
        lang = lang_from_label(str(choice))
        try:
            api("/api/lang", {"lang": lang})
        except Exception:
            from i18n import save_lang
            save_lang(lang)
        self.status.config(text=t("lang_saved"))

    def do_qr(self) -> None:
        rid = self.region.get() or "eu"
        self._thread(lambda: self.after(0, lambda: self._paint(api("/api/qr/start", {"region": rid}))))

    def do_logout(self) -> None:
        self._thread(lambda: self.after(0, lambda: self._paint(api("/api/logout", {}))))

    def do_refresh(self) -> None:
        self._thread(lambda: self.after(0, lambda: self._paint(api("/api/cameras/refresh", {}))))

    def do_rst_rtsp(self) -> None:
        self.status.config(text=t("engine_restart"))
        self._thread(lambda: self.after(0, lambda: self._paint(api("/api/restart/rtsp", {}))))

    def do_rst_ui(self) -> None:
        self.status.config(text=t("ui_restart"))
        self._thread(lambda: api("/api/restart/ui", {}))

    def do_rst_all(self) -> None:
        self.status.config(text=t("all_restart"))
        self._thread(lambda: api("/api/restart/all", {}))


def main() -> None:
    ensure_backend()
    app = BridgeGui()
    app.mainloop()


if __name__ == "__main__":
    main()
