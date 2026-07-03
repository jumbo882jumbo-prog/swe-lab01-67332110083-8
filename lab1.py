def calculate_grade(scores):
    # 1. ตรวจสอบก่อนว่าลิสต์ว่างหรือไม่ (แก้ Bug ZeroDivisionError)
    if not scores:
        return "N/A", 0  # หรือส่งค่าที่เหมาะสมกลับไปกรณีไม่มีคะแนน

    # 2. ใช้ sum() เพื่อความรวดเร็วและอ่านง่าย
    total = sum(scores)
    average = total / len(scores)
    
    # 3. การตัดสินเกรด (Logic เดิมถูกต้องแล้ว)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ทดสอบใช้งาน
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Grade: {grade}, Average: {avg:.2f}")

# ทดสอบกรณีลิสต์ว่าง (จะไม่พังแล้ว)
print(calculate_grade([]))
