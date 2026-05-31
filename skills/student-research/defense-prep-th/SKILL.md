---
name: defense-prep-th
description: คำถาม + คำตอบที่กรรมการชอบถาม. Use when user wants to: เตรียมสอบ defense thesis. Triggers on (Thai+EN): 'thesis defense', 'สอบป้องกัน'
---

# เตรียมสอบ defense thesis

> 🇹🇭 **ปรับมาเป็นภาษาไทย** | Adapted to Thai
> **ดัดแปลงจาก:** [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
> **Skill ต้นฉบับ:** `thesis-defense`
> **License:** MIT
> **หมายเหตุการแก้ไข:** แปลเป็นภาษาไทย, ปรับ trigger ให้รองรับคำไทย, ปรับตัวอย่างให้เข้ากับบริบทคนทำงาน/นักศึกษาไทย

---

## ใช้เมื่อไหร่

ใช้ skill นี้เมื่อต้องการ **เตรียมสอบ defense thesis** — เหมาะกับ นักศึกษา ป.ตรี/โท/เอก ที่ทำวิจัยหรือ thesis

## วิธีใช้

บอก Claude ตรงๆ เช่น:

- "ช่วยเตรียมสอบ defense thesisให้หน่อย"
- "ทำ thesis-defense ให้"
- "thesis defense"

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
thesis defense — บริบทคือ [อธิบายสถานการณ์]
```

```
ช่วยเตรียมสอบ defense thesisสำหรับ [target] — ต้องการแบบ [tone/style]
```

## ข้อควรระวัง

- ตรวจสอบ output ก่อนใช้งานจริงเสมอ — AI อาจมี factual error
- ปรับตัวอย่าง/อ้างอิงให้ตรงกับบริบทไทย (กฎหมาย, วัฒนธรรม, ตลาด)
- ถ้าใช้ในงานเชิงกฎหมาย/การเงิน/การแพทย์ — ปรึกษาผู้เชี่ยวชาญก่อน

## เครดิต

Skill นี้ดัดแปลงจาก [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) ภายใต้ MIT License
ดู [CREDITS.md](../../../CREDITS.md) สำหรับรายชื่อแหล่งที่มาทั้งหมด
