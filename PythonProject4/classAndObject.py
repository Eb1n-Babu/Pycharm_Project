class Student():
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self):
        return f"first Name : {self.firstName} /n last name :{self.lastName} /n age : {self.age} years old"


stu1 = Student("John", "Smith", 10)
print(stu1)