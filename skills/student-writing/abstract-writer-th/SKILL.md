---
name: abstract-writer-th
description: abstract วิจัย 200-300 คำ | สำหรับ นักศึกษา. Triggers when user says (Thai/EN): 'abstract'
---

# เขียน abstract

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/tree/main/skills/abstract-writer) · License: MIT

## ทำอะไรได้

abstract วิจัย 200-300 คำ

## เหมาะกับใคร

นักศึกษาที่ต้องส่งรายงาน/เลคเชอร์/สอบ

ใช้ตอน:

- อาจารย์สั่งงานเสาร์อาทิตย์ต้องส่งจันทร์
- ฟังเลคเชอร์ไม่ทัน อยากได้สรุปใช้อ่านสอบ
- ต้อง present หน้าห้องแต่ไม่รู้จะเริ่มยังไง

## บอก Claude ยังไง

แค่พิมพ์เป็นภาษาไทยปกติ ไม่ต้องจำชื่อ skill เพราะ Claude จะหยิบใช้เองตาม trigger ที่กำหนดไว้

ตัวอย่าง:

```
"ช่วยเขียน abstract ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"abstract สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

ครูบางท่านใช้ AI detector, ปรับสำนวนให้เป็นเสียงตัวเอง อย่าส่ง output ดิบ

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
