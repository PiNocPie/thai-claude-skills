---
name: figma-to-code-th
description: Figma design → React/HTML 1:1 | สำหรับ designer, UX/UI หรือคนที่ต้อง . Triggers when user says (Thai/EN): 'figma to code', 'figma code'
---

# แปลง Figma เป็นโค้ด

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [openai/skills](https://github.com/openai/skills/tree/main/skills/figma-implement-design) · License: MIT

## ทำอะไรได้

Figma design → React/HTML 1:1

## เหมาะกับใคร

designer, UX/UI หรือคนที่ต้อง review งานออกแบบ

ใช้ตอน:

- มีไฟล์ Figma แต่ไม่มีเวลา review ทีละหน้า
- อยากได้ feedback แบบ structured ไม่ใช่ "สวยดี/ไม่สวย"
- ต้องส่งให้ stakeholder แต่อยากรอบคอบก่อน

## บอก Claude ยังไง

แค่พิมพ์เป็นภาษาไทยปกติ ไม่ต้องจำชื่อ skill เพราะ Claude จะหยิบใช้เองตาม trigger ที่กำหนดไว้

ตัวอย่าง:

```
"ช่วยแปลง Figma เป็นโค้ด ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"figma to code สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

AI ไม่เห็นรูปจริง, ใช้สำหรับ structure/heuristics ได้ แต่ visual judgment ยังต้องคน

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
