students = {}

def add_student(student_id, student):
    students[student_id] = student

def search_student(student_id):
    return students.get(student_id, "Student not found.")

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
