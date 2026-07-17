# 🇹🇭 Thai Claude Skills

**คลัง SKILL.md ภาษาไทย 67 ตัว สำหรับคนทำงาน + นักศึกษา**

ใช่ครับ 67 (ตามมีม 67) คัดมาแล้วใช้ได้จริงทุกตัว ไม่ใช่จำนวนปลอมๆ

ใช้กับ Claude.ai, Claude Code, Cursor, Codex, หรือ AI coding agent ตัวไหนก็ได้ที่รองรับ Agent Skills format

ฟรี · Open Source · ภาษาไทย · ใช้ได้กับงานจริง

---

## ⭐ ใหม่: reel-editor-th — ระบบตัดคลิป Reel ด้วย AI

นอกจาก 67 text skills มี **1 ตัวพิเศษ** ที่เป็น "ระบบจริง" ไม่ใช่แค่ prompt:

👉 **[reel-editor-th](./skills/content/reel-editor-th)** = โยนคลิปพูดหน้ากล้องให้ AI แล้วได้ **Reel 9:16 พร้อมลง** (ซับไทยคำต่อคำ · hook 3 วิแรก · การ์ดเดโม · เอฟเฟกต์เสียง · แก้สี HDR ให้เป็นสีจริง · ทำปก) โดยไม่เปิดโปรแกรมตัดต่อเลย

⚠️ ตัวนี้รันในเครื่อง ต้องมี **macOS (Apple Silicon) + Claude Code + ffmpeg + python** (ต่างจาก 67 ตัวอื่นที่ใช้บนเว็บได้เลย) วิธีใช้อยู่ใน [README ของ skill](./skills/content/reel-editor-th/README.md)

---

## ทำไมต้องมี Repo นี้?

Skills ดีๆ มีเยอะมากบน GitHub แต่ **เป็นภาษาอังกฤษหมด** คนไทยที่อยากใช้ต้องแปล + ปรับให้เข้ากับบริบทตัวเองทุกครั้ง

Repo นี้คือ **คลังกลาง** ที่ทำให้คนไทยเริ่มใช้ Claude Skills ได้ทันที โดย:

- ✅ แปลเป็นไทยทั้งหมด
- ✅ ปรับ trigger ให้ Claude เข้าใจคำสั่งภาษาไทย
- ✅ ใส่ attribution ครบ ให้เครดิตเจ้าของต้นฉบับเสมอ
- ✅ จัดเป็นหมวดตามอาชีพ/บทบาท หาง่าย

---

## 📂 หมวดที่มี (67 skills)

### 👔 สำหรับคนทำงาน (48 skills)

| หมวด | จำนวน | สำหรับใคร |
|------|------|----------|
| [Marketing](./skills/marketing) | 12 | นักการตลาด, social media manager, freelancer |
| [Content / Copywriting](./skills/content) | 11 | นักเขียน, content creator |
| [HR / ธุรการ](./skills/hr-admin) | 11 | HR, ธุรการ, ผู้จัดการ |
| [Designer](./skills/designer) | 7 | UX/UI, product designer |
| [Productivity / PM](./skills/productivity) | 7 | พนักงานออฟฟิศทุกตำแหน่ง |

### 🎓 สำหรับนักศึกษา (19 skills)

| หมวด | จำนวน | สำหรับใคร |
|------|------|----------|
| [วิจัย / วิชาการ](./skills/student-research) | 7 | นักศึกษา ป.ตรี/โท/เอก |
| [งานเขียน / รายงาน](./skills/student-writing) | 6 | นักศึกษาที่ต้องส่งรายงาน/สอบ |
| [เตรียมตัวทำงาน](./skills/student-career) | 6 | ฝึกงาน, จบใหม่, สมัครงาน |

> **อยากได้ Data Analyst skills?** กำลังขออนุญาตจาก source repo อยู่ จะเพิ่มเร็วๆ นี้ ติดตามได้

---

## 🚀 เริ่มใช้ใน 30 วินาที

### วิธีที่ 1: Claude Code (ง่ายสุด)

```bash
/plugin marketplace add PiNocPie/thai-claude-skills
```

### วิธีที่ 2: copy เอาเฉพาะ skill ที่อยากใช้

```bash
# clone repo
git clone https://github.com/PiNocPie/thai-claude-skills.git

# copy skill ที่ต้องการไปยัง Claude folder
cp -r thai-claude-skills/skills/marketing/social-content-th ~/.claude/skills/
```

### วิธีที่ 3: ใช้กับ Claude.ai (web/app)

1. เปิด skill ที่อยากใช้ เช่น `skills/marketing/social-content-th/SKILL.md`
2. copy เนื้อหาทั้งหมด
3. เริ่มบทสนทนาใหม่ใน Claude.ai แล้ว paste เป็นข้อความแรก

---

## 🎯 ตัวอย่างการใช้

หลังติดตั้งแล้ว แค่บอก Claude เป็นภาษาไทย:

```
"ช่วยเขียน JD ตำแหน่ง Marketing Manager หน่อย"
→ Claude เรียก jd-writer-th อัตโนมัติ

"สรุป paper อันนี้ให้หน่อย: [paste url]"
→ Claude เรียก paper-summary-th อัตโนมัติ

"เขียน resume สำหรับเด็กจบใหม่สาย data analyst"
→ Claude เรียก resume-builder-th อัตโนมัติ
```

ไม่ต้องจำชื่อ skill เพราะ Claude หยิบใช้เองตาม trigger ภาษาไทยที่กำหนดไว้

---

## 🌏 ที่มาของ Skills

Skills ทุกตัวในนี้ **ดัดแปลงมาจาก repo ต้นฉบับ** ที่ open source อยู่แล้ว เราแค่ทำหน้าที่:

1. แปลเป็นไทย
2. ปรับให้เข้ากับบริบทไทย
3. รวมไว้ในที่เดียวให้หาง่าย

ดูรายชื่อ **แหล่งที่มาทั้งหมด + license** ที่ [CREDITS.md](./CREDITS.md)

ขอบคุณ open source maintainers ทุกคน ถ้าไม่มีพวกคุณ repo นี้คงไม่เกิด 🙏

---

## 🤝 อยากช่วยพัฒนา?

- พบ bug หรือคำผิด → เปิด [Issue](https://github.com/PiNocPie/thai-claude-skills/issues)
- มี skill อยาก contribute → ดู [CONTRIBUTING.md](./CONTRIBUTING.md)
- มี repo ภาษาอังกฤษอยากให้แปล → tag เราใน issue

---

## 📬 ติดต่อ

อยากให้ช่วยทำ AI workflow / custom skill ให้ทีมหรือบริษัท · มีโปรเจกอยากชวนคุย · อยากให้ไปพูด/workshop

📧 **panupong.workcontact [at] gmail.com**

(บอกในอีเมลด้วยว่าเห็นจาก repo นี้ จะได้ตอบเร็วขึ้น)

---

## 📜 License

โค้ดและการแปลของ repo นี้ใช้ MIT License

Skills แต่ละตัวอาจมี license ต่างกันตาม source ดู [CREDITS.md](./CREDITS.md) และ LICENSE file ในแต่ละ skill folder

---

**สร้างด้วย ❤️ จากคนไทยที่อยากให้คนไทยใช้ AI ได้เก่งขึ้น**
