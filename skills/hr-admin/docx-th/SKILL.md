---
name: docx-th
description: สร้าง .docx + heading, TOC, table | สำหรับ HR ธุรการ หรือผู้จัดการที่ต้อง. Triggers when user says (Thai/EN): 'word doc', 'docx', 'เอกสารเวิร์ด'
---

# สร้าง Word document

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) · License: Apache-2.0

## ทำอะไรได้

สร้าง .docx + heading, TOC, table

## เหมาะกับใคร

HR ธุรการ หรือผู้จัดการที่ต้องดูแลคนในทีม

ใช้ตอน:

- ต้องร่างเอกสารทางการแต่ไม่อยากเริ่มจากแผ่นเปล่า
- อยากได้ template ที่ใช้ได้จริงในบริษัทไทย
- ต้องส่งงานวันนี้แต่ยังไม่มีโครง

## บอก Claude ยังไง

แค่พิมพ์เป็นภาษาไทยปกติ ไม่ต้องจำชื่อ skill เพราะ Claude จะหยิบใช้เองตาม trigger ที่กำหนดไว้

ตัวอย่าง:

```
"ช่วยสร้าง Word document ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"เอกสารเวิร์ด สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

เช็คกฎหมายแรงงานไทยก่อนใช้จริง, บางอย่าง template ฝรั่งไม่ตรงกับ พ.ร.บ. ไทย

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
