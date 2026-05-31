---
name: daily-standup-th
description: format yesterday/today/blocker | สำหรับ พนักงานออฟฟิศที่อยากทำงานเร็วข. Triggers when user says (Thai/EN): 'standup', 'daily update'
---

# Daily standup update

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/tree/main/skills/daily-standup) · License: MIT

## ทำอะไรได้

format yesterday/today/blocker

## เหมาะกับใคร

พนักงานออฟฟิศที่อยากทำงานเร็วขึ้น ไม่ว่าจะตำแหน่งไหน

ใช้ตอน:

- งานล้น ไม่รู้ทำอะไรก่อน
- ต้องเขียนเอกสารซ้ำๆ ทุกสัปดาห์ อยากให้มีระบบ
- ประชุมเยอะ ตามไม่ทัน อยากได้สรุปดีๆ

## บอก Claude ยังไง

แค่พิมพ์เป็นภาษาไทยปกติ ไม่ต้องจำชื่อ skill เพราะ Claude จะหยิบใช้เองตาม trigger ที่กำหนดไว้

ตัวอย่าง:

```
"ช่วยDaily standup update ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"standup สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

AI ไม่รู้บริบทภายในทีม/บริษัทคุณ ใส่ context ให้ครบจะได้คำตอบที่ใช้ได้จริง

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
