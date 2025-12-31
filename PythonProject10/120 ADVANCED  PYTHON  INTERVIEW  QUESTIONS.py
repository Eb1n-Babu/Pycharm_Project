#1. Why would you use the 11pass11 statement?
import copy
from itertools import groupby

from Demos.SystemParametersInfo import orig_value


def add(a,b):
    pass

print(type(add))
#pass is help us to declare a empty function or class without logic implemented
#2. Subtracting 1 from Each Element in a List
#Problem: Given a list 1st with elements [2, 33,222, 14, 25], you want to subtract 1

demo_list = [2, 33,222, 14, 25]
sub_list = [x-1 for x in demo_list]
print(sub_list)

#4. Understanding Callables
#Functions,Methods,Classes,callable objects,Built-in Functions,Callable Instances:

#5. Printing Odd Numbers Between O and 100

oddNumbers = [i for i in range(1,100,2)]
print(oddNumbers)

#6. Finding Unique Values in a List
lst = [1, 2, 3, 4, 4, 6, 7, 3, 4, 5, 2, 7]
x= set(lst)
print(list(x))

#7. Accessing Attributes of Functions
def display(str1):
    print(f"hello {str1}")

display("amal")

#8. Performing Bitwise XOR
x = 6
y = 8
print(bin(x))
print(bin(y))
print("Bitwise XOR")
print(x ^ y)
print(bin(14))

x1 = 1100
y2 = 1010
print(int("1100",2)+int("1010",2))
print(int("1100",2))
print(int("1010",2))

#9. Swapping Variable Values Without an Intermediary Variable
a = 5
b = 7

a,b = b,a
print(a,b)
bubble_switch = [23,34,24,0,-1,2,56,23,45,23,45,67,89]
print(dir(bubble_switch))
def bubble_(input_list):
    x = len(input_list)
    for i in range(0, x):
        for j in range(1, x):
            if input_list[j - 1] > input_list[j]:
                input_list[j - 1], input_list[j] = input_list[j], input_list[j - 1]
            else:
                continue
    return input_list
print(bubble_(bubble_switch))


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

""" 
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
"""
def validate_inputs(fun):
    def wrapper(num1,num2):
        if type(num1) == int and type(num2) == int:
            return fun(num1,num2)
        else:
            return f"invalid input"
    return wrapper

@validate_inputs
def add(num1,num2):
    return num1 + num2
print(add(1,2))
@validate_inputs
def multiply(num1,num2):
    return num1 * num2
print(multiply(1,2))

def string_validation(func):
    def wrapper(string):
        if type(string) == str:
            return func(string)
        else:
            return f"invalid input"
    return wrapper

@string_validation
def hello(name):
    return f"hello {name}"

print(hello("amal"))
print(hello(6))


#25. Python modules and commonly used built-in modules
import math
print(math.floor(math.pi))
print(math.ceil(math.pi))
print(math.pi)

import random
print(random.randint(1,10))
print(random.randrange(1,10,1))

import datetime
print(datetime.datetime.now())
print(datetime.date.today())

#27. Type conversion
x = 5
y = 4.6
print(x+y) #implicit type convertion
print(str(x))
print(type(x))

#30. Randomizing items in a list
import random
new_list = random.sample(range(1,100), 10)
print(new_list)

print(new_list)

#31. Python iterators
my_list = [1, 2, 3, 4, 5]
obj = iter(my_list)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

def elements(list1):
    for element in list1:
        yield element

obj = elements(my_list)
print(next(obj),(next(obj)))

#32. Generating random numbers

import random

x = random.randint(1,10)
print(x)
y = random.sample(range(1,10),5)
print(y)
z = random.choice(range(1,10))
print(z)
my_list = ["apple", "banana", "cherry", "date"]
print(random.choice(my_list))
print(random.uniform(1,10))

#35. "and" and "or" logical operators
x = 5
y = 6
if type(x) == int and type(y) == int:
    print("true")
if type(x) == float or type(y) == int:
    print("true")

#36. Mastering the Use of Python•s range() Function
x = list(range(1,10))
print(x)

for i in range(1,10):
    print(i)

def add(**kwargs):
    return sum(kwargs.values())

print(add(num1=1,num2=2))

def add1(*args):
    return sum(args)

print(add1(3,4))

def add2(*args,**kwargs):
    return sum(args), sum(kwargs.values())
print(add2(num1=1,num2=2))

def add3(**kwargs):
    return sum(kwargs.values())

print(add3(num1=1,num2=2))

#37. What's init ? constructor method that initialize call instance

help(list)
x = (1,2,3,4,5,6,7,8)
for elements in x:
    print(elements)

x = [1,2,3,[3,4,5],[5,6,7],8,9,10]

def flatten(y):
    new_list = []
    for element in y:
        if isinstance(element,list):
            new_list.extend(flatten(element))
        else:
            new_list.append(element)
    return new_list

print(flatten(x))


x = "aaaasssebsbssbsa"

def counts(num):
    x = set(num)
    for element in list(x):
        print(f"{num.count(element)}{element}",end="")

counts(x)
print("")
for i,group in groupby(x):
    print(f"{len("".join(group))}{i}",end="")

word = "Alignerr"
print("")
print(word[-3:])

xf = [11,12,13,14,15,16,17,18]
for x,elements in enumerate(xf,start=10):
    print(f"{x}{elements}")

for value, element in enumerate(xf,start=10):
    print(value," = ",element)

original = [1,2,3,4,5,6,7,8]

shallow_copy = copy.copy(original)
print(original)
print(shallow_copy)
print("===============")
shallow_copy.append(10)
print(shallow_copy)
print(original)
print("============================")
original.append(10)
print(original)
print(shallow_copy)

h1 = "hello"
def palindrome_check(words):
    x = words[::-1]
    if x.strip().lower().replace(" ","") == words.strip().lower().replace(" ",""):
        return True
    else:
        return False
print(palindrome_check("hello"))
print(palindrome_check(" malaya  lam"))

def prime_number(string):
    if string>=2:
        for i in range(2,string):
            if string%i==0:
                return False
            else:
                continue
        return True
    else:
        return False

print(prime_number(5))
print(prime_number(2))
print(prime_number(3))
print(prime_number(6))
print(prime_number(7))

for i in range(100):
    if prime_number(i):
        print(i)
    else:
        continue

def fact(stre):
    factorial = 1
    for i in range(1,stre+1):
        factorial *= i
    return factorial

print(fact(5))