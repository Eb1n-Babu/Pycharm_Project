from student import Student
from graduate_student import GraduateStudent
from file_handler import save_student_data, read_student_data
from exception_handler import validate_age
from data_manager import add_student, search_student, delete_student
from functional_utils import square, apply_map, apply_filter
from regex_utils import validate_name
from threading_utils import start_processing
from database import insert_student, get_students

import mysql.connector

# Establish database connection
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",  # Replace with MySQL username
    password="your_password",  # Replace with MySQL password
    database="students_db"  # Replace with MySQL database name
)

cursor = connection.cursor()

# Ensure the table exists in MySQL
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        grades TEXT
    )
""")
connection.commit()

def main():
    student1 = Student("Alice", validate_age(20), [85, 90, 88])
    student2 = GraduateStudent("Bob", validate_age(22), [78, 85, 80], "Computer Science")

    student1.display()
    student2.display()

    save_student_data(student1)
    save_student_data(student2)

    read_student_data()

    add_student(1, student1)
    add_student(2, student2)

    print(search_student(1))

    start_processing()

    # Insert students into MySQL
    insert_student(student1)
    insert_student(student2)

    # Fetch students from MySQL
    print(get_students())

    # Close connection at the end
    connection.close()

if __name__ == "__main__":
    main()
