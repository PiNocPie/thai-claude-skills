---
name: resume-builder-th
description: Build an ATS-friendly Thai resume/CV for new graduates or career changers. Bullets use Action+Task+Result+Metric format. Supports Thai, English, and bilingual versions for both Thai and international employers. Triggers when user says (Thai/EN): 'เขียน resume', 'ทำ CV', 'เรซูเม่', 'อัพเดท resume', 'สร้างเรซูเม่', 'CV สมัครงาน', 'เด็กจบใหม่ resume'
---

# เขียน Resume / CV ภาษาไทย

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [w95/awesome-claude-corporate-skills](https://github.com/w95/awesome-claude-corporate-skills/tree/main/03-human-resources/resume-builder) · License: MIT

## ทำอะไรได้

ช่วยเขียน resume ที่ผ่านระบบ ATS (ระบบกรอง resume อัตโนมัติของบริษัท) แล้วยังโดนใจคนอ่านด้วย, bullet ทุกบรรทัดใช้สูตร **Action + Task + Result + ตัวเลข** เพื่อให้ HR เห็นค่าของคุณภายใน 6 วินาทีแรก

ทำได้ทั้ง resume ไทย, English และเวอร์ชั่น 2 ภาษาสำหรับสมัครบริษัทต่างชาติ

## เหมาะกับใคร

- **เด็กจบใหม่** ที่ไม่รู้จะเขียนยังไงให้ดึงดูดบริษัท
- **คนเปลี่ยนสายงาน** ที่อยากจัด experience ใหม่ให้ตรง role เป้าหมาย
- **คนทำงาน 2-5 ปี** ที่อยากอัพเดท resume สมัครที่ใหม่
- **คนสมัครต่างประเทศ** ที่ต้องทำ international CV (US/EU style)

## บอก Claude ยังไง

```
ช่วยเขียน resume สมัครตำแหน่ง Marketing Coordinator
ฉันเพิ่งจบ นิเทศ จุฬาฯ มีฝึกงาน agency 3 เดือน
```

```
อัพเดท resume, เปลี่ยนสายจาก Marketing ไป Product Manager
ทำ marketing ที่ Shopee 3 ปี เคยจัด launch 2 ครั้ง
อยากเน้น transferable skills
```

```
เขียน resume English version สำหรับสมัครงาน remote ที่บริษัทยุโรป
ตำแหน่ง Content Strategist
```

Claude จะถามต่อก่อนเริ่มเขียน: ตำแหน่งเป้าหมาย, JD (ถ้ามี, paste มาเลย), การศึกษา, ประสบการณ์, ทักษะ, format (ไทย/อังกฤษ/2 ภาษา), จำนวนหน้า

## สิ่งที่จะได้

1. **Resume ฉบับ Markdown**, copy ไปทำเป็น PDF ผ่าน [resume.io](https://resume.io) หรือ Canva ได้ทันที
2. **เวอร์ชัน ATS-friendly**, plain text สำหรับ paste ในระบบสมัครงานออนไลน์
3. **Cover letter ฉบับร่าง** (ถ้าขอ)
4. **Checklist ก่อนส่ง**, เช็คความถูกต้องก่อน submit

## ที่ต้องระวัง

- **อย่าโกหก**, Resume เกินจริง = โดนจับได้ตอนสัมภาษณ์ (HR ไทยเช็ค reference จริง)
- **ตัวเลขต้องอธิบายได้**, เขียน "เพิ่มยอดขาย 30%" ต้องตอบได้ว่าวัดจากอะไร เทียบกับช่วงไหน
- **ใส่รูป?**, บริษัทไทยใส่ได้; บริษัท US/UK/EU **ห้ามใส่** เพราะป้องกัน bias
- **GPA**, ใส่ถ้า ≥ 3.00, ไม่ใส่ถ้าจบมาเกิน 3 ปี

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
