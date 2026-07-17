# -*- coding: utf-8 -*-
"""Render the full overlay (captions + hook/punch text + CTA) for a given style.
Cards are added by render_cards.py (composited in the frame builder)."""
import sys, os
from PIL import Image, ImageDraw
import timeline as T
from render_lib import *

GREEN = (*getattr(T, "ACCENT", (11, 222, 133)), 255)   # accent (per-clip via timeline.ACCENT; default brand green)
WHITE = (255, 255, 255, 255)
YELLOW = (255, 214, 10, 255)
INK = (10, 12, 16, 255)

STYLES = {
    # loud tiktok: big, thick outline, no bar, active word green pop, numbers yellow
    "bold": dict(size=104, weight="bold", bar=None, outline=(0,0,0,255), ow=12,
                 active=GREEN, base=WHITE, num=YELLOW, y=1200, pop=True, shadow=(0,7,(0,0,0,150))),
    # terminal/coder: dark rounded bar, mono-ish, green active, cursor
    "terminal": dict(size=88, weight="semi", bar=(8,10,14,235), outline=None, ow=0,
                 active=GREEN, base=(225,235,230,255), num=GREEN, y=1230, pop=False,
                 barpad=(46,26), cursor=True, shadow=None),
    # clean editorial: subtle translucent pill, semibold, green active underline
    "clean": dict(size=92, weight="semi", bar=(18,20,26,180), outline=None, ow=0,
                 active=GREEN, base=WHITE, num=WHITE, y=1215, pop=False,
                 barpad=(54,30), underline=True, shadow=(0,4,(0,0,0,120))),
}

def is_num(w):
    return w.strip() in {"1","2","3","4"}

def draw_caption(img, t, st):
    cap = None
    for c in T.CAPTIONS:
        if c[0] <= t < c[1]:
            cap = c; break
    if not cap: return
    start, end, text, emph = cap
    words = text.split(" ")
    ai = word_active(cap, t)
    f = font(st["size"], st["weight"])
    asc, desc = f.getmetrics()
    line_h = asc + desc
    space = int(st["size"]*0.30)
    # word advance widths (use font.getlength for proper advance incl. side bearing)
    adv = [int(f.getlength(w)) for w in words]
    total_w = sum(adv) + space*(len(words)-1)
    cy = getattr(T, "CAPTION_Y", st["y"])   # per-clip caption height (keep clear of the face)
    top = cy - line_h//2            # common baseline top
    d = ImageDraw.Draw(img)
    # background bar
    if st["bar"]:
        bx, by = st.get("barpad",(40,24))
        x0 = (T.W-total_w)//2 - bx
        rounded(d, [x0, top-by, x0+total_w+2*bx, top+line_h+by],
                r=int(st["size"]*0.36), fill=st["bar"])
    x = (T.W - total_w)//2
    for i,w in enumerate(words):
        active = (i==ai)
        col = st["active"] if active else (st["num"] if is_num(w) else st["base"])
        if (w in emph) and not active:
            col = st["active"]
        wy = top
        if st["shadow"]:
            sx,sy,scol = st["shadow"]
            d.text((x+sx, wy+sy), w, font=f, fill=scol)
        if st["ow"]>0:
            ow=st["ow"]; step=max(1,ow//3)
            for dx in range(-ow,ow+1,step):
                for dy in range(-ow,ow+1,step):
                    if dx*dx+dy*dy<=ow*ow:
                        d.text((x+dx,wy+dy), w, font=f, fill=st["outline"])
        d.text((x,wy), w, font=f, fill=col)
        if active and st.get("underline"):
            d.rounded_rectangle([x, top+line_h-6, x+adv[i], top+line_h+4], radius=5, fill=GREEN)
        x += adv[i] + space
    if st.get("cursor"):
        if int(t*2)%2==0:
            d.rectangle([x+4, top+8, x+4+16, top+line_h-8], fill=GREEN)

def fit_font(txt, maxw, start=96, weight="bold"):
    sz = start
    while sz > 40:
        f = font(sz, weight)
        if f.getlength(txt) <= maxw: return f, sz
        sz -= 3
    return font(40, weight), 40

def draw_hook(img, t):
    st_, en, txt = T.HOOK_TEXT
    if not (st_ <= t < en): return
    d = ImageDraw.Draw(img)
    lines = txt.split("\n")
    # auto-fit the widest line (top band, kept above the head so it never covers the face)
    widest = max(lines, key=lambda l: font(88,"bold").getlength(l))
    f, sz = fit_font(widest, 980, 88)
    lh = int(sz*1.16)
    # kicker tag (top)
    kf = font(46,"bold")
    tag=getattr(T,"HOOK_TAG","ทริค AI ที่ออฟฟิศไม่บอก")
    tw = int(kf.getlength(tag)); kasc,kdesc = kf.getmetrics()
    ky=85
    rounded(d,[T.W//2-tw//2-34, ky, T.W//2+tw//2+34, ky+kasc+kdesc+14], 34, fill=GREEN)
    d.text((T.W//2-tw//2, ky+7), tag, font=kf, fill=INK)
    # hook lines (top band, above head)
    y = 255
    for i, ln in enumerate(lines):
        col = WHITE if i==0 else GREEN
        draw_text_outline(img, (T.W//2, y), ln, f, col, (0,0,0,255), 12, anchor="mm", shadow=(0,8,(0,0,0,160)))
        y += lh

def draw_punch(img, t):
    st_, en, txt = T.PUNCH_TEXT
    if not (st_ <= t < en): return
    d = ImageDraw.Draw(img)
    age=t-st_
    s=ease_out_back(clamp(age/0.3))
    f=font(92,"bold")
    draw_text_outline(img,(T.W//2, 455), txt, f, YELLOW,(0,0,0,255),12, anchor="mm", shadow=(0,8,(0,0,0,170)))

def draw_cta(img, t):
    d=ImageDraw.Draw(img)
    # early save sticker
    s0,s1=T.CTA["save_sticker"]
    if s0<=t<s1:
        f=font(38,"bold")
        tag="เซฟไว้ก่อน"
        tw=int(f.getlength(tag)); asc,desc=f.getmetrics()
        x=T.W-tw-70; y=250
        rounded(d,[x-52,y-12,x+tw+24,y+asc+desc+8],26,fill=(0,0,0,190))
        # pin dot
        d.ellipse([x-40,y+asc//2-8,x-24,y+asc//2+8], fill=GREEN)
        d.text((x,y),tag,font=f,fill=(255,255,255,255))
    # follow chip
    f0,f1=T.CTA["follow"]
    if f0<=t<f1:
        age=t-f0; s=ease_out_back(clamp(age/0.3))
        f=font(46,"bold")
        label="กดติดตาม"; sub="กดติดตามไว้เลย"
        fw,fh,fo=text_wh(f,label)
        sf=font(34,"medium"); sw,sh,so=text_wh(sf,sub)
        bw=max(fw,sw)+ 250
        x0=(T.W-bw)//2; y0=1440
        rounded(d,[x0,y0,x0+bw,y0+150],40,fill=GREEN)
        # plus circle
        d.ellipse([x0+30,y0+40,x0+100,y0+110],fill=INK)
        d.text((x0+52,y0+48),"+",font=font(56,"bold"),fill=GREEN)
        d.text((x0+130,y0+28),label,font=f,fill=INK)
        d.text((x0+130,y0+92),sub,font=sf,fill=(28,24,20,255))
    # bio CTA: free offer (replaces comment-a-keyword CTA)
    c0,c1=T.CTA["comment"]
    if c0<=t<c1:
        f=font(56,"bold")
        pre="ของฟรีทั้งหมด "; kw="ที่ไบโอ"; post=""
        parts=[(pre,WHITE),(kw,GREEN),(post,WHITE)]
        widths=[int(f.getlength(p)) for p,_ in parts]
        tot=sum(widths); x=(T.W-tot)//2; y=1625
        asc,desc=f.getmetrics()
        rounded(d,[x-40,y-16,x+tot+40,y+asc+desc+16],32,fill=(0,0,0,190))
        for (p,col),wd in zip(parts,widths):
            draw_text_outline(img,(x,y),p,f,col,(0,0,0,255),4)
            x+=wd
        # small "link in bio" pointer line
        sf=font(34,"semi"); sub="แตะลิงก์ในไบโอโปรไฟล์"
        sw=int(sf.getlength(sub))
        d.text((T.W//2-sw//2, y+asc+desc+26), sub, font=sf, fill=(190,196,204,255))

def build_frame(t, style_name):
    st = STYLES[style_name]
    img = Image.new("RGBA",(T.W,T.H),(0,0,0,0))
    draw_hook(img, t)
    draw_punch(img, t)
    if t >= 4.6:            # cold-open hook owns the first beat; captions take over after
        draw_caption(img, t, st)
    draw_cta(img, t)
    return img

if __name__ == "__main__":
    style = sys.argv[1] if len(sys.argv)>1 else "bold"
    outdir = sys.argv[2] if len(sys.argv)>2 else "frames"
    tests = [0.6, 3.2, 7.6, 14.6, 18.6, 20.0, 25.2, 36.0, 46.0, 51.0]
    os.makedirs(outdir, exist_ok=True)
    for i,t in enumerate(tests):
        im = build_frame(t, style)
        # composite on gray to preview
        bg = Image.new("RGBA",(T.W,T.H),(60,60,60,255))
        bg.alpha_composite(im)
        bg.convert("RGB").save(f"{outdir}/test_{style}_{i:02d}_t{t:.1f}.jpg", quality=88)
    print("wrote", len(tests), "test frames for", style)
