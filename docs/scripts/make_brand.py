"""Rasterize brand assets. No network, no secrets, no live video."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "images"
WEB = ROOT / "web"

BG, PANEL, INK, DIM = (12, 16, 12), (20, 26, 20), (200, 230, 184), (111, 138, 98)
AMBER, OK, LINE = (226, 177, 60), (125, 206, 106), (42, 54, 40)


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = (
        ("segoeuib.ttf", "segoeui.ttf")
        if bold
        else ("segoeui.ttf", "arial.ttf", "DejaVuSans.ttf")
    )
    windir = Path(r"C:\Windows\Fonts")
    for name in names:
        p = windir / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def draw_mark(size: int) -> Image.Image:
    im = Image.new("RGBA", (size, size), (*BG, 255))
    d = ImageDraw.Draw(im)
    s = size / 256.0

    def xy(*pts: float) -> list[float]:
        return [p * s for p in pts]

    r = 28 * s
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=(*BG, 255))
    pad = 12 * s
    d.rounded_rectangle(
        [pad, pad, size - 1 - pad, size - 1 - pad],
        radius=20 * s,
        outline=AMBER,
        width=max(2, int(6 * s)),
    )
    d.rounded_rectangle(
        xy(70, 124, 186, 186),
        radius=10 * s,
        fill=PANEL,
        outline=INK,
        width=max(2, int(5 * s)),
    )
    # dome
    d.pieslice(xy(86, 74, 170, 158), 180, 360, fill=PANEL, outline=INK, width=max(2, int(5 * s)))
    cx, cy, rr = 128 * s, 112 * s, 20 * s
    d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=BG, outline=INK, width=max(2, int(5 * s)))
    pr = 8 * s
    d.ellipse([cx - pr, cy - pr, cx + pr, cy + pr], fill=AMBER)
    y = 206 * s
    d.line([(88 * s, y), (168 * s, y)], fill=OK, width=max(2, int(5 * s)))
    d.line(
        [(168 * s, y), (168 * s, y + 12 * s), (88 * s, y + 12 * s), (88 * s, y)],
        fill=DIM,
        width=max(1, int(3 * s)),
    )
    return im


def social() -> Image.Image:
    w, h = 1280, 640
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for y in range(0, h, 3):
        d.line([(0, y), (w, y)], fill=(8, 11, 8), width=1)
    mark = draw_mark(360)
    im.paste(mark, (80, 140), mark)
    title = _font(54, bold=True)
    sub = _font(28)
    tiny = _font(20)
    d.text((500, 170), "TUYA RTSP BRIDGE", font=title, fill=AMBER)
    d.text((500, 250), "Cheap cloud-only cameras", font=sub, fill=INK)
    d.text((500, 290), "become local RTSP.", font=sub, fill=INK)
    d.text((500, 360), "No ONVIF.  No firmware flash.  QR once.", font=tiny, fill=DIM)
    d.text((500, 430), "github.com/DanEng1982/tuya-rtsp-bridge", font=tiny, fill=OK)
    d.rectangle([0, h - 8, w, h], fill=AMBER)
    return im


def save_ico(src: Image.Image, dest: Path) -> None:
    sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    src.convert("RGBA").save(dest, sizes=sizes)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    WEB.mkdir(parents=True, exist_ok=True)
    mark512 = draw_mark(512)
    mark256 = draw_mark(256)
    mark64 = draw_mark(64)
    mark512.save(OUT / "logo.png")
    mark256.save(OUT / "logo-mark.png")
    social().save(OUT / "social.png", optimize=True)
    save_ico(mark256, OUT / "app.ico")
    save_ico(mark256, WEB / "favicon.ico")
    mark64.save(WEB / "logo.png")
    svg = (OUT / "logo.svg").read_text(encoding="utf-8")
    (WEB / "logo.svg").write_text(svg, encoding="utf-8")
    print("wrote", OUT / "logo.png", (OUT / "logo.png").stat().st_size)
    print("wrote", OUT / "social.png", (OUT / "social.png").stat().st_size)
    print("wrote", WEB / "favicon.ico")


if __name__ == "__main__":
    main()
