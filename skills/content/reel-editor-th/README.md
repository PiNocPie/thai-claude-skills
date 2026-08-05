# 🎬 reel-editor-th : ระบบตัดคลิป Reel ภาษาไทยด้วย AI

เปลี่ยนคลิปพูดหน้ากล้อง 1 คน (ถ่ายมือถือแนวตั้ง) ให้เป็น **Reel 9:16 พร้อมลง** แบบทำมาเพื่อไวรัล:
ซับไทยคำต่อคำ ไฮไลต์คีย์เวิร์ด · hook 3 วิแรก · การ์ด/mockup โชว์เดโม · เอฟเฟกต์เสียง · ปกคลิป · แก้สีจาก HDR ให้เป็นสีจริง

> นี่คือ **ระบบจริงที่ผมใช้ตัดคลิปในช่องตัวเอง** ทุกคลิป ไม่ได้เปิดโปรแกรมตัดต่อเลย
> โดย [@kin3th](https://instagram.com/kin3th) · AI ง่ายนิดเดียว

---

## ⚠️ อ่านก่อน: skill นี้ไม่เหมือน 67 ตัวอื่น

67 skills อื่นในรีโปนี้เป็น **text skill** ใช้บน Claude.ai เว็บได้เลย
แต่ **reel-editor-th เป็น skill ที่รันเครื่องมือในเครื่อง (local tooling)** ต้องมีของพวกนี้ก่อน:

| ต้องมี | ใช้ทำอะไร |
|--------|-----------|
| **macOS + Apple Silicon** (M1 ขึ้นไป) | tonemap HDR (Swift/AVFoundation) + mlx-whisper |
| **Claude Code** (ไม่ใช่เว็บ) | ให้ Claude รันสคริปต์ให้ |
| **ffmpeg** (`brew install ffmpeg`) | ตัดต่อ/ประกอบวิดีโอ |
| **python3 + Pillow** (`pip install pillow`) | เรนเดอร์ซับ/การ์ด (PNG overlay) |
| **mlx-whisper** (`pip install mlx-whisper`) | ถอดเสียงไทยคำต่อคำ |
| **ฟอนต์ Sukhumvit Set** | มากับ macOS อยู่แล้ว |

> ไม่ใช่ Mac / ไม่มี Claude Code? ใช้ skill นี้ไม่ได้ครับ (แต่ 67 ตัวอื่นใช้ได้หมด)

---

## 🚀 เริ่มใช้

```bash
# copy skill เข้า Claude folder
cp -r thai-claude-skills/skills/content/reel-editor-th ~/.claude/skills/

# แล้วใน Claude Code แค่โยนคลิปให้ + บอก
"ทำ reel จากคลิปนี้ให้หน่อย"
```

Claude จะทำตาม `SKILL.md`: ถอดเสียง → เขียน `timeline.py` → รัน `build.sh` → ได้ `reel_clean.mp4` + ปก

## 🧠 มันทำอะไรให้บ้าง
- **ตัด/ต่อ** คลิปให้กระชับ + ซูมเข้าเบาๆ (push-in)
- **ซับไทยคำต่อคำ** ไฮไลต์เฉพาะคำสำคัญด้วยสี accent (ปรับได้ต่อคลิปผ่าน `timeline.ACCENT`)
- **การ์ด/mockup** เลื่อนเข้าเหนือหัว (browser, แชท AI, ขั้นตอน, editor, ตาราง, แถบหลักฐานคลิปเก่า, เช็กลิสต์, โครงข่าย AI) ไม่บังหน้า
- **เอฟเฟกต์เสียง** (ไม่ใช่เพลง): whoosh ตอนการ์ดเข้า, pop ตอนนับเลข, chime ตอนเฉลย, impact ตอนพันช์
- **แก้สี HDR → สีจริง** ธรรมชาติ (ไม่ใส่ฟิลเตอร์/ไม่เกรด)
- **ปกคลิป** ให้พร้อม

## 📁 ไฟล์
```
SKILL.md                 # Claude อ่านตัวนี้เป็นหลัก
scripts/build.sh         # ประกอบทั้งหมด
scripts/tonemap.swift    # HDR->SDR (คอมไพล์ครั้งแรกอัตโนมัติ)
scripts/render_*.py      # ซับ / การ์ด / ปก / overlay
scripts/build_audio.py   # ผสมเอฟเฟกต์เสียงใต้เสียงพูด
scripts/timeline_template.py  # ก๊อปเป็น timeline.py ต่อคลิป
references/authoring-guide.md # วิธีเขียน timeline + จูน
```

## 🔊 หมายเหตุเรื่องเอฟเฟกต์เสียง
`build_audio.py` มองหาไฟล์ SFX จากโฟลเดอร์ SFX (ค่าเริ่มต้นชี้ไปที่ skill `hyperframes-media`) ถ้าไม่มีโฟลเดอร์นั้น ระบบจะ **ข้ามเอฟเฟกต์เสียงให้อัตโนมัติ** (ใช้เสียงพูดล้วน ไม่ error) อยากได้เสียง เอาไฟล์ `.mp3` (whoosh / pop / chime / impact) ใส่โฟลเดอร์เอง แล้วส่ง path เป็น argument ตัวที่ 3 ของ `build_audio.py`

## 📜 License
MIT · เอาไปใช้/ดัดแปลงได้ ใส่เครดิตกันนิดนึงก็ดีครับ 🙏
