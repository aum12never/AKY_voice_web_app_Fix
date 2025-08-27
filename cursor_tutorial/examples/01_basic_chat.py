# ตัวอย่างที่ 1: การใช้งาน AI Chat พื้นฐาน
# กด Ctrl+L เพื่อเปิด AI Chat และลองถามคำถามเหล่านี้

"""
ตัวอย่างคำถามที่ควรถาม AI ใน Chat:

1. "อธิบายโค้ด Python นี้ให้หน่อย"
2. "ช่วยเพิ่ม docstring ให้ฟังก์ชันนี้"
3. "มีวิธีเขียนโค้ดนี้ให้สั้นลงไหม"
4. "ช่วยหา bug ในโค้ดนี้"
5. "แนะนำการปรับปรุงโค้ดนี้"
"""

def calculate_area(length, width):
    # ฟังก์ชันคำนวณพื้นที่
    return length * width

def greet_user(name):
    # ฟังก์ชันทักทาย
    if name:
        return f"สวัสดี {name}!"
    else:
        return "สวัสดี!"

# ลองเลือกโค้ดข้างบนแล้วถาม AI ว่า:
# - "ช่วยเพิ่ม type hints ให้โค้ดนี้"
# - "ช่วยเพิ่ม error handling"
# - "ทำให้โค้ดนี้ดีขึ้น"

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

# ลองถาม AI:
# "ช่วยเพิ่มเมธอด subtract และ divide ให้ class นี้"