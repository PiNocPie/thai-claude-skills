---
name: figma-review-th
description: review Figma + post comment อัตโนมัติ | สำหรับ designer, UX/UI หรือคนที่ต้อง . Triggers when user says (Thai/EN): 'figma review', 'ตรวจดีไซน์'
---

# review งานดีไซน์ Figma

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [shomtsm/figma-review-skill](https://github.com/shomtsm/figma-review-skill/tree/main/skills/figma-review-skill) · License: MIT

## ทำอะไรได้

review Figma + post comment อัตโนมัติ

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
"ช่วยreview งานดีไซน์ Figma ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"ตรวจดีไซน์ สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

AI ไม่เห็นรูปจริง, ใช้สำหรับ structure/heuristics ได้ แต่ visual judgment ยังต้องคน

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
