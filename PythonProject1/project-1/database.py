import mysql.connector

# Establish connection to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",  # Replace with your MySQL username
    password="your_password",  # Replace with your MySQL password
    database="students_db"  # Replace with your MySQL database name
)

cursor = connection.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name VARCHAR(255),
        age INT,
        grades TEXT
    )
""")

# Function to insert a student into the database
def insert_student(student):
    cursor.execute(
        "INSERT INTO students (name, age, grades) VALUES (%s, %s, %s)",
        (student.name, student.get_age(), str(student.grades))
    )
    connection.commit()

# Function to retrieve all students from the database
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

# Close the database connection
connection.close()
