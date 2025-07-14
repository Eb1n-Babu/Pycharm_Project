"""Object-Oriented Programming (Classes & Objects): Write a Python class named
Student with attributes for name and age. Add a method to display the student's
details. Create an instance and print the details."""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)

stu1 = Student("John",25)
stu2 = Student("amal",36)

stu2.display()
stu1.display()