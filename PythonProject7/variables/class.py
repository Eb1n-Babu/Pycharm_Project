import datetime


class demo:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} is {self.age} years old'

obj = demo('john',20)
print(obj)
print(obj.age)

print(datetime.datetime.now().year)
print(datetime.datetime.now().year - obj.age)