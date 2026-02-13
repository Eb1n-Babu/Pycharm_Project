import math
import os
import random
from gc import garbage
from itertools import groupby


def  gcd():
    n = int(input("Enter a number pairs to calculate GCD: "))
    for i in range(1,n+1):
        x = int(input(f"Enter first number to calculate GCD in pair {i}: "))
        y = int(input(f"Enter second number to calculate GCD in pair {i}: "))
        z = math.gcd(x,y)
        print(z)

def reverse(word):
    reversed_word = word[::-1]
    return reversed_word
print(reverse("hello"))
print(reverse("world"))

def prime_number(num):
    if num >=2 :
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False
            else:
                continue
        return True
    else:
        return False
print(prime_number(5))
print(prime_number(2))

def palindrome(word):
    x = word.strip().lower().replace(" ","")[::-1]
    if word.strip().lower().replace(" ","") == x:
        return True
    else:
        return False
print(palindrome("hello"))
print(palindrome("malayalam"))

def anagram(word1, word2):
    if sorted(word1.strip())==sorted(word2.strip()):
        return True
    else:
        return False
print(anagram("hello", "world"))
print(anagram("   listen", " silent"))

def gcd_normal(num1, num2):
    x = sorted([num1, num2])
    for i in range(x[0],0,-1):
        if x[1]%i == 0 and x[0]%i ==0:
            return i
        else:
            continue
    else:
        return 0

print(gcd_normal(1000,10))




demos = [1,2,[1,2,3,4],[5,6],[6,5]]


def flatten(x):
    y = []
    for element in x:
        if isinstance(element,list):
            y.extend(flatten(element))
        else:
            y.append(element)
    return y
print(flatten(demos))

x = "aaabbccddaaa"

def count_elements(lst):
    for i, group in groupby(x):
        print(f'{len(''.join(group))}{i}', end="")

count_elements(x)

print("")
bubble_list = [62,45,56,45,67,45,67.2,1,4,60]

def bubble_switch(c):
    for i in range (0,len(bubble_list)):
        for j in range(1,len(bubble_list)):
            if c[j-1] > c[j]:
                c[j-1],c[j] = c[j],c[j-1]
    return c

print(bubble_switch(bubble_list))

def greeting(fun):
    def wrapper():
        print("before function call")
        fun()
        print("after function call")
    return wrapper

@greeting
def hello():
    print("hello")

hello()


def validation(fun):
    def wrapper(num1,num2):
        if isinstance(num1,int) and isinstance(num2,int):
            return fun(num1,num2)
        else:
            return f"invalid input"
    return wrapper

@validation
def add(num1,num2):
    return num1+num2

@validation
def subtract(num1,num2):
    return num1-num2

@validation
def multiply(num1,num2):
    return num1*num2


print(add(2,3))
print(add("3",3))
print(add("455fff",3))
print(subtract(2,3))
print(multiply(2,3))
print(multiply("455fff",3))


def fib(serirs):
    fib_series = [0,1]
    for i in range(2,serirs):
        fib_series.append(fib_series[i-1]+fib_series[i-2])
    return fib_series

print(fib(10))

for j in range(10):
    print(" "*(10-j),end=" ")
    print(" *"*j)

def add_elements(*args):
    return sum(args)

print(add_elements(1,2,3,4,5,6,7,8,9))

def name(**kwargs):
    print(kwargs)

# Call with keyword arguments
name(hello="new",age="34")

ui = [i for i in range(1,10)]
print(ui)

li = [x for x in range(10) if x%2==0]
print(li)

fi = {x:x**2 for x in range(10)}
print(fi)

add_numbers = lambda a,b:a+b
print(add_numbers(1,2))


two_number = lambda x,y:x*y
print(two_number(3,4))

t = "heLLO"
print(t.swapcase())

i = 0
while i<=10:
    print(i)
    i+=1

s1 = [1,2,3,4,5]
s2 = [4,5,6,7,8]

x = map(add,s1,s2)
print(list(x))

h = [x for x in range(10) if x%2==0]
print(h)

n = map(lambda x:x**2,h)
print(list(n))

dict_1 = {x:x**2 for x in range(10)}
print(dict_1)

dq = [1,2,4,5,67,8]
print(sorted(dq))
dq.sort()
print(dq)






def generator(g):
    for x in range(g):
        yield x

x = generator(5)
for i in x:
    print(i)


def d1(t):
    for i in range (t):
        yield i

k = d1(10)
for i in k:
    print(i)

f1 = [56,45,6,7,87,78]
for i in enumerate(f1):
    print(i)

#with open("hello.txt","r") as f:
    #x = f.read()
    #print(x)

print("")

elements = [5,6,7,89,9,0]

for i in enumerate(elements):
    print(i)

list_elements = ["hello","align","next","new"]

for i in enumerate(list_elements):
    print(i)


class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):   # getter
        return self.__name

    @name.setter
    def name(self, value):   # setter
        self.__name = value

    @name.deleter
    def name(self):   # deleter
        del self.__name

s = Student("Ebin")
print(s.name)        # calls getter, prints "Ebin"
s.name = "Rahul"     # calls setter
del s.name           # calls deleter


print(random.randint(10,15))
print(random.randrange(10,100,6))

x = {x:x**2 for x in range(10)}
print(x)

x = "hello my dear wrong number"
print(x.split())
y = x.split()
random.shuffle(y)
print(y)

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def sound(self):
        print("vehicle sound")

class Bike(Vehicle):
    def sound(self):
        print("bike sound")

class Car(Vehicle):
    def sound(self):
        print("car sound")


xh = 6
def hel():
    z = xh+1
    return z
print(hel())

g1 = garbage.sort()
print(g1)

f1 = [1,2,3,4,5,6,7,3,2,4,5,1]

def duplicate():
    uniq = []
    duplicate = []
    for i in f1:
        if i in uniq:
            duplicate.append(i)
        else:
            uniq.append(i)
    return duplicate
print(duplicate())

