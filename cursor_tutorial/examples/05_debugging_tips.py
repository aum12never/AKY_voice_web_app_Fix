# ตัวอย่างที่ 5: การใช้ AI ช่วย Debug
# Cursor AI สามารถช่วยหาและแก้ไข bug ได้อย่างมีประสิทธิภาพ

"""
วิธีใช้ AI สำหรับ Debugging:

1. Copy error message มาวางใน Chat (Ctrl+L)
2. เลือกโค้ดที่มีปัญหาแล้วถาม AI
3. ใช้ Ctrl+K เพื่อแก้ไขโค้ดที่มีปัญหา
4. ขอให้ AI อธิบายสาเหตุของ bug

ตัวอย่างคำถามสำหรับ Debug:
- "ทำไมโค้ดนี้เกิด IndexError"
- "ช่วยหา logic error ในฟังก์ชันนี้"
- "ทำไม API call นี้ return None"
- "ช่วยอธิบาย error message นี้"
"""

# ตัวอย่าง Bug ที่พบบ่อย - ลองใช้ AI ช่วยหา!

# Bug 1: IndexError
def get_first_element(lst):
    return lst[0]  # จะเกิด error ถ้า list ว่าง

# ลองถาม AI: "ช่วยแก้ไข IndexError ในฟังก์ชันนี้"

# Bug 2: KeyError
def get_user_name(user_dict):
    return user_dict['name']  # จะเกิด error ถ้าไม่มี key 'name'

# ลองถาม AI: "ป้องกัน KeyError ในฟังก์ชันนี้"

# Bug 3: Type Error
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# ลองเรียกฟังก์ชันด้วย: calculate_average("123")
# แล้วถาม AI: "ทำไมโค้ดนี้เกิด TypeError"

# Bug 4: Logic Error
def is_even(number):
    if number % 2 == 1:
        return True
    return False

# ลองถาม AI: "หา logic error ในฟังก์ชันนี้"

# Bug 5: Infinite Loop
def countdown(n):
    while n > 0:
        print(n)
        # ลืมลด n!

# ลองถาม AI: "ทำไมฟังก์ชันนี้เป็น infinite loop"

# Bug 6: Wrong Variable Name
def calculate_discount(price, discount_percent):
    discount_amount = price * discount_percentage / 100  # ใช้ชื่อตัวแปรผิด!
    return price - discount_amount

# ลองถาม AI: "หา NameError ในฟังก์ชันนี้"

# Bug 7: Off-by-one Error
def print_numbers(n):
    for i in range(n + 1):  # จะพิมพ์เกินไป 1 ตัว
        print(i)

# ลองถาม AI: "ตรวจสอบ off-by-one error ในฟังก์ชันนี้"

"""
เทคนิคการ Debug ด้วย AI:

1. ให้ข้อมูลครบถ้วน:
   - Copy error message ทั้งหมด
   - ระบุ input ที่ทำให้เกิด error
   - อธิบายผลลัพธ์ที่คาดหวัง

2. ถามคำถามที่เฉพาะเจาะจง:
   ❌ "โค้ดนี้ผิดอะไร"
   ✅ "ทำไมฟังก์ชันนี้ return None แทนที่จะเป็น list"

3. ให้ AI อธิบายก่อนแก้ไข:
   "อธิบายสาเหตุของ bug ก่อน แล้วค่อยแนะนำวิธีแก้ไข"

4. ขอให้เพิ่ม error handling:
   "แก้ไข bug นี้แล้วเพิ่ม error handling ด้วย"
"""

# ตัวอย่างการใช้ AI ช่วยเขียน Unit Test เพื่อป้องกัน Bug
def divide_safely(a, b):
    """ฟังก์ชันหารที่ปลอดภัย - ขอให้ AI เขียน unit test ให้"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# ลองถาม AI: "เขียน unit test สำหรับฟังก์ชัน divide_safely"