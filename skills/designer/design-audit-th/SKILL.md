---
name: design-audit-th
description: ตรวจตาม 19 professional design rules. Use when user wants to: audit ดีไซน์ 19 rules. Triggers on (Thai+EN): 'design audit', 'ตรวจดีไซน์'
---

# audit ดีไซน์ 19 rules

> 🇹🇭 **ปรับมาเป็นภาษาไทย** | Adapted to Thai
> **ดัดแปลงจาก:** [Ashutos1997/claude-design-auditor-skill](https://github.com/Ashutos1997/claude-design-auditor-skill)
> **Skill ต้นฉบับ:** `claude-design-auditor`
> **License:** MIT
> **หมายเหตุการแก้ไข:** แปลเป็นภาษาไทย, ปรับ trigger ให้รองรับคำไทย, ปรับตัวอย่างให้เข้ากับบริบทคนทำงาน/นักศึกษาไทย

---

## ใช้เมื่อไหร่

ใช้ skill นี้เมื่อต้องการ **audit ดีไซน์ 19 rules** — เหมาะกับ designer, UX/UI, product designer

## วิธีใช้

บอก Claude ตรงๆ เช่น:

- "ช่วยaudit ดีไซน์ 19 rulesให้หน่อย"
- "ทำ claude-design-auditor ให้"
- "design audit"

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
design audit — บริบทคือ [อธิบายสถานการณ์]
```

```
ช่วยaudit ดีไซน์ 19 rulesสำหรับ [target] — ต้องการแบบ [tone/style]
```

## ข้อควรระวัง

- ตรวจสอบ output ก่อนใช้งานจริงเสมอ — AI อาจมี factual error
- ปรับตัวอย่าง/อ้างอิงให้ตรงกับบริบทไทย (กฎหมาย, วัฒนธรรม, ตลาด)
- ถ้าใช้ในงานเชิงกฎหมาย/การเงิน/การแพทย์ — ปรึกษาผู้เชี่ยวชาญก่อน

## เครดิต

Skill นี้ดัดแปลงจาก [Ashutos1997/claude-design-auditor-skill](https://github.com/Ashutos1997/claude-design-auditor-skill) ภายใต้ MIT License
ดู [CREDITS.md](../../../CREDITS.md) สำหรับรายชื่อแหล่งที่มาทั้งหมด
