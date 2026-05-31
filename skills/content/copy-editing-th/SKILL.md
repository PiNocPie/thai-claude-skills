---
name: copy-editing-th
description: line-by-line edit + ปรับ tone | สำหรับ นักเขียน คอนเทนต์ครีเอเตอร์ หร. Triggers when user says (Thai/EN): 'copy edit', 'ขัดเกลา copy'
---

# ขัดเกลา copy ทีละบรรทัด

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [OpenClaudia/openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills/tree/main/skills/copy-editing) · License: MIT

## ทำอะไรได้

line-by-line edit + ปรับ tone

## เหมาะกับใคร

นักเขียน คอนเทนต์ครีเอเตอร์ หรือคนที่อยากสร้าง personal brand

ใช้ตอน:

- นั่งหน้าจอเปล่ามาครึ่งชั่วโมงแล้วยังเขียนไม่ออก
- มีหัวข้อแล้วแต่ไม่รู้จะวางโครงยังไง
- อยากได้ first draft ไว้แก้ต่อ ไม่ต้องเริ่มจากศูนย์

## บอก Claude ยังไง

แค่พิมพ์เป็นภาษาไทยปกติ ไม่ต้องจำชื่อ skill เพราะ Claude จะหยิบใช้เองตาม trigger ที่กำหนดไว้

ตัวอย่าง:

```
"ช่วยขัดเกลา copy ทีละบรรทัด ให้หน่อย บริบทคือ [อธิบายสถานการณ์ของคุณ]"
```

```
"ขัดเกลา copy สำหรับ [กลุ่มเป้าหมาย], อยากได้แบบ [น้ำเสียง/สไตล์]"
```

Claude จะถามข้อมูลที่ยังขาด (เช่น กลุ่มเป้าหมาย น้ำเสียง บริบทธุรกิจ) ก่อนเริ่มทำงาน

## ที่ต้องระวัง

อ่านออกเสียงก่อนโพสต์เสมอ, ภาษาแปลกๆ มักโผล่ตอนอ่านดังๆ

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
