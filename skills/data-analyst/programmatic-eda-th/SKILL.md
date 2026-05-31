---
name: programmatic-eda-th
description: exploratory data analysis ครบ sanity check. Use when user wants to: EDA อัตโนมัติ. Triggers on (Thai+EN): 'EDA', 'สำรวจข้อมูล'
---

# EDA อัตโนมัติ

> 🇹🇭 **ปรับมาเป็นภาษาไทย** | Adapted to Thai
> **ดัดแปลงจาก:** [nimrodfisher/data-analytics-skills](https://github.com/nimrodfisher/data-analytics-skills)
> **Skill ต้นฉบับ:** `01-data-quality-validation/programmatic-eda`
> **License:** Permission requested
> **หมายเหตุการแก้ไข:** แปลเป็นภาษาไทย, ปรับ trigger ให้รองรับคำไทย, ปรับตัวอย่างให้เข้ากับบริบทคนทำงาน/นักศึกษาไทย

---

## ใช้เมื่อไหร่

ใช้ skill นี้เมื่อต้องการ **eda อัตโนมัติ** — เหมาะกับ data analyst, BI, marketing analyst

## วิธีใช้

บอก Claude ตรงๆ เช่น:

- "ช่วยeda อัตโนมัติให้หน่อย"
- "ทำ 01-data-quality-validation/programmatic-eda ให้"
- "EDA"

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
EDA — บริบทคือ [อธิบายสถานการณ์]
```

```
ช่วยeda อัตโนมัติสำหรับ [target] — ต้องการแบบ [tone/style]
```

## ข้อควรระวัง

- ตรวจสอบ output ก่อนใช้งานจริงเสมอ — AI อาจมี factual error
- ปรับตัวอย่าง/อ้างอิงให้ตรงกับบริบทไทย (กฎหมาย, วัฒนธรรม, ตลาด)
- ถ้าใช้ในงานเชิงกฎหมาย/การเงิน/การแพทย์ — ปรึกษาผู้เชี่ยวชาญก่อน

## เครดิต

Skill นี้ดัดแปลงจาก [nimrodfisher/data-analytics-skills](https://github.com/nimrodfisher/data-analytics-skills) ภายใต้ Permission requested License
ดู [CREDITS.md](../../../CREDITS.md) สำหรับรายชื่อแหล่งที่มาทั้งหมด
