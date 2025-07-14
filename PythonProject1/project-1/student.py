class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.__age = age
        self.grades = grades

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer.")

    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}, Average Grade: {self.calculate_average()}")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
