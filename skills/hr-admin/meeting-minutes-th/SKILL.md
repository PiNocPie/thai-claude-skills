---
name: meeting-minutes-th
description: minutes มี action items + owner + deadline | สำหรับ HR ธุรการ หรือผู้จัดการที่ต้อง. Triggers when user says (Thai/EN): 'สรุปประชุม', 'meeting minutes'
---

# สรุปประชุม

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/tree/main/skills/meeting-minutes) · License: MIT

## ทำอะไรได้

minutes มี action items + owner + deadline

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
"ช่วยสรุปประชุม ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"สรุปประชุม สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

เช็คกฎหมายแรงงานไทยก่อนใช้จริง, บางอย่าง template ฝรั่งไม่ตรงกับ พ.ร.บ. ไทย

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
