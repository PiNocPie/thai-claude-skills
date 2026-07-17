# -*- coding: utf-8 -*-
"""Shared drawing helpers + caption/text layout for the reel overlay."""
from PIL import Image, ImageDraw, ImageFont
import math

SUKHUMVIT = "/System/Library/Fonts/Supplemental/SukhumvitSet.ttc"
SILOM = "/System/Library/Fonts/Supplemental/Silom.ttf"
MENLO = "/System/Library/Fonts/Menlo.ttc"

_font_cache = {}
def font(size, weight="bold"):
    idx = {"thin":0,"light":1,"text":2,"medium":3,"semi":4,"bold":5}[weight]
    key = ("suk", size, idx)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(SUKHUMVIT, size, index=idx)
    return _font_cache[key]

def silom(size):
    key = ("silom", size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(SILOM, size)
    return _font_cache[key]

def mono(size):
    key = ("menlo", size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(MENLO, size, index=0)
    return _font_cache[key]

# ---------- easing ----------
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(t): return 1 - (1 - t) ** 3
def ease_out_back(t):
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2
def ease_in_out(t): return 3*t*t - 2*t*t*t

# ---------- primitives ----------
def rounded(draw, xy, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def text_wh(f, s):
    b = f.getbbox(s)
    return b[2]-b[0], b[3]-b[1], b[1]

def draw_text_outline(img, pos, s, f, fill, outline=(0,0,0,255), ow=6, anchor=None, shadow=None):
    """Draw text with an outline by stamping. pos is top-left unless anchor set (center 'mm')."""
    d = ImageDraw.Draw(img)
    x, y = pos
    if anchor == "mm":
        w, h, off = text_wh(f, s)
        x = x - w/2
        y = y - h/2 - off
    if shadow:
        sx, sy, scol = shadow
        d.text((x+sx, y+sy), s, font=f, fill=scol)
    if ow > 0 and outline:
        rng = range(-ow, ow+1, max(1, ow//3))
        for dx in rng:
            for dy in rng:
                if dx*dx+dy*dy <= ow*ow:
                    d.text((x+dx, y+dy), s, font=f, fill=outline)
    d.text((x, y), s, font=f, fill=fill)
    return x, y

def word_active(cap, t):
    """Return index of currently-spoken word given caption (start,end,text,emph)."""
    st, en, text, emph = cap
    words = text.split(" ")
    n = len(words)
    if en <= st: return n-1
    frac = clamp((t - st) / (en - st))
    idx = min(n-1, int(frac * n))
    return idx
