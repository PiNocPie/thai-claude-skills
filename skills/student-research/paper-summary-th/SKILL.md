---
name: paper-summary-th
description: Summarize academic research papers in Thai. Breaks down abstract, methods, findings, and limitations into easy-to-understand Thai. Perfect for literature review, thesis prep, or keeping up with new research. Triggers when user says (Thai/EN): 'สรุป paper', 'สรุปงานวิจัย', 'อ่าน paper', 'paper summary', 'สรุป journal', 'อธิบาย paper'
---

# สรุป Research Paper

> 🇹🇭 ดัดแปลงเป็นภาษาไทยจาก [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/tree/main/skills/paper-summarizer) · License: MIT

## ทำอะไรได้

อ่าน paper ภาษาอังกฤษให้ แล้วสรุปออกมาเป็นไทยที่เข้าใจง่าย พร้อมแยกเป็น section ตามมาตรฐาน academic, RQ, methodology, findings, limitations พร้อมข้อเสนอแนะว่าเอาไปใช้ใน thesis ของคุณได้ที่ section ไหน

ไม่ใช่แค่แปล, เป็นการ **ตีความ + ย่อ + วาง context** ให้พร้อมใช้

## เหมาะกับใคร

นักศึกษา ป.ตรี/โท/เอก โดยเฉพาะตอน:

- **อ่าน paper ภาษาอังกฤษไม่ทัน**, มี deadline แต่ paper หนา 20 หน้า
- **ทำ literature review**, ต้องสรุปหลาย paper ในรูปแบบเดียวกัน
- **เตรียมนำเสนอ journal club**, ต้องเล่าให้คนอื่นฟังภายใน 10 นาที
- **เขียน thesis**, เก็บ paper อ่านไว้ใช้เขียน background

## บอก Claude ยังไง

paste URL paper หรือ abstract แล้วบอก context:

```
สรุป paper นี้ให้หน่อย: [paste URL]
```

```
สรุป paper นี้แบบ literature review entry สำหรับ thesis เรื่อง consumer behavior:
[paste abstract]
```

```
อธิบาย paper นี้แบบเล่าให้เพื่อนฟัง, ไม่ต้องใช้ศัพท์ statistic
[paste abstract]
```

## รูปแบบที่ได้

```markdown
## [ชื่อ paper] (ปี)
ผู้เขียน: ... Journal: ... Citations: ...

🎯 คำถามวิจัย, paper ตอบคำถามอะไร
🔬 วิธีการศึกษา, design, sample, method, analysis
💡 ผลการศึกษา, 3 findings หลัก
⚖️ ข้อจำกัด, ที่ผู้เขียนยอมรับ + ที่อ่านแล้วเห็น
🔑 ใช้ใน thesis ยังไง, cite ที่ section ไหน
🧠 สรุปสั้นๆ, เล่าให้เพื่อนฟัง 2-3 ประโยค
```

## ที่ต้องระวัง

- **อย่า copy ลง thesis ตรงๆ** = plagiarism, สรุปจาก AI แล้วต้องเขียนใหม่ด้วยภาษาตัวเอง พร้อมอ้างอิง
- **AI อาจอ่าน table/figure ผิด**, ถ้า paper มี data สำคัญใน chart, ต้องเช็คเองด้วย
- **เช็ค citation count + journal ranking**, paper บางตัวเก่า/quality ต่ำ ไม่ควรใช้อ้างอิงงานสำคัญ
- **paper เก่าเกิน 5 ปี** ในสาย tech/marketing/digital อาจไม่ relevant แล้ว

---

🔙 [กลับไปดู skill ทั้งหมด](../../../README.md) · 🐛 [แจ้ง bug / ขอแก้](https://github.com/PiNocPie/thai-claude-skills/issues) · 📜 [License เต็ม](../../../CREDITS.md)
