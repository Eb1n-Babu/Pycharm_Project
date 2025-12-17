import copy


def digits_to_string():
    try:
        n = int(input("enter a number :"))
        x = str(n)
        if len(x) > 1:
            raise ValueError
        for element in x:
            if int(element) == 1:
                return f"one"
            elif int(element) == 2:
                return f"two"
            elif int(element) == 3:
                return f"three"
            elif int(element) == 4:
                return f"four"
            elif int(element) == 5:
                return f"five"
            elif int(element) == 6:
                return f"six"
            elif int(element) == 7:
                return f"seven"
            elif int(element) == 8:
                return f"eight"
            elif int(element) == 9:
                return f"nine"
            elif int(element) == 0:
                return "zero"
    except ValueError:
        return f"please enter a number only"

def div_two(num):
    try:
        if num == 0:
            raise ZeroDivisionError
        x = [x for x in range(0, num + 1, 2)]
        if num in x:
            return f"{num} is divisible by two"
        else:
            return f"{num} is not divisible by two"
    except ValueError:
        return f"please enter a number only"
    except ZeroDivisionError:
        return f"please enter a number only"

print(div_two(5))
print(div_two(6))
print(div_two(7))
print(div_two(8))
print(div_two(0))

print(chr(65))
print(chr(90))

for elements in range(0,26):
    print((elements+1)*chr(65+elements))


x1 = lambda x,y : x*y
print(x1(5,7))

f1 = list(range(1,11))
x3 = list(filter(lambda x: x%2==0,f1))
print(x3)

#39. Inserting an Object at a specific index in Python lists

x = list(range(1,11))
print(x)
x.insert(7,3)
print(x)

#40. How do you reverse a list?
s = [1, 2, 3, 4, 5, 6, 7, 3, 8, 9, 10]
s.reverse()
print(s)
print(list(reversed(s)))

#41. Removing Duplicates from a List

s = [1, 2, 3, 4, 5, 5, 5 ,6,6,6,7,7, 7, 3, 8, 9, 10]
x = set(s)
print(list(x))

#42. Returning Multiple Values from a Python Function
def number():
    return 1,2,34,5

print(number())

#43. Python switch-case statement

def switch_case(case):
    if case == "one":
        return "one"
    elif case == "two":
        return "two"
    elif case == "three":
        return "three"
    elif case == "four":
        return "four"
    elif case == "five":
        return "five"
    else:
        return "six"
print(switch_case("one"))

#46. Decorators
def my_function(func):
    def wrapper():
        print("execute before original function")
        func()
        print("execute after original function")
    return wrapper
@my_function
def hello_world():
    print("hello world")
hello_world()

def validate(func):
    def wrapper(num1,num2):
        if type(num1) == int and type(num2) == int:
            return func(num1,num2)
        else:
            return f"please enter a number only"
    return wrapper

@validate
def add(num1,num2):
    return num1+num2

print(add(1,2))
print(add(3,"4"))

#47. Pickling and Unpickling
data_to_pickle = [1,2,3,4,5,6,7,8,9,10,{'Python':3.9,'Library':'pickle'}]



#48. *args and **kwargs

def add(*args):
    return sum(args)

print(add(1,2,3,4,5,6,7,8,9,10))

def add(**kwargs):
    return sum(kwargs.values())
print(add(num=1,num2=2))

#50. The is Operator
q4 = 1
b2 = 1
x1 = 1
xc = 1


print(q4 is b2)
print(id(q4))
print(id(b2))
print(id(x1))
print(id(xc))

q1 = [1,2,3,4,5,6]
q2 = [1,2,3,4,5,6]
print(id(q1))
print(id(q2))
print(id(chr(65)))
x = "A"
print(id(x))
string_1 = "All"
for element in string_1:
    print(id(element))
print("")
for i in range(0,10):
    print(id(i))

#51. Checking if a String Contains Only Alphanumeric Characters
x = "h9undund3"
print(x.isalnum())

#52. Using the split() Function

x1 = "hello world"
print(x1.split("e"))

#53. Copying Objects

list_1 = [1,2,3,4,5,6,7,8]
list_2 = copy.copy(list_1)

list_2[4] = 101
print(list_2)
print(list_2)



list_3 = [1,2,3,4,5,6,7,8]
list_4 = copy.deepcopy(list_3)
list_4[4] = 101
print(list_4)
print(list_3)

#54. Deleting a File
import os

x = "D:\project\PycharmProjects\PythonProject10\hello.txt"
try:
    os.remove(x)
except FileNotFoundError:
    print("file not found")


#55. Polymorphism

class Animal:
    def sound(self):
        return "any sound"

class Dog(Animal):
    def sound(self):
        return "bow bow"
class Cat(Animal):
    pass
animal = Animal()
print(animal.sound())
animal1 = Dog()
print(animal1.sound())
animal2 = Cat()
print(animal2.sound())

#56. Creating an Empty Class
class Dog(Animal):
    pass

#58. Finding the Maximum Alphabetical Character in a String Using the max Function
x1 = 'fly{}iNg'
print(max(x1))

#61. Declaring Multiple Assignments

a = b = c = 3
f,g,h = 3,4,5