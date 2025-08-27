# ตัวอย่างที่ 6: ฟีเจอร์ขั้นสูงของ Cursor
# ฟีเจอร์เหล่านี้จะช่วยให้การเขียนโค้ดมีประสิทธิภาพมากขึ้น

"""
ฟีเจอร์ขั้นสูงของ Cursor:

1. Chat with Codebase (Ctrl+Shift+L)
   - ถามคำถามเกี่ยวกับโปรเจคทั้งหมด
   - หาฟังก์ชันหรือคลาสที่ต้องการ
   - เข้าใจโครงสร้างโค้ดใหญ่ๆ

2. การใช้ @ mentions
   - @filename - อ้างอิงไฟล์เฉพาะ
   - @folder - อ้างอิงโฟลเดอร์
   - @url - อ้างอิง URL หรือ documentation

3. Rules และ Instructions
   - ตั้งกฎการเขียนโค้ดสำหรับโปรเจค
   - กำหนด coding style
   - ระบุ framework และ library ที่ใช้

4. Multi-file Editing
   - แก้ไขหลายไฟล์พร้อมกัน
   - Refactor ข้ามไฟล์
   - การ import และ export อัตโนมัติ
"""

# ตัวอย่างการใช้ @ mentions ใน Chat:

"""
ตัวอย่างคำสั่งที่ใช้ @ mentions:

1. "@main.py ช่วยอธิบายโครงสร้างของไฟล์นี้"

2. "@models/ สร้าง User model ใหม่ในโฟลเดอร์นี้"

3. "@https://docs.python.org/3/library/datetime.html 
   ช่วยแปลง datetime string ตาม documentation นี้"

4. "@package.json เพิ่ม dependency ใหม่"

5. "@tests/ เขียน test cases สำหรับฟังก์ชันใหม่ที่สร้าง"
"""

# ตัวอย่างการใช้ Rules (สร้างไฟล์ .cursorrules ในโปรเจค)
CURSOR_RULES_EXAMPLE = """
# .cursorrules ตัวอย่าง

## Coding Style
- ใช้ Python 3.9+
- ใช้ type hints ทุกฟังก์ชัน
- ใช้ docstring รูปแบบ Google style
- ตัวแปรและฟังก์ชันใช้ snake_case
- คลาสใช้ PascalCase

## Libraries
- ใช้ FastAPI สำหรับ web framework
- ใช้ Pydantic สำหรับ data validation
- ใช้ SQLAlchemy สำหรับ ORM
- ใช้ pytest สำหรับ testing

## File Structure
- models/ สำหรับ database models
- routes/ สำหรับ API endpoints
- services/ สำหรับ business logic
- tests/ สำหรับ test files

## Error Handling
- ใช้ try-except สำหรับ error handling
- สร้าง custom exceptions เมื่อจำเป็น
- log errors ด้วย logging module
"""

# ตัวอย่างการใช้ Chat with Codebase
"""
คำถามที่เหมาะสำหรับ Chat with Codebase:

1. "มีฟังก์ชันไหนบ้างที่เกี่ยวข้องกับการจัดการผู้ใช้?"

2. "โครงสร้างของโปรเจคนี้เป็นอย่างไร?"

3. "มีไฟล์ configuration อยู่ที่ไหน?"

4. "ฟังก์ชัน calculate_price ถูกเรียกใช้ที่ไหนบ้าง?"

5. "มี duplicate code ในโปรเจคนี้ไหม?"

6. "แนะนำการปรับปรุงโครงสร้างโค้ด"
"""

# ตัวอย่างการใช้งานกับ Multiple Files
class DatabaseManager:
    """
    เมื่อใช้ AI สร้างคลาสนี้ AI จะสร้างไฟล์เพิ่มเติม:
    - models.py สำหรับ database models
    - migrations/ สำหรับ database migrations
    - config.py สำหรับ database configuration
    """
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
    
    def connect(self):
        """เชื่อมต่อฐานข้อมูล"""
        pass
    
    def execute_query(self, query: str):
        """รัน SQL query"""
        pass

# ตัวอย่างการใช้ Context-aware suggestions
def process_user_data():
    """
    AI จะแนะนำโค้ดโดยดูจาก:
    1. ไฟล์อื่นในโปรเจค
    2. Import statements
    3. โครงสร้างโค้ดที่มีอยู่
    4. Pattern ที่ใช้ในโปรเจค
    """
    # เมื่อพิมพ์ user. AI จะแนะนำ method ที่มีในคลาส User
    # เมื่อพิมพ์ db. AI จะแนะนำ method ที่มีในคลาส Database
    pass

"""
เคล็ดลับการใช้งานขั้นสูง:

1. ใช้ Chat with Codebase ก่อนเริ่มงานใหม่
   - ทำความเข้าใจโครงสร้างโค้ด
   - หาฟังก์ชันที่มีอยู่แล้วไม่ให้เขียนซ้ำ

2. ตั้งค่า Rules ให้เหมาะกับโปรเจค
   - กำหนด coding style
   - ระบุ libraries ที่ใช้
   - กำหนดโครงสร้างไฟล์

3. ใช้ @ mentions อย่างชาญฉลาด
   - อ้างอิงไฟล์ที่เกี่ยวข้อง
   - ใช้ documentation URLs
   - ระบุโฟลเดอร์เป้าหมาย

4. Refactor อย่างปลอดภัย
   - ใช้ AI ช่วย refactor code
   - ขอให้สร้าง test ก่อน refactor
   - ตรวจสอบ impact ข้ามไฟล์

5. การทำงานเป็นทีม
   - แชร์ .cursorrules กับทีม
   - ใช้ consistent naming convention
   - สร้าง documentation ด้วย AI
"""