---
name: salary-negotiation-th
description: script + tactic ต่อรอง | สำหรับ นักศึกษา. Triggers when user says (Thai/EN): 'ต่อรองเงินเดือน', 'salary negotiation'
---

# ต่อรองเงินเดือน

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/tree/main/skills/salary-negotiation) · License: MIT

## ทำอะไรได้

script + tactic ต่อรอง

## เหมาะกับใคร

นักศึกษาปีสูง / เด็กจบใหม่ ที่กำลังหางาน ฝึกงาน หรือสมัครต่อ

ใช้ตอน:

- เพิ่งจบ ไม่เคยเขียน resume มาก่อน
- จะสัมภาษณ์อาทิตย์หน้า ตื่นเต้น อยากซ้อม
- อยากต่อ ป.โท แต่ไม่รู้จะเขียน statement ยังไง

## บอก Claude ยังไง

แค่พิมพ์เป็นภาษาไทยปกติ ไม่ต้องจำชื่อ skill เพราะ Claude จะหยิบใช้เองตาม trigger ที่กำหนดไว้

ตัวอย่าง:

```
"ช่วยต่อรองเงินเดือน ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"ต่อรองเงินเดือน สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

ตัวเลข achievement ใน resume ต้องอธิบายได้ตอนสัมภาษณ์ อย่าใส่ที่ตอบไม่ได้

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
