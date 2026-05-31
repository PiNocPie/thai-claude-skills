# 🇹🇭 Thai Claude Skills

**คลัง SKILL.md ภาษาไทย 115+ ตัว สำหรับคนทำงาน + นักศึกษา**

ใช้กับ Claude.ai, Claude Code, Cursor, Codex, หรือ AI coding agent ตัวไหนก็ได้ที่รองรับ Agent Skills format

ฟรี · Open Source · ภาษาไทย · ใช้ได้กับงานจริง

---

## ทำไมต้องมี Repo นี้?

Skills ดีๆ มีเยอะมากบน GitHub แต่ **เป็นภาษาอังกฤษหมด** คนไทยที่อยากใช้ต้องแปล + ปรับให้เข้ากับบริบทตัวเองทุกครั้ง

Repo นี้คือ **คลังกลาง** ที่ทำให้คนไทยเริ่มใช้ Claude Skills ได้ทันที โดย:

- ✅ แปลเป็นไทยทั้งหมด
- ✅ ปรับ trigger ให้ Claude เข้าใจคำสั่งภาษาไทย
- ✅ ใส่ attribution ครบ ให้เครดิตเจ้าของต้นฉบับเสมอ
- ✅ จัดเป็นหมวดตามอาชีพ/บทบาท หาง่าย

---

## 📂 หมวดที่มี (115 skills)

### 👔 สำหรับคนทำงาน (83 skills)

| หมวด | จำนวน | สำหรับใคร |
|------|------|----------|
| [Marketing](./skills/marketing) | 20 | นักการตลาด, social media manager, freelancer |
| [Content / Copywriting](./skills/content) | 18 | นักเขียน, content creator |
| [HR / ธุรการ](./skills/hr-admin) | 15 | HR, ธุรการ, ผู้จัดการ |
| [Designer](./skills/designer) | 10 | UX/UI, product designer |
| [Data Analyst](./skills/data-analyst) | 10 | data analyst, BI |
| [Productivity / PM](./skills/productivity) | 10 | พนักงานออฟฟิศทุกตำแหน่ง |

### 🎓 สำหรับนักศึกษา (32 skills)

| หมวด | จำนวน | สำหรับใคร |
|------|------|----------|
| [วิจัย / วิชาการ](./skills/student-research) | 12 | นักศึกษา ป.ตรี/โท/เอก |
| [งานเขียน / รายงาน](./skills/student-writing) | 10 | นักศึกษาที่ต้องส่งรายงาน/สอบ |
| [เตรียมตัวทำงาน](./skills/student-career) | 10 | ฝึกงาน, จบใหม่, สมัครงาน |

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

ไม่ต้องจำชื่อ skill — Claude หยิบใช้เองตาม trigger ภาษาไทยที่กำหนดไว้

---

## 🌏 ที่มาของ Skills

Skills ทุกตัวในนี้ **ดัดแปลงมาจาก repo ต้นฉบับ** ที่ open source อยู่แล้ว เราแค่ทำหน้าที่:

1. แปลเป็นไทย
2. ปรับให้เข้ากับบริบทไทย
3. รวมไว้ในที่เดียวให้หาง่าย

ดูรายชื่อ **แหล่งที่มาทั้งหมด + license** ที่ [CREDITS.md](./CREDITS.md)

ขอบคุณ open source maintainers ทุกคน — ถ้าไม่มีพวกคุณ repo นี้คงไม่เกิด 🙏

---

## 🤝 อยากช่วยพัฒนา?

- พบ bug หรือคำผิด → เปิด [Issue](https://github.com/PiNocPie/thai-claude-skills/issues)
- มี skill อยาก contribute → ดู [CONTRIBUTING.md](./CONTRIBUTING.md)
- มี repo ภาษาอังกฤษอยากให้แปล → tag เราใน issue

---

## 📜 License

โค้ดและการแปลของ repo นี้ — MIT License

Skills แต่ละตัวอาจมี license ต่างกันตาม source — ดู [CREDITS.md](./CREDITS.md) และ LICENSE file ในแต่ละ skill folder

---

**สร้างด้วย ❤️ จากคนไทยที่อยากให้คนไทยใช้ AI ได้เก่งขึ้น**
