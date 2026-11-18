#!/usr/bin/env python3
"""Build docs/images/m5burner_cover.png (800x600) from the real screenshots.

  python tools/make_cover.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / "docs" / "screenshots"
OUT = ROOT / "docs" / "images" / "m5burner_cover.png"

BG, INK, SOFT, BLUE = (12, 12, 24), (241, 244, 255), (140, 152, 184), (80, 200, 255)


def font(size, bold=False):
    for name in (("segoeuib.ttf" if bold else "segoeui.ttf"), "arialbd.ttf" if bold else "arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (800, 600), BG)
    d = ImageDraw.Draw(img)
    d.text((400, 62), "AtomS3 Motion Face", font=font(54, True), fill=INK, anchor="mm")
    d.text((400, 112), "Shake it, tilt it, leave it alone - it reacts", font=font(24), fill=SOFT, anchor="mm")

    moods = ["idle", "happy", "dizzy", "scared"]
    chars = ["cat", "robot", "ghost", "cyclops"]
    size, gap = 150, 25
    x0 = (800 - (4 * size + 3 * gap)) // 2
    for row, c in enumerate(chars[:2]):
        for col, m in enumerate(moods):
            p = SHOTS / f"{c}_{m}.png"
            if not p.exists():
                continue
            im = Image.open(p).convert("RGB").resize((size, size), Image.NEAREST)
            x, y = x0 + col * (size + gap), 160 + row * (size + gap)
            d.rounded_rectangle((x - 4, y - 4, x + size + 4, y + size + 4), 14, outline=(40, 46, 70), width=3)
            img.paste(im, (x, y))
    d.text((400, 540), "M5Stack AtomS3  -  4 characters  -  MPU6886 motion", font=font(24), fill=BLUE, anchor="mm")
    d.text((400, 572), "github.com/ElectroIoT/M5-AtomS3-Motion-Face", font=font(18), fill=SOFT, anchor="mm")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    main()
