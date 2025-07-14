def save_student_data(student):
    with open("students.txt", "a") as file:
        file.write(f"{student.name},{student.get_age()},{student.grades}\n")

def read_student_data():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No student records found.")
