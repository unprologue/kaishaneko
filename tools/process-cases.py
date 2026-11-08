"""Prepare the case photos (images/cases/*.jpg) for the gallery.

Writes to images/processed/ and never touches the sources.
- Trim the SNS overlays: top 12% (company logo / UNPROLOGUE) and bottom ~13% (会社猫 logo).
- Front shots 4:5, side/back shots 1:1, centred on the subject.
- Same tone for every photo: saturation -10%, slightly warmer.
- Cut-outs (_cut.webp) with a 1px feathered edge.
- seikan-front: _blur versions with the wooden tag blurred (6px) until name use is approved.
Usage: U2NET_HOME=<models> python tools/process-cases.py   (Pillow, numpy, rembg)
"""
import os
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from rembg import remove, new_session

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "images", "cases")
OUT = os.path.join(ROOT, "images", "processed")
os.makedirs(OUT, exist_ok=True)
TOP, BOTTOM = 162, 1176  # rows kept from the 1080x1350 SNS cards
SESSION = new_session("isnet-general-use")

SHOTS = {
    "seikan-front": "front", "seikan-back": "square", "seikan-left": "square", "seikan-right": "square",
    "unprologue-front": "front", "unprologue-back": "square", "unprologue-side-a": "square", "unprologue-side-b": "square",
}
# wooden tag with personal names, in source pixel coordinates
TAG_BOXES = {"seikan-front": (78, 520, 425, 1048)}


def tone(im):
    im = ImageEnhance.Color(im).enhance(0.9)  # saturation -10%
    a = np.asarray(im).astype(np.float32)
    a[..., 0] *= 1.025
    a[..., 2] *= 0.97
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def blur_box(im, box, radius=6):
    region = im.crop(box).filter(ImageFilter.GaussianBlur(radius))
    out = im.copy()
    out.paste(region, box[:2])
    return out


def cutout(im):
    cut = remove(im, session=SESSION, post_process_mask=True)
    r, g, b, a = cut.split()
    a = a.filter(ImageFilter.GaussianBlur(1))
    cut = Image.merge("RGBA", (r, g, b, a))
    return cut, a.point(lambda v: 255 if v > 8 else 0).getbbox()


def pad_vertical(im, extra):
    """Extend the plain backdrop above and below by repeating and softening the edge rows."""
    a = np.asarray(im)
    top, bottom = extra // 2, extra - extra // 2
    padded = np.pad(a, ((top, bottom), (0, 0), (0, 0)), mode="edge")
    out = Image.fromarray(padded)
    soft = out.filter(ImageFilter.GaussianBlur(12))
    mask = Image.new("L", out.size, 0)
    mask.paste(255, (0, 0, out.width, top))
    mask.paste(255, (0, out.height - bottom, out.width, out.height))
    return Image.composite(soft, out, mask), top


def crop_ratio(im, bbox, ratio):
    """Crop of the given width/height ratio that keeps the whole subject, centred.
    When the subject is wider than the ratio allows, the backdrop is extended vertically."""
    need = (bbox[2] - bbox[0]) + 60
    if need > im.height * ratio:
        im, shift = pad_vertical(im, round(min(need, im.width) / ratio) - im.height)
        bbox = (bbox[0], bbox[1] + shift, bbox[2], bbox[3] + shift)
        crop, (x0, y0) = crop_ratio(im, bbox, ratio)
        return crop, (x0, y0 - shift)
    w, h = im.size
    cw = min(w, round(h * ratio))
    ch = round(cw / ratio)
    cx = (bbox[0] + bbox[2]) / 2
    x0 = int(min(max(cx - cw / 2, 0), w - cw))
    y0 = (h - ch) // 2
    return im.crop((x0, y0, x0 + cw, y0 + ch)), (x0, y0)


def save(im, name, fmt="WEBP"):
    path = os.path.join(OUT, name)
    if fmt == "WEBP":
        im.save(path, "WEBP", quality=82, method=6)
    else:
        im.convert("RGB").save(path, "JPEG", quality=84, optimize=True, progressive=True)
    print(name, im.size)


for name, kind in SHOTS.items():
    src = Image.open(os.path.join(SRC, name + ".jpg")).convert("RGB")
    trimmed = tone(src.crop((0, TOP, src.width, BOTTOM)))
    cut, bbox = cutout(trimmed)
    framed, (fx, fy) = crop_ratio(trimmed, bbox, 4 / 5 if kind == "front" else 1)
    save(framed, name + ".webp")
    save(framed, name + ".jpg", "JPEG")
    save(cut.crop(bbox), name + "_cut.webp")
    if name in TAG_BOXES:
        x0, y0, x1, y1 = TAG_BOXES[name]
        tag = (x0, y0 - TOP, x1, y1 - TOP)
        blurred = blur_box(trimmed, tag)
        framed_blur, _ = crop_ratio(blurred, bbox, 4 / 5 if kind == "front" else 1)
        save(framed_blur, name + "_blur.webp")
        save(framed_blur, name + "_blur.jpg", "JPEG")
        cut_blur = blur_box(cut.convert("RGBA"), tag)
        save(cut_blur.crop(bbox), name + "_cut_blur.webp")
