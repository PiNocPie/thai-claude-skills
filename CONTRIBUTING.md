# Contributing Guide

ขอบคุณที่อยากช่วยพัฒนา Thai Claude Skills! 🙏

## วิธี contribute

### 1. แก้ skill ที่มีอยู่ (typo, ปรับ tone, เพิ่มตัวอย่าง)

1. Fork repo
2. แก้ไฟล์ `skills/<หมวด>/<skill-name>/SKILL.md`
3. ทดสอบกับ Claude จริงดูว่า trigger ใช้งานได้
4. ส่ง PR พร้อมอธิบายว่าแก้อะไร

### 2. เพิ่ม skill ใหม่

**ขั้นตอน:**

1. เช็คก่อนว่ายังไม่มีใน repo
2. สร้าง folder ใหม่: `skills/<หมวด>/<skill-name>-th/`
3. สร้างไฟล์ `SKILL.md` ตามรูปแบบมาตรฐาน (ดูตัวอย่างจาก skill อื่น)

**SKILL.md ที่ดีต้องมี:**

```markdown
---
name: skill-name-th
description: คำอธิบายภาษาอังกฤษ (สำคัญ!) + Triggers ทั้งไทยและอังกฤษ
---

# ชื่อ Skill ภาษาไทย

> Attribution block ที่ครบ (source, license, การแก้ไข)

## ใช้เมื่อไหร่
## วิธีใช้
## ขั้นตอนการทำงาน
## Output ที่ได้
## ตัวอย่าง prompts
## ข้อควรระวัง
## เครดิต
```

**กฎสำคัญ:**

- `description:` ใน frontmatter **ต้องเป็นภาษาอังกฤษ** (Claude trigger ได้แม่นกว่า) แต่ใส่ trigger ภาษาไทยรวมเข้าไปด้วย
- เนื้อหาด้านในเขียนภาษาไทยล้วน
- ตั้งชื่อ folder/file เป็น kebab-case ภาษาอังกฤษ
- ใส่ `-th` ต่อท้ายชื่อ skill เสมอ
- ถ้าดัดแปลงมาจาก repo อื่น **ต้องใส่ attribution ครบ** (source URL, license, แก้อะไร)

### 3. รายงานปัญหา / ขอ skill ใหม่

เปิด [Issue](../../issues) พร้อมข้อมูล:

- **สำหรับ bug**: skill ตัวไหน, ทำอะไรแล้วเกิดอะไร, คาดหวังอะไร
- **สำหรับ feature request**: อยากได้ skill อะไร, ทำงานอย่างไร, มี repo อังกฤษเป็น reference ไหม

## License Compliance — สำคัญที่สุด

ก่อนเอา skill จาก repo อื่นมา ต้องเช็ค:

1. **มี LICENSE ไหม** — ถ้าไม่มี = "All Rights Reserved" ห้ามใช้โดยไม่ขออนุญาต
2. **License ประเภทอะไร** — MIT/Apache 2.0/BSD = ใช้ได้ถ้าให้เครดิต; GPL = ต้องระวัง; CC-BY-NC = ใช้ commercial ไม่ได้
3. **ใส่ attribution** — ทุก skill ที่ดัดแปลงต้องระบุ source + author + license + การแก้ไข

ถ้าไม่แน่ใจ → ถามใน Issue ก่อน

## Style Guide

- ใช้ภาษาไทยกระชับ ตรงประเด็น ไม่ต้องเป็นทางการเกินไป
- ใช้คำที่คนทำงาน/นักศึกษาเข้าใจ ไม่ใช้ศัพท์ technical เกินจำเป็น
- ตัวอย่างต้องเป็นบริบทไทย (เช่น ตำแหน่งงาน, ชื่อมหาวิทยาลัย, เงินเดือนเป็นบาท)

ขอบคุณที่ช่วยทำให้คนไทยใช้ AI ได้เก่งขึ้น 🇹🇭
