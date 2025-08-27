# ตัวอย่างที่ 2: การใช้งาน Inline Editing (Ctrl+K)
# เลือกโค้ดที่ต้องการแก้ไข แล้วกด Ctrl+K

"""
วิธีใช้ Inline Editing:
1. เลือกโค้ดที่ต้องการแก้ไข
2. กด Ctrl+K
3. พิมพ์คำสั่งที่ต้องการให้ AI ทำ
4. กด Enter

ตัวอย่างคำสั่งที่ใช้บ่อย:
- "เพิ่ม error handling"
- "เพิ่ม type hints"
- "เพิ่ม docstring"
- "ทำให้โค้ดสั้นลง"
- "แปลงเป็น async function"
"""

# ลองเลือกฟังก์ชันนี้แล้วใช้ Ctrl+K พร้อมคำสั่ง:
# "เพิ่ม input validation และ error handling"
def divide_numbers(a, b):
    return a / b

# ลองเลือกฟังก์ชันนี้แล้วใช้ Ctrl+K พร้อมคำสั่ง:
# "เพิ่ม type hints และ docstring"
def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

# ลองเลือกคลาสนี้แล้วใช้ Ctrl+K พร้อมคำสั่ง:
# "เพิ่มเมธอด __str__ และ __repr__"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ลองเลือกโค้ดนี้แล้วใช้ Ctrl+K พร้อมคำสั่ง:
# "แปลงให้เป็น list comprehension"
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)

# ลองเลือกโค้ดนี้แล้วใช้ Ctrl+K พร้อมคำสั่ง:
# "เพิ่ม logging และ better error messages"
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        return None