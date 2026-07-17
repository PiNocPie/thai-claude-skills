# -*- coding: utf-8 -*-
"""Demo insert cards: SKILL.md editor, go/walk/turn analogy, Claude Code chat,
Excel filling. Rendered as a slide-in panel over the upper part of the frame."""
from PIL import Image, ImageDraw, ImageFilter
import timeline as T
from render_lib import font, mono, rounded, clamp, ease_out, ease_out_back

GREEN=(*getattr(T,"ACCENT",(11,222,133)),255); INK=(16,19,24,255); PANEL=(24,27,33,255)
PANEL2=(31,35,42,255); GREY=(150,158,168,255); WHITE=(238,242,246,255)
YELLOW=(255,214,10,255); BLUE=(90,170,255,255); PURP=(190,150,255,255)
ORANGE=(255,150,70,255); RED=(255,95,95,255)

def _panel_anim(t, win):
    """Return (dx, alpha_mult, active) for slide-in/out."""
    s,e,_=win
    if not (s-0.05 <= t <= e+0.4): return None
    ein=clamp((t-s)/0.42)
    eout=1.0-clamp((t-(e-0.32))/0.34)
    a=min(ein,max(0.0,eout))
    dx=int((1-ease_out_back(ein))*120)
    return dx, clamp(a), True

_SHADOW_CACHE={}
def _shadow(base, box, r, blur=26, alpha=150):
    x0,y0,x1,y1=[int(v) for v in box]
    key=(x0,y0,x1,y1,r,blur,alpha,base.size)
    sh=_SHADOW_CACHE.get(key)
    if sh is None:
        sh=Image.new("RGBA", base.size, (0,0,0,0))
        d=ImageDraw.Draw(sh)
        d.rounded_rectangle([x0+6,y0+14,x1+6,y1+16], radius=r, fill=(0,0,0,alpha))
        sh=sh.filter(ImageFilter.GaussianBlur(blur))
        _SHADOW_CACHE[key]=sh
    base.alpha_composite(sh)

def _window_chrome(d, box, r, title, accent=GREEN):
    x0,y0,x1,y1=box
    rounded(d, box, r, fill=PANEL)
    # title bar
    d.rounded_rectangle([x0,y0,x1,y0+70], radius=r, fill=PANEL2)
    d.rectangle([x0,y0+40,x1,y0+72], fill=PANEL2)
    for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
        d.ellipse([x0+28+i*34,y0+26,x0+50+i*34,y0+48], fill=c)
    tf=font(34,"semi")
    tw=int(tf.getlength(title))
    d.text((x0+(x1-x0)//2-tw//2, y0+18), title, font=tf, fill=GREY)

def _reveal_lines(local, lines, factor=1.25):
    n=len(lines)
    return int(clamp(local*factor)*n+0.001)

# ---------- card: SKILL.md ----------
def card_skillmd(base, t, win, dx, a):
    x0,y0=70+dx,210; x1,y1=1010+dx,1080
    box=[x0,y0,x1,y1]
    _shadow(base, box, 34)
    layer=Image.new("RGBA", base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    _window_chrome(d, box, 34, "SKILL.md")
    lines=[
        ("---",GREY),("name: ",GREEN,"excel-data-entry",WHITE),
        ("description: ",GREEN,"กรอกข้อมูลลง Excel",WHITE),
        ("  แล้วแจ้งหัวหน้าเมื่อเสร็จ",WHITE),
        ("---",GREY),("",WHITE),
        ("# ขั้นตอนงาน (แทนพี่คนนั้น)",YELLOW),
        ("1. รับข้อมูลที่ส่งเข้ามา",WHITE),
        ("2. เปิดไฟล์ report.xlsx",WHITE),
        ("3. กรอก: วันที่ | รายการ | จำนวน",WHITE),
        ("4. เซฟไฟล์",WHITE),
        ('5. แจ้งหัวหน้า “เรียบร้อยครับ”',WHITE),
    ]
    s,e,_=win; local=clamp((t-s)/(e-s-0.4))
    nshow=_reveal_lines(local, lines, 1.3)
    f=font(37,"medium")
    y=y0+104; lh=64
    for i,ln in enumerate(lines[:nshow]):
        x=x0+46
        if len(ln)==2:
            d.text((x,y),ln[0],font=f,fill=ln[1])
        else:
            d.text((x,y),ln[0],font=f,fill=ln[1])
            x+=int(f.getlength(ln[0]))
            d.text((x,y),ln[2],font=f,fill=ln[3])
        y+=lh
    # cursor on last visible line
    if nshow<len(lines) and int(t*2)%2==0:
        cx=x0+46
        d.rectangle([cx, y+6, cx+16, y+44], fill=GREEN)
    if a<1: layer=_fade(layer,a)
    base.alpha_composite(layer)

# ---------- card: analogy arrows ----------
def card_arrow(base, t, win, dx, a):
    x0,y0=70+dx,70; x1,y1=1010+dx,500
    box=[x0,y0,x1,y1]
    _shadow(base, box, 34)
    layer=Image.new("RGBA", base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    rounded(d, box, 34, fill=PANEL)
    tf=font(38,"bold"); tt="ถาม AI ให้ได้คำตอบเป๊ะ"
    d.text((x0+(x1-x0)//2-int(tf.getlength(tt))//2, y0+30), tt, font=tf, fill=GREEN)
    s,e,_=win; local=clamp((t-s)/(e-s-0.5))
    steps=[('ถามให้ตรง',GREEN),('ใส่ข้อมูลครบ',WHITE),('ได้คำตอบเป๊ะ',YELLOW)]
    cy=y0+250; n=len(steps)
    show=int(clamp(local*1.3)*n+0.001)
    bw=250; gap=(x1-x0-bw*n)//(n+1)
    cf=font(34,"semi")
    for i,(lbl,col) in enumerate(steps):
        if i>=show: break
        bx=x0+gap+(bw+gap)*i
        rounded(d,[bx,cy-56,bx+bw,cy+56],26,fill=PANEL2,outline=col,width=3)
        tw=int(cf.getlength(lbl))
        d.text((bx+bw//2-tw//2, cy-24), lbl, font=cf, fill=col)
        if i<n-1 and i<show-1:
            ax=bx+bw+gap//2
            d.polygon([(ax-16,cy-16),(ax+16,cy),(ax-16,cy+16)], fill=GREEN)
    if a<1: layer=_fade(layer,a)
    base.alpha_composite(layer)

# ---------- card: Claude Code chat (compact, top band) ----------
def card_claudechat(base, t, win, dx, a):
    x0,y0=70+dx,70; x1,y1=1010+dx,600
    box=[x0,y0,x1,y1]
    _shadow(base, box, 34)
    layer=Image.new("RGBA", base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    _window_chrome(d, box, 34, "Claude")
    s,e,_=win; local=clamp((t-s)/(e-s-0.4))
    y=y0+92
    # screenshot attachment chip
    ch=[x0+40,y,x0+470,y+72]
    rounded(d,ch,16,fill=PANEL2)
    gx,gy=x0+60,y+16
    rounded(d,[gx,gy,gx+52,gy+40],8,outline=GREEN,width=3)
    d.ellipse([gx+9,gy+8,gx+23,gy+22],fill=GREEN)
    d.polygon([(gx+8,gy+36),(gx+26,gy+16),(gx+46,gy+36)],fill=GREEN)
    d.text((gx+70,y+18),"screenshot.png",font=font(30,"medium"),fill=WHITE)
    y+=98
    # user prompt bubble
    uf=font(35,"medium")
    ub=[x0+40,y,x1-40,y+100]
    rounded(d,ub,22,fill=(38,43,52,255))
    d.text((x0+62,y+14),"You",font=font(26,"bold"),fill=GREY)
    d.text((x0+62,y+50),"รูปนี้คืออะไร ใช้ยังไงครับ?",font=uf,fill=WHITE)
    y=ub[3]+30
    # assistant streaming checklist
    if local>0.30:
        d.text((x0+62,y),"Claude",font=font(26,"bold"),fill=GREEN)
        y+=48
        checks=[
            "บอกได้เลยว่านี่คือทูลอะไร",
            "ใช้ยังไง ทีละสเต็ป",
        ]
        cf=font(34,"medium")
        nshow=int(clamp((local-0.30)/0.60)*len(checks)+0.001)
        for i,c in enumerate(checks[:nshow]):
            d.ellipse([x0+62,y+6,x0+92,y+36],outline=GREEN,width=3)
            d.line([x0+70,y+21,x0+77,y+29],fill=GREEN,width=4)
            d.line([x0+77,y+29,x0+87,y+13],fill=GREEN,width=4)
            d.text((x0+108,y),c,font=cf,fill=WHITE)
            y+=54
    if a<1: layer=_fade(layer,a)
    base.alpha_composite(layer)

# ---------- card: Excel ----------
def card_excel(base, t, win, dx, a):
    x0,y0=70+dx,220; x1,y1=1010+dx,1010
    box=[x0,y0,x1,y1]
    _shadow(base, box, 30)
    layer=Image.new("RGBA", base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    rounded(d, box, 30, fill=(255,255,255,255))
    # green header bar (excel)
    d.rounded_rectangle([x0,y0,x1,y0+68],radius=30,fill=(16,124,16,255))
    d.rectangle([x0,y0+40,x1,y0+70],fill=(16,124,16,255))
    d.text((x0+30,y0+16),"report.xlsx",font=font(34,"semi"),fill=(255,255,255,255))
    cols=["วันที่","รายการ","จำนวน","สถานะ"]
    rows=[["05/07","ค่าวัตถุดิบ","12,400","✓"],
          ["05/07","ค่าขนส่ง","2,150","✓"],
          ["06/07","ค่าจ้าง","8,000","✓"],
          ["06/07","ค่าไฟ","1,320","✓"],
          ["07/07","ค่าเช่า","15,000","✓"]]
    gx=x0+20; gy=y0+92; gw=x1-x0-40
    cw=[gw*0.22,gw*0.40,gw*0.22,gw*0.16]
    hf=font(30,"bold"); cf=font(30,"medium")
    # header row
    cx=gx
    for i,c in enumerate(cols):
        d.rectangle([cx,gy,cx+cw[i],gy+56],fill=(226,232,226,255),outline=(200,206,200,255))
        d.text((cx+14,gy+12),c,font=hf,fill=(40,60,40,255))
        cx+=cw[i]
    s,e,_=win; local=clamp((t-s)/(e-s-0.4))
    nshow=int(clamp(local*1.35)*len(rows)+0.001)
    ry=gy+56
    for r in range(len(rows)):
        cx=gx
        filled = r<nshow
        for i,val in enumerate(rows[r]):
            d.rectangle([cx,ry,cx+cw[i],ry+56],fill=(255,255,255,255),outline=(224,228,224,255))
            if filled:
                if i==3:
                    # green check cell
                    d.line([cx+cw[i]//2-12,ry+28,cx+cw[i]//2-2,ry+40],fill=(16,150,60,255),width=5)
                    d.line([cx+cw[i]//2-2,ry+40,cx+cw[i]//2+16,ry+14],fill=(16,150,60,255),width=5)
                else:
                    d.text((cx+14,ry+12),val,font=cf,fill=(30,36,30,255))
            cx+=cw[i]
        # active row highlight (currently filling)
        if r==nshow-1 and int(t*3)%2==0:
            d.rectangle([gx,ry,gx+gw,ry+56],outline=GREEN,width=4)
        ry+=56
    # counter chip
    chip=f"กรอกแล้ว {min(nshow,len(rows))}/{len(rows)} แถว"
    cfc=font(30,"bold"); cw2=int(cfc.getlength(chip))
    rounded(d,[x1-cw2-64, y1-70, x1-20, y1-16],26,fill=(16,124,16,255))
    d.text((x1-cw2-44, y1-62),chip,font=cfc,fill=(255,255,255,255))
    if a<1: layer=_fade(layer,a)
    base.alpha_composite(layer)

# ---------- card: external website / tool (browser mockup, top band) ----------
def card_browser(base, t, win, dx, a):
    x0,y0=70+dx,70; x1,y1=1010+dx,560
    box=[x0,y0,x1,y1]
    _shadow(base, box, 30)
    layer=Image.new("RGBA", base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    rounded(d, box, 30, fill=(250,250,252,255))                 # white browser body
    # top chrome
    d.rounded_rectangle([x0,y0,x1,y0+64],radius=30,fill=(232,234,238,255)); d.rectangle([x0,y0+34,x1,y0+66],fill=(232,234,238,255))
    for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
        d.ellipse([x0+26+i*30,y0+22,x0+46+i*30,y0+42],fill=c)
    rounded(d,[x0+150,y0+14,x1-40,y0+50],18,fill=(255,255,255,255))
    d.text((x0+172,y0+19),"newtool.ai",font=font(28,"medium"),fill=(90,96,104,255))
    # page content
    px=x0+44; py=y0+96
    d.text((px,py),"New AI Tool",font=font(50,"bold"),fill=(28,32,40,255))
    d.text((px,py+68),"เครื่องมือที่เพิ่งเจอในเน็ต",font=font(32,"medium"),fill=(120,126,134,255))
    hb=[px,py+128,x1-44,y1-40]
    rounded(d,hb,20,fill=(240,241,244,255))
    ccx=(hb[0]+hb[2])//2; ccy=(hb[1]+hb[3])//2
    d.ellipse([ccx-44,ccy-44,ccx+44,ccy+44],fill=GREEN)
    d.polygon([(ccx-14,ccy-24),(ccx+26,ccy),(ccx-14,ccy+24)],fill=(255,255,255,255))
    # screenshot marquee (dashed accent) — signals "capture this"
    s,e,_=win; local=clamp((t-s)/(e-s-0.4))
    if local>0.34:
        mx0,my0,mx1,my1=px+16,py+148,x1-88,y1-66
        dash=26
        for xx in range(mx0,mx1,dash*2):
            d.line([xx,my0,min(xx+dash,mx1),my0],fill=GREEN,width=5)
            d.line([xx,my1,min(xx+dash,mx1),my1],fill=GREEN,width=5)
        for yy in range(my0,my1,dash*2):
            d.line([mx0,yy,mx0,min(yy+dash,my1)],fill=GREEN,width=5)
            d.line([mx1,yy,mx1,min(yy+dash,my1)],fill=GREEN,width=5)
        cap="สกรีนช็อตเก็บไว้"
        cf=font(30,"bold"); cw=int(cf.getlength(cap))
        rounded(d,[mx1-cw-40,my0-54,mx1+2,my0-4],20,fill=GREEN)
        d.text((mx1-cw-20,my0-48),cap,font=cf,fill=(255,255,255,255))
    if a<1: layer=_fade(layer,a)
    base.alpha_composite(layer)

def _fade(layer, a):
    r,g,b,al=layer.split()
    al=al.point(lambda v:int(v*a))
    layer.putalpha(al); return layer

# ---------- card: proof strip (row of past-clip thumbnails, top band) ----------
# reads timeline.PROOF_IMAGES = [path, ...]  (generic; no hardcoded paths)
def card_proof(base, t, win, dx, a):
    imgs=getattr(T,"PROOF_IMAGES",[])
    if not imgs: return
    n=len(imgs); tw=250; th=int(tw*16/9); gap=40
    total=n*tw+(n-1)*gap; x0=(base.size[0]-total)//2+dx; y0=112
    s,e,_=win; local=clamp((t-s)/(e-s-0.4))
    layer=Image.new("RGBA", base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    # label chip
    lf=font(40,"bold"); lab="ผลงานล่าสุด"
    lw=int(lf.getlength(lab)); la,ld=lf.getmetrics()
    rounded(d,[base.size[0]//2-lw//2-30, 30, base.size[0]//2+lw//2+30, 30+la+ld+14],28,fill=GREEN)
    d.text((base.size[0]//2-lw//2, 37),lab,font=lf,fill=(14,15,19,255))
    for i,p in enumerate(imgs):
        if local < i*0.14: continue
        try: im=Image.open(p).convert("RGB").resize((tw,th))
        except Exception: continue
        bx=x0+i*(tw+gap)
        _shadow(layer,[bx,y0,bx+tw,y0+th],24)
        card=Image.new("RGBA",(tw,th),(0,0,0,0)); card.paste(im,(0,0))
        m=Image.new("L",(tw,th),0); ImageDraw.Draw(m).rounded_rectangle([0,0,tw-1,th-1],24,fill=255)
        card.putalpha(m); layer.alpha_composite(card,(bx,y0))
        ImageDraw.Draw(layer).rounded_rectangle([bx,y0,bx+tw-1,y0+th-1],24,outline=GREEN,width=5)
    if a<1: layer=_fade(layer,a)
    base.alpha_composite(layer)

# ---------- card: checklist (ticks items progressively, top band) ----------
# reads timeline.CHECKLIST_ITEMS = ["ตัด/ต่อ", ...]  and optional CHECKLIST_TITLE
def card_checklist(base, t, win, dx, a):
    items=getattr(T,"CHECKLIST_ITEMS",[])
    if not items: return
    n=len(items); rowh=72
    x0,y0=90+dx,90; x1=990+dx; y1=y0+84+n*rowh+18
    box=[x0,y0,x1,y1]
    _shadow(base, box, 30)
    layer=Image.new("RGBA", base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    rounded(d, box, 30, fill=PANEL)
    tf=font(38,"bold"); tt=getattr(T,"CHECKLIST_TITLE","AI ทำให้หมดนี่เลย")
    d.text((x0+(x1-x0)//2-int(tf.getlength(tt))//2, y0+24), tt, font=tf, fill=GREEN)
    s,e,_=win; local=clamp((t-s)/(e-s-0.4))
    nshow=int(clamp(local*1.15)*n+0.001)
    y=y0+92; cf=font(36,"medium")
    for i,it in enumerate(items):
        done=i<nshow; col=GREEN if done else GREY; cx=x0+52
        d.ellipse([cx,y+6,cx+34,y+40],outline=col,width=3)
        if done:
            d.line([cx+9,y+24,cx+16,y+33],fill=GREEN,width=5)
            d.line([cx+16,y+33,cx+28,y+13],fill=GREEN,width=5)
        d.text((cx+56,y+2),it,font=cf,fill=WHITE if done else GREY)
        y+=rowh
    if a<1: layer=_fade(layer,a)
    base.alpha_composite(layer)

# ---------- card: orchestration network (1 person -> many AI, top band) ----------
def _spark(d, cx, cy, r, col):
    k=0.30
    d.polygon([(cx,cy-r),(cx+r*k,cy-r*k),(cx+r,cy),(cx+r*k,cy+r*k),
               (cx,cy+r),(cx-r*k,cy+r*k),(cx-r,cy),(cx-r*k,cy-r*k)],fill=col)

def card_network(base, t, win, dx, a):
    Wd=base.size[0]
    layer=Image.new("RGBA", base.size,(0,0,0,0)); d=ImageDraw.Draw(layer)
    s,e,_=win; local=clamp((t-s)/(e-s-0.4))
    g=(GREEN[0],GREEN[1],GREEN[2])
    # title chip
    lf=font(40,"bold"); lab=getattr(T,"NETWORK_LABEL","1 คน คุม AI ทั้งทีม")
    lw=int(lf.getlength(lab)); la,ld=lf.getmetrics()
    rounded(d,[Wd//2-lw//2-30,36,Wd//2+lw//2+30,36+la+ld+14],28,fill=GREEN)
    d.text((Wd//2-lw//2,43),lab,font=lf,fill=(14,15,19,255))
    cx=Wd//2+dx; py=210
    ai_xs=[250+dx,410+dx,670+dx,830+dx]; ai_y=440
    nshow=int(clamp(local*1.3)*len(ai_xs)+0.001)
    # connecting lines person -> each AI (reveal progressively)
    for i,ax in enumerate(ai_xs):
        if i>=nshow: continue
        d.line([(cx,py+56),(ax,ai_y-44)],fill=(*g,170),width=4)
    for i in range(len(ai_xs)-1):
        if i+1<nshow: d.line([(ai_xs[i],ai_y),(ai_xs[i+1],ai_y)],fill=(120,92,72,130),width=3)
    # AI nodes
    for i,ax in enumerate(ai_xs):
        if i>=nshow: continue
        r=46; d.ellipse([ax-r,ai_y-r,ax+r,ai_y+r],fill=PANEL2,outline=GREEN,width=4)
        _spark(d,ax,ai_y,17,GREEN)
        af=font(24,"bold"); aw=int(af.getlength("AI")); d.text((ax-aw//2,ai_y+18),"AI",font=af,fill=WHITE)
    # person node (center, on top)
    r=60; d.ellipse([cx-r,py-r,cx+r,py+r],fill=GREEN)
    d.ellipse([cx-17,py-28,cx+17,py+6],fill=(14,15,19,255))          # head
    d.pieslice([cx-32,py+2,cx+32,py+60],180,360,fill=(14,15,19,255)) # shoulders
    pf=font(32,"bold"); pl="ผม = ผู้กำกับ"; pw=int(pf.getlength(pl))
    rounded(d,[cx-pw//2-16,py+r+6,cx+pw//2+16,py+r+6+44],20,fill=(0,0,0,185))
    d.text((cx-pw//2,py+r+12),pl,font=pf,fill=WHITE)
    if a<1: layer=_fade(layer,a)
    base.alpha_composite(layer)

CARDS={"skillmd":card_skillmd,"arrow":card_arrow,"claudechat":card_claudechat,
       "excel":card_excel,"browser":card_browser,"proof":card_proof,
       "checklist":card_checklist,"network":card_network}

def draw(img, t, style):
    for win in T.INSERTS:
        an=_panel_anim(t, win)
        if not an: continue
        dx,a,_=an
        CARDS[win[2]](img, t, win, dx, a)
