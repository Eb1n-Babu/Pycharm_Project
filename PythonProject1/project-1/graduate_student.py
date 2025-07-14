from student import Student

class GraduateStudent(Student):
    def __init__(self, name, age, grades, specialization):
        super().__init__(name, age, grades)
        self.specialization = specialization

    def display(self):
        print(f"Name: {self.name}, Age: {self.get_age()}, Specialization: {self.specialization}, Average Grade: {self.calculate_average()}")
