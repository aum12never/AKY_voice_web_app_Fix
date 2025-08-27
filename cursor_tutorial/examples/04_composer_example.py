# ตัวอย่างที่ 4: การใช้งาน Composer (Ctrl+I)
# Composer ใช้สำหรับสร้างฟีเจอร์ใหม่หรือแก้ไขหลายไฟล์พร้อมกัน

"""
วิธีใช้ Composer:
1. กด Ctrl+I
2. อธิบายสิ่งที่ต้องการให้ AI สร้าง
3. AI จะสร้างไฟล์หรือแก้ไขไฟล์ตามที่ต้องการ
4. ตรวจสอบและอนุมัติการเปลี่ยนแปลง

ตัวอย่างคำสั่งสำหรับ Composer:
- "สร้าง REST API สำหรับจัดการผู้ใช้ด้วย FastAPI"
- "สร้างหน้าเว็บ HTML สำหรับแสดงข้อมูลสินค้า"
- "เพิ่มฟีเจอร์ authentication ให้กับแอป"
- "สร้าง unit tests สำหรับฟังก์ชันทั้งหมด"
- "ปรับปรุงโครงสร้างโค้ดให้เป็น MVC pattern"
"""

# ไฟล์นี้แสดงตัวอย่างโครงสร้างที่ Composer อาจสร้างขึ้น

class UserManager:
    """
    คลาสสำหรับจัดการผู้ใช้
    ตัวอย่างที่ Composer อาจสร้างเมื่อขอให้สร้าง user management system
    """
    
    def __init__(self):
        self.users = {}
    
    def create_user(self, username, email, password):
        """สร้างผู้ใช้ใหม่"""
        pass
    
    def authenticate_user(self, username, password):
        """ตรวจสอบการเข้าสู่ระบบ"""
        pass
    
    def get_user(self, username):
        """ดึงข้อมูลผู้ใช้"""
        pass
    
    def update_user(self, username, **kwargs):
        """อัปเดตข้อมูลผู้ใช้"""
        pass
    
    def delete_user(self, username):
        """ลบผู้ใช้"""
        pass

# เมื่อใช้ Composer AI จะสร้างไฟล์เพิ่มเติม เช่น:
# - models.py (สำหรับ data models)
# - routes.py (สำหรับ API endpoints)
# - database.py (สำหรับการเชื่อมต่อฐานข้อมูล)
# - tests.py (สำหรับ unit tests)
# - config.py (สำหรับการตั้งค่า)

"""
เทคนิคการใช้ Composer:

1. เริ่มจากการอธิบายโครงการโดยรวม
   "สร้างเว็บแอป e-commerce ด้วย Flask และ SQLite"

2. ระบุเทคโนโลยีที่ต้องการ
   "ใช้ React สำหรับ frontend และ Node.js สำหรับ backend"

3. อธิบายฟีเจอร์ที่ต้องการ
   "ต้องมี login, registration, product catalog, shopping cart"

4. ระบุโครงสร้างไฟล์
   "จัดโครงสร้างแบบ MVC pattern"

5. ขอให้เพิ่ม error handling และ validation
   "เพิ่ม input validation และ error handling ทุกที่"
"""