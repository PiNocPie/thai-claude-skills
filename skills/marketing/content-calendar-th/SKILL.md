---
name: content-calendar-th
description: วางแผนปฏิทิน 30 วัน แยกธีม/วัน/เวลา/platform. Use when user wants to: ปฏิทินคอนเทนต์รายเดือน. Triggers on (Thai+EN): 'content calendar', 'ปฏิทินคอนเทนต์', 'วางแผนโพสต์'
---

# ปฏิทินคอนเทนต์รายเดือน

> 🇹🇭 **ปรับมาเป็นภาษาไทย** | Adapted to Thai
> **ดัดแปลงจาก:** [OpenClaudia/openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills)
> **Skill ต้นฉบับ:** `content-calendar`
> **License:** MIT
> **หมายเหตุการแก้ไข:** แปลเป็นภาษาไทย, ปรับ trigger ให้รองรับคำไทย, ปรับตัวอย่างให้เข้ากับบริบทคนทำงาน/นักศึกษาไทย

---

## ใช้เมื่อไหร่

ใช้ skill นี้เมื่อต้องการ **ปฏิทินคอนเทนต์รายเดือน** — เหมาะกับ นักการตลาด, social media manager, freelancer

## วิธีใช้

บอก Claude ตรงๆ เช่น:

- "ช่วยปฏิทินคอนเทนต์รายเดือนให้หน่อย"
- "ทำ content-calendar ให้"
- "content calendar"

Claude จะถามข้อมูลเพิ่มเติมที่จำเป็น เช่น context, audience, goal ก่อนเริ่มทำงาน

## ขั้นตอนการทำงาน

1. **เก็บ context** — Claude จะถามข้อมูลที่จำเป็น (อย่ารีบให้คำตอบ ระบุให้ครบ)
2. **ร่างฉบับแรก** — Claude ทำ draft แรกตามโครงสร้างมาตรฐาน
3. **ปรับแก้** — รีวิวด้วยกัน ปรับ tone/รายละเอียดให้เข้ากับงาน
4. **ส่งมอบ** — output พร้อมใช้ทันที (copy ไปใช้ หรือ save เป็นไฟล์)

## Output ที่ได้

- Structured output ตามมาตรฐานของงานนี้
- ภาษาไทยเป็นหลัก (ปรับเป็นอังกฤษได้ถ้าต้องการ)
- พร้อม CTA / next step ในตอนท้าย

## ตัวอย่าง prompts ที่ใช้บ่อย

```
content calendar — บริบทคือ [อธิบายสถานการณ์]
```

```
ช่วยปฏิทินคอนเทนต์รายเดือนสำหรับ [target] — ต้องการแบบ [tone/style]
```

## ข้อควรระวัง

- ตรวจสอบ output ก่อนใช้งานจริงเสมอ — AI อาจมี factual error
- ปรับตัวอย่าง/อ้างอิงให้ตรงกับบริบทไทย (กฎหมาย, วัฒนธรรม, ตลาด)
- ถ้าใช้ในงานเชิงกฎหมาย/การเงิน/การแพทย์ — ปรึกษาผู้เชี่ยวชาญก่อน

## เครดิต

Skill นี้ดัดแปลงจาก [OpenClaudia/openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills) ภายใต้ MIT License
ดู [CREDITS.md](../../../CREDITS.md) สำหรับรายชื่อแหล่งที่มาทั้งหมด
