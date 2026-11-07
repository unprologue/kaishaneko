"""Crop, tone-match and cut out the photos used by FINISHING / PROCESS.

Writes to images/processed/ and never touches the source files.
Tone (same values for every non-cutout photo): saturation -15%, slightly warmer,
highlights pulled down a little so the photos sit on the #f4efe6 page.
Usage: python tools/process-photos.py  (needs Pillow, numpy, rembg; EDSR model path via EDSR_X2)
"""
import os
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "images", "processed")
os.makedirs(OUT, exist_ok=True)


def src(path):
    return Image.open(os.path.join(ROOT, path)).convert("RGB")


def tone(im):
    im = ImageEnhance.Color(im).enhance(0.85)  # saturation -15%
    a = np.asarray(im).astype(np.float32)
    a[..., 0] *= 1.03  # a touch warmer
    a[..., 2] *= 0.96
    hi = a > 200  # soften highlights
    a[hi] = 200 + (a[hi] - 200) * 0.8
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def upscale2x(im):
    path = os.environ.get("EDSR_X2")
    if not path:
        return im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    import cv2
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(path)
    sr.setModel("edsr", 2)
    up = sr.upsample(cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR))
    return Image.fromarray(cv2.cvtColor(up, cv2.COLOR_BGR2RGB))


def save(im, name, width=None):
    if width and im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, name), "WEBP", quality=85, method=6)
    print(name, im.size)


# FINISHING 01: hands applying the logo, portrait 3:4
save(tone(src("assets/logo-guide/hero.jpg").crop((160, 0, 627, 623))), "finishing-01-hands.webp")

# PROCESS strip: kiln/craft, design, apply, deliver, display (overlay text cropped away)
save(tone(src("miyasou2021.09_026.JPG")), "process-1-craft.webp", 1200)
save(tone(src("assets/delivery/design-proposal.jpg").crop((0, 0, 1021, 700))), "process-2-design.webp", 1000)
save(tone(upscale2x(src("assets/logo-guide/step-03.jpg").crop((120, 0, 722, 242)))), "process-3-apply.webp")
save(tone(src("assets/service/07-delivered-before-logo.jpg").crop((0, 460, 1080, 1270))), "process-4-deliver.webp")
save(tone(src("assets/service/09-reception.jpg").crop((0, 535, 1080, 1270))), "process-5-display.webp")

# FINISHING 02: the delivered cat with its tag, background removed (1px feather)
from rembg import remove, new_session

cut = remove(src("assets/choose/delivered-with-tag.jpg"), session=new_session("isnet-general-use"), post_process_mask=True)
r, g, b, a = cut.split()
a = a.filter(ImageFilter.GaussianBlur(1))
cut = Image.merge("RGBA", (r, g, b, a))
box = a.point(lambda v: 255 if v > 8 else 0).getbbox()
save(cut.crop(box), "finishing-02-cat.webp", 1200)
