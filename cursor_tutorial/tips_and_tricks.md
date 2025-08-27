# Tips และ Tricks สำหรับ Cursor

## 🎯 เทคนิคการเขียน Prompt ที่ดี

### ✅ ควรทำ
```
"สร้างฟังก์ชัน Python ที่รับ list ของตัวเลข และคืนค่าเฉลี่ย พร้อม error handling สำหรับ empty list"
```

### ❌ ไม่ควรทำ
```
"สร้างฟังก์ชัน"
```

## 🚀 Shortcuts ที่ต้องจำ

| Shortcut | ฟังก์ชัน | เมื่อไหร่ใช้ |
|----------|----------|-------------|
| `Ctrl+L` | AI Chat | ถามคำถาม, ขอคำแนะนำ |
| `Ctrl+K` | Inline Edit | แก้ไขโค้ดที่เลือก |
| `Ctrl+I` | Composer | สร้างฟีเจอร์ใหม่, หลายไฟล์ |
| `Ctrl+Shift+L` | Chat with Codebase | ถามเกี่ยวกับโปรเจค |
| `Tab` | Accept Suggestion | รับข้อเสนอแนะ AI |
| `Ctrl+→` | Accept Word | รับเฉพาะคำถัดไป |
| `Escape` | Reject Suggestion | ปฏิเสธข้อเสนอแนะ |

## 💡 เคล็ดลับการใช้งาน

### 1. การจัดการ Context
- เปิดไฟล์ที่เกี่ยวข้องก่อนใช้ AI
- ใช้ `@filename` เพื่ออ้างอิงไฟล์เฉพาะ
- ใช้ `@folder/` เพื่ออ้างอิงโฟลเดอร์

### 2. การใช้งานกับโปรเจคใหญ่
```
# ดี: ระบุ context ที่ชัดเจน
"@models/user.py ช่วยเพิ่มเมธอด update_password ให้ User model"

# ไม่ดี: ไม่ระบุ context
"เพิ่มเมธอด update_password"
```

### 3. การ Debug มีประสิทธิภาพ
1. Copy error message ทั้งหมด
2. วาง error ใน Chat พร้อมโค้ดที่เกี่ยวข้อง
3. ขอให้ AI อธิบายสาเหตุและแนะนำวิธีแก้ไข

### 4. การ Refactor อย่างปลอดภัย
1. สร้าง backup หรือ commit ก่อน
2. ใช้ Composer สำหรับ refactor ใหญ่
3. ขอให้ AI สร้าง test ก่อน refactor

## 🎨 การปรับแต่งการใช้งาน

### ตั้งค่า .cursorrules
```
# สร้างไฟล์ .cursorrules ในโปรเจค

## Programming Language
- Use Python 3.9+
- Always include type hints
- Use descriptive variable names

## Code Style
- Functions use snake_case
- Classes use PascalCase
- Constants use UPPER_CASE
- Use Google-style docstrings

## Error Handling
- Always handle potential errors
- Use specific exception types
- Log errors appropriately

## Testing
- Write unit tests for all functions
- Use pytest framework
- Aim for 80%+ test coverage
```

### การใช้ Custom Instructions
- อธิบายโปรเจคและเทคโนโลยีที่ใช้
- ระบุ coding standard ที่ต้องการ
- กำหนดโครงสร้างไฟล์ที่ต้องการ

## 🔧 การแก้ปัญหาที่พบบ่อย

### AI ไม่เข้าใจ context
**วิธีแก้:**
- เปิดไฟล์ที่เกี่ยวข้องใน editor
- ใช้ `@filename` อ้างอิงไฟล์
- ให้ context เพิ่มเติมในคำถาม

### AI generate โค้ดผิด
**วิธีแก้:**
- เขียน prompt ให้ชัดเจนขึ้น
- ให้ตัวอย่าง input/output ที่ต้องการ
- ระบุ constraints และ requirements

### Suggestion ช้า
**วิธีแก้:**
- ปิด/เปิด Cursor ใหม่
- ตรวจสอบ internet connection
- ลดจำนวนไฟล์ที่เปิดพร้อมกัน

## 📚 การเรียนรู้อย่างต่อเนื่อง

### ฝึกใช้งานประจำ
1. **วันแรก:** ใช้ Chat และ Code Generation
2. **สัปดาห์แรก:** ฝึกใช้ Inline Editing
3. **เดือนแรก:** เรียนรู้ Composer และ Advanced Features
4. **ต่อไป:** สร้าง workflow ที่เหมาะกับงาน

### ทดลองกับโปรเจคจริง
- เริ่มจากงานเล็กๆ
- ค่อยๆ ใช้กับงานซับซ้อนขึ้น
- แชร์ประสบการณ์กับทีม

### ติดตามอัปเดต
- อ่าน release notes ของ Cursor
- เรียนรู้ feature ใหม่ๆ
- ลองใช้ AI models ใหม่

## 🏆 Best Practices

### การทำงานเป็นทีม
1. **แชร์ .cursorrules** กับทีมงาน
2. **ตั้ง coding standard** ร่วมกัน
3. **สอนการใช้งาน** ให้สมาชิกใหม่
4. **Review โค้ดที่ AI generate** ก่อน commit

### การรักษาคุณภาพโค้ด
1. **ไม่ยอมรับ suggestion ทุกอัน** - ใช้วิจารณญาณ
2. **Review และ test** โค้ดที่ AI สร้าง
3. **เรียนรู้จากโค้ดที่ AI สร้าง** - ทำความเข้าใจ pattern
4. **ปรับปรุงอย่างต่อเนื่อง** - ให้ feedback กับ AI

### การประหยัดเวลา
1. **ใช้ Composer** สำหรับงานใหม่
2. **ใช้ Chat with Codebase** เพื่อทำความเข้าใจโปรเจค
3. **เตรียม template** สำหรับงานประจำ
4. **สร้าง shortcuts** สำหรับคำสั่งที่ใช้บ่อย