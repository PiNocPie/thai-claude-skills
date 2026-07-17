# -*- coding: utf-8 -*-
"""Three Reel cover variants (1080x1920). Key content kept in the centre 1:1
safe area so the profile-grid crop still reads."""
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from render_lib import font, silom, mono, rounded, clamp
import render_cards as RC

W,H=1080,1920
GREEN=(11,222,133,255); INK=(9,11,15,255); WHITE=(245,248,250,255)
YELLOW=(255,214,10,255); DARK=(18,21,27,255)

def load_face(path, darken=0.55, blurbg=False):
    im=Image.open(path).convert("RGB").resize((W,H))
    if blurbg: im=im.filter(ImageFilter.GaussianBlur(6))
    im=ImageEnhance.Brightness(im).enhance(darken)
    im=ImageEnhance.Contrast(im).enhance(1.08)
    return im.convert("RGBA")

def grad(img, top_a=210, bot_a=230, mid=0):
    """vertical dark gradient top+bottom for text legibility."""
    g=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(g)
    for y in range(H):
        if y<H*0.42:
            a=int(top_a*(1-y/(H*0.42)))
        elif y>H*0.58:
            a=int(bot_a*((y-H*0.58)/(H*0.42)))
        else:
            a=mid
        d.line([(0,y),(W,y)],fill=(6,8,11,max(0,min(255,a))))
    img.alpha_composite(g)

def outline_text(d, xy, s, f, fill, ow=10, oc=(0,0,0,255), anchor="mm"):
    x,y=xy
    if anchor=="mm":
        w=int(f.getlength(s)); asc,desc=f.getmetrics()
        x-=w//2; y-=(asc+desc)//2
    for dx in range(-ow,ow+1,max(1,ow//3)):
        for dy in range(-ow,ow+1,max(1,ow//3)):
            if dx*dx+dy*dy<=ow*ow:
                d.text((x+dx,y+dy),s,font=f,fill=oc)
    d.text((x,y),s,font=f,fill=fill)

def fit(txt,maxw,start,weight="bold"):
    sz=start
    while sz>36:
        f=font(sz,weight)
        if f.getlength(txt)<=maxw: return f
        sz-=3
    return font(36,weight)

def tag(d, cx, y, text, bg=GREEN, fg=INK, size=52, arrow=False):
    f=font(size,"bold"); tw=int(f.getlength(text)); asc,desc=f.getmetrics()
    extra=int(size*1.1) if arrow else 0
    rounded(d,[cx-tw//2-40-extra//2,y,cx+tw//2+40+extra//2,y+asc+desc+18],36,fill=bg)
    d.text((cx-tw//2-extra//2,y+9),text,font=f,fill=fg)
    if arrow:
        ax=cx+tw//2-extra//2+24; ay=y+(asc+desc)//2+9; s=size//3
        d.polygon([(ax,ay-s),(ax+s,ay),(ax,ay+s)],fill=fg)

# ---------- Cover A: BOLD hook ----------
def cover_bold(face_path, out):
    img=load_face(face_path,0.5)
    grad(img,200,235)
    d=ImageDraw.Draw(img)
    tag(d, W//2, 250, "ทริค AI ที่ออฟฟิศไม่บอก")
    l1="แทนเพื่อนร่วมงาน"; l2="ตัวปัญหา"; l3="ด้วย AI ตัวเดียว"
    f1=fit(l1,1000,120); f2=fit(l2,1000,120)
    outline_text(d,(W//2,470),l1,f1,WHITE,12)
    outline_text(d,(W//2,470+150),l2,f2,GREEN,12)
    # bottom claim band
    f3=fit(l3,980,96)
    rounded(d,[70,1470,1010,1470+180],40,fill=(0,0,0,180))
    outline_text(d,(W//2,1560),l3,f3,YELLOW,8)
    # arrow accent
    d.polygon([(W//2-40,1360),(W//2+40,1360),(W//2,1420)],fill=GREEN)
    img.convert("RGB").save(out,quality=92)
    print("cover_bold ->",out)

# ---------- Cover B: TERMINAL ----------
def cover_terminal(face_path, out):
    img=Image.new("RGBA",(W,H),(12,14,18,255))
    # faint face on right
    face=load_face(face_path,0.4,blurbg=False).resize((int(W*0.9),int(H*0.9)))
    img.alpha_composite(face,(int(W*0.16),int(H*0.16)))
    grad(img,150,240)
    d=ImageDraw.Draw(img)
    # terminal snippet card centered
    box=[90,430,990,1000]
    RC._shadow(img,box,30)
    d=ImageDraw.Draw(img)
    rounded(d,box,30,fill=(22,25,31,248))
    d.rounded_rectangle([90,430,990,500],radius=30,fill=(31,35,42,255)); d.rectangle([90,470,990,502],fill=(31,35,42,255))
    for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
        d.ellipse([120+i*34,452,142+i*34,474],fill=c)
    d.text((450,446),"SKILL.md",font=font(32,"semi"),fill=(150,158,168,255))
    mf=font(40,"medium")
    lines=[("name: ",GREEN,"replace-coworker",WHITE),
           ("do: ",GREEN,"กรอก Excel + แจ้งหัวหน้า",WHITE),
           ("run: ",GREEN,"อัตโนมัติทุกวัน",WHITE)]
    y=540
    for ln in lines:
        x=130; d.text((x,y),ln[0],font=mf,fill=ln[1]); x+=int(mf.getlength(ln[0]))
        d.text((x,y),ln[2],font=mf,fill=ln[3]); y+=78
    d.rectangle([130,y+14,152,y+62],fill=GREEN)   # cursor block
    # headline
    tag(d,W//2,150,"1 ไฟล์ .md",bg=GREEN,size=54)
    outline_text(d,(W//2,340),"แทนคนทั้งคน ?",fit("แทนคนทั้งคน ?",980,110),WHITE,10)
    # bottom
    outline_text(d,(W//2,1150),"สอน AI ให้ทำงานซ้ำๆ แทนเรา",fit("สอน AI ให้ทำงานซ้ำๆ แทนเรา",980,64,"semi"),GREEN,6)
    tag(d,W//2,1660,"ดูวิธีเลย",bg=YELLOW,size=56,arrow=True)
    img.convert("RGB").save(out,quality=92)
    print("cover_terminal ->",out)

# ---------- Cover C: BEFORE/AFTER clean ----------
def cover_clean(face_path, out):
    img=load_face(face_path,0.62)
    grad(img,150,235)
    d=ImageDraw.Draw(img)
    tag(d,W//2,220,"AI ทำงานแทนคน",bg=GREEN,size=52)
    outline_text(d,(W//2,430),"งานที่พี่เขา",fit("งานที่พี่เขา",980,110),WHITE,10)
    outline_text(d,(W//2,560),"ทำทั้งวัน",fit("ทำทั้งวัน",980,110),WHITE,10)
    outline_text(d,(W//2,700),"AI ทำใน 1 นาที",fit("AI ทำใน 1 นาที",980,116),GREEN,10)
    # mini excel chip bottom
    box=[240,1250,840,1560]
    RC._shadow(img,box,26)
    d=ImageDraw.Draw(img)
    rounded(d,box,26,fill=(255,255,255,255))
    d.rounded_rectangle([240,1250,840,1312],radius=26,fill=(16,124,16,255)); d.rectangle([240,1286,840,1314],fill=(16,124,16,255))
    d.text((272,1264),"report.xlsx",font=font(30,"semi"),fill=WHITE)
    yy=1330
    for r in range(4):
        d.rectangle([264,yy,816,yy+52],outline=(220,224,220,255))
        d.text((284,yy+10),["ค่าวัตถุดิบ  12,400","ค่าขนส่ง  2,150","ค่าจ้าง  8,000","ค่าไฟ  1,320"][r],font=font(28,"medium"),fill=(30,36,30,255))
        d.line([760,yy+26,772,yy+38],fill=(16,150,60,255),width=4); d.line([772,yy+38,790,yy+14],fill=(16,150,60,255),width=4)
        yy+=54
    tag(d,W//2,1650,"เซฟไว้ทำตาม",bg=YELLOW,size=52)
    img.convert("RGB").save(out,quality=92)
    print("cover_clean ->",out)

if __name__=="__main__":
    import sys
    face=sys.argv[1] if len(sys.argv)>1 else "cover/face_5.0.jpg"
    cover_bold(face,"out/cover_bold.jpg")
    cover_terminal(face,"out/cover_terminal.jpg")
    cover_clean(face,"out/cover_clean.jpg")
