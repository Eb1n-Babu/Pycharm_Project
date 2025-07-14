from new_demo.person import Person

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grade = []

    def grade_for(self, grade):
        self.grade.append(grade)
        return self.grade

    def average(self):
        return sum(self.grade) / len(self.grade)

    def display(self):
        print(self.name, self.age, self.grade)





