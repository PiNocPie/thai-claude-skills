---
name: interview-protocol-th
description: qualitative interview guide. Use when user wants to: protocol สัมภาษณ์เชิงคุณภาพ. Triggers on (Thai+EN): 'qualitative interview', 'สัมภาษณ์เชิงลึก'
---

# protocol สัมภาษณ์เชิงคุณภาพ

> 🇹🇭 **ปรับมาเป็นภาษาไทย** | Adapted to Thai
> **ดัดแปลงจาก:** [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
> **Skill ต้นฉบับ:** `qualitative-interview`
> **License:** MIT
> **หมายเหตุการแก้ไข:** แปลเป็นภาษาไทย, ปรับ trigger ให้รองรับคำไทย, ปรับตัวอย่างให้เข้ากับบริบทคนทำงาน/นักศึกษาไทย

---

## ใช้เมื่อไหร่

ใช้ skill นี้เมื่อต้องการ **protocol สัมภาษณ์เชิงคุณภาพ** — เหมาะกับ นักศึกษา ป.ตรี/โท/เอก ที่ทำวิจัยหรือ thesis

## วิธีใช้

บอก Claude ตรงๆ เช่น:

- "ช่วยprotocol สัมภาษณ์เชิงคุณภาพให้หน่อย"
- "ทำ qualitative-interview ให้"
- "qualitative interview"

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
qualitative interview — บริบทคือ [อธิบายสถานการณ์]
```

```
ช่วยprotocol สัมภาษณ์เชิงคุณภาพสำหรับ [target] — ต้องการแบบ [tone/style]
```

## ข้อควรระวัง

- ตรวจสอบ output ก่อนใช้งานจริงเสมอ — AI อาจมี factual error
- ปรับตัวอย่าง/อ้างอิงให้ตรงกับบริบทไทย (กฎหมาย, วัฒนธรรม, ตลาด)
- ถ้าใช้ในงานเชิงกฎหมาย/การเงิน/การแพทย์ — ปรึกษาผู้เชี่ยวชาญก่อน

## เครดิต

Skill นี้ดัดแปลงจาก [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) ภายใต้ MIT License
ดู [CREDITS.md](../../../CREDITS.md) สำหรับรายชื่อแหล่งที่มาทั้งหมด
