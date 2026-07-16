class phone:
    def __init__(self,brand, model, year , price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price




    def display(self):
        return f"{self.brand} {self.model} {self.year} {self.__price}"

new_phone = phone("iphone", "iphone 15", "2023",900000)
print(new_phone.display())

new_phone.brand = "iphonettt"
print(new_phone.display())
new_phone.price = 90785
print(new_phone.display())

#14. PEP 8: The Python Enhancement Proposal 8
# module with small letter
class Phone:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        pass

    def display(self):
        pass

    def display_details(self):
        pass
#15. Modifying Strings

string_1 = "hello"
string_2 = "world"
print(string_1+string_2)
print(string_1[::-1])
print(string_1.upper())
print(string_1.lower())
word = " hello world  "
word1 = word.replace("world", "kochi")
print(word1)
print(word.strip())

#16. Built-in Types
x1 = 5
print(type(x1))

x2 = 3.13
print(type(x2))

x3 = "hello world"
print(type(x3))

x4 = [1,2,3,4,5,6]
print(type(x4))

x5 = (1,2,3,4,5,6)
print(type(x5))

x6 = {1:"x",2:"y",3:"z"}
print(type(x6))
print(x6[1])

x7 = {1,2,3,4,5,6}
print(type(x7))

x8 = None
print(type(x8))

#17. Linear (Sequential) Search and Its Usage
my_list = [10, 25,11,30,8,11]
for elements in my_list:
    if elements == 8:
        print("True")
    else:
        print("False")

if 8 in my_list:
    print("True")

#19. Discussing Data Types

#1. Simple Lambda Function: A lambda function that adds two numbers:

result = lambda a,b:a+b
print(result(10,20))

#2. Sorting with Lambda:
students = [('Alice' , 25), ('Bob' , 20), ('Charlie' , 30)]
students.sort(key=lambda student: student[1])
print(students)
print(type(students))

#3. Filtering with Lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = list(filter(lambda number: number % 2 == 0, numbers))
print(x)

x1 = [x for x in numbers if x % 2 == 0]
print(x1)

#20. Local and Global Variables

x = 10
def values(num1 ,num2):
    y = num2
    x = num1
    return x,y
print(values(1,5))
print(x)
#print(y)

#21. Checking if a List is Empty
my_list = []
if len(my_list) == 0 or None:
    print("Empty list")

#22. Creating a Chain of Function Decorators

def my_function(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result
    return wrapper
@my_function
def my_function2(*args, **kwargs):
    print(args)
    print(kwargs)
my_function2(3,45,k=45)

def demo_function(fun):
    def wrapper():
        print("hello")
        fun()
        print("world")
    return wrapper

@demo_function
def hello():
    print("hello")
hello()

def login(fun):
    def wrapper(name,age):
        name = input("Please input your name:")
        age = input("Please input your age:")
        fun(name, age)
        return fun
    return wrapper

@login
def hello(name,age):
    print("hello " + name+"your age is "+str(age))

hello("amal",50)

