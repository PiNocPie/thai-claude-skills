---
name: research-question-th
description: กำหนด RQ ที่ดี testable + relevant | สำหรับ นักศึกษา. Triggers when user says (Thai/EN): 'research question', 'คำถามวิจัย'
---

# ตั้ง research question

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/tree/main/skills/research-question) · License: MIT

## ทำอะไรได้

กำหนด RQ ที่ดี testable + relevant

## เหมาะกับใคร

นักศึกษา ป.ตรี/โท/เอก ที่กำลังทำวิจัยหรือ thesis

ใช้ตอน:

- อ่าน paper ภาษาอังกฤษไม่ทัน
- ที่ปรึกษาให้ revise งานแต่ไม่รู้จะเริ่มตรงไหน
- ใกล้ deadline แต่ section ยังว่าง

## บอก Claude ยังไง

แค่พิมพ์เป็นภาษาไทยปกติ ไม่ต้องจำชื่อ skill เพราะ Claude จะหยิบใช้เองตาม trigger ที่กำหนดไว้

ตัวอย่าง:

```
"ช่วยตั้ง research question ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"คำถามวิจัย สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

อย่า copy ไปวาง thesis ตรงๆ = plagiarism, ใช้เป็นแนวทาง แล้วเขียนใหม่ด้วยภาษาคุณเอง พร้อมอ้างอิง

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
