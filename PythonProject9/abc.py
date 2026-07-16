from abc import ABC, abstractmethod

# Abstract class
class Vehicle:
    def start(self):
        print("start of vehicle")


class Car(Vehicle):
    def start(self):
        print("Car engine starts with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike engine starts with a kick.")

v1 = Car()
v2 = Bike()
v1.start()
v2.start()

v2 = Vehicle()
v2.start()

def hello(fun):
    def wrapper():
        print("before function call")
        fun()
        print("after function call")
    return wrapper

@hello
def hello():
    print("hello world")

hello()

def my_function(fun):
    def wrapper():
        fun()
    return wrapper

@my_function
def hello():
    print("hello world")
hello()

def fib(n):
    x = [0,1]
    for i in range(2,n):
        x.append(x[-1]+x[-2])

    for y in range(len(x)):
        yield x[y]

for i in fib(10):
    print(i)

x = [x for x in range(10) if x % 2 == 0]
y = [x for x in range(100) if x%10 == 0]
print(x)
print(y)

d = {x:x*x for x in range(10)}
print(d)

a = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(id(a))
b=a
print(b)
print(id(b))

print(b is a)

c = a.copy()
print(c)
print(id(c))

print(b is c )

x1 = set(range(10))
print(x1)
x2 = set(range(11,21))
print(x2)
x3 = set(range(9))

y1 = x1 | x2
print(y1)

y2 = x1 & x3
print(y2)

y3 = x1-x3
print(y3)
