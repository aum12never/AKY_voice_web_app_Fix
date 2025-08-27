# แบบฝึกหัดที่ 1: การใช้งาน AI Chat และ Code Generation
# ลองทำแบบฝึกหัดเหล่านี้เพื่อฝึกใช้งาน Cursor

"""
คำแนะนำ:
1. อ่านโจทย์แต่ละข้อ
2. ใช้ AI Chat (Ctrl+L) เพื่อขอความช่วยเหลือ
3. ใช้ Code Generation (Tab) เพื่อสร้างโค้ด
4. ใช้ Inline Editing (Ctrl+K) เพื่อปรับปรุงโค้ด
"""

# แบบฝึกหัดที่ 1.1: ขอให้ AI สร้างฟังก์ชันคำนวณ BMI
# ใช้ Chat เพื่อถามว่า "สร้างฟังก์ชันคำนวณ BMI หน่อย"



# แบบฝึกหัดที่ 1.2: สร้างฟังก์ชันตรวจสอบเลขคู่-คี่
# พิมพ์ comment: "ฟังก์ชันตรวจสอบว่าตัวเลขเป็นเลขคู่หรือคี่"



# แบบฝึกหัดที่ 1.3: สร้างคลาสสำหรับจัดการรายการสินค้า
# ใช้ Composer (Ctrl+I) สั่ง: "สร้างคลาส Product ที่มี name, price, quantity"



# แบบฝึกหัดที่ 1.4: สร้างฟังก์ชันแปลงอุณหภูมิ
# พิมพ์ comment: "ฟังก์ชันแปลงอุณหภูมิจากเซลเซียสเป็นฟาเรนไฮต์"



# แบบฝึกหัดที่ 1.5: ปรับปรุงโค้ดให้ดีขึ้น
# เลือกโค้ดด้านล่างแล้วใช้ Ctrl+K สั่ง: "เพิ่ม error handling และ type hints"
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# แบบฝึกหัดที่ 1.6: สร้างฟังก์ชันค้นหาใน list
# ใช้ Chat ถาม: "สร้างฟังก์ชันค้นหาตัวเลขใน list และบอกตำแหน่ง"



# แบบฝึกหัดที่ 1.7: สร้าง class inheritance
# ใช้ Composer สั่ง: "สร้าง parent class Animal และ child class Dog, Cat"



# แบบฝึกหัดที่ 1.8: เพิ่ม docstring
# เลือกฟังก์ชันด้านล่างแล้วใช้ Ctrl+K สั่ง: "เพิ่ม docstring แบบ Google style"
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# แบบฝึกหัดที่ 1.9: สร้างฟังก์ชันจัดการไฟล์
# พิมพ์ comment: "ฟังก์ชันอ่านไฟล์ text และนับจำนวนคำ"



# แบบฝึกหัดที่ 1.10: Debug โค้ด
# ใช้ Chat ถาม: "ช่วยหา bug ในโค้ดนี้" พร้อมโค้ดด้านล่าง
def get_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # อาจเกิด error ถ้า numbers ว่าง

"""
หลังจากทำแบบฝึกหัดเสร็จ ให้ลองสิ่งเหล่านี้:

1. ใช้ Chat ถาม: "อธิบายโค้ดที่เขียนไปทั้งหมด"
2. ขอให้ AI แนะนำการปรับปรุงโค้ด
3. ขอให้สร้าง unit test สำหรับฟังก์ชันที่สร้าง
4. ลองใช้ @ mentions อ้างอิงไฟล์นี้ในการสนทนา
"""