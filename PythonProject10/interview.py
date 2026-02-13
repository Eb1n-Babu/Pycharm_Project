import math

import numpy as np

x = [1,23,5,6,7,8,None]
y = [2,3,4,6,8,9,11]

print(x+y)
print(y+x)

x.extend(y)
y.extend(x)

print(x)
print(y)

def add(c,d):
    return c+d

def call(func,b,c):
    return func(b,c)

print(call(add,2,3))


x1 = 12
x2 = [1,2,3,4]

def change(x1):
    return x1+10
print(change(x1))

def change1(x2):
    x2.append(34)
    return x2
print(change1(x2))

df = [x for x in range(10) if x%2==0]
print(df)

import pdb

def add(a,b):
    #pdb.set_trace()
    return a+b
print(add(1,2))

x1 = [1,2,3]
x2 = [4,5,6]
x3 = [7,8,9]

print(list(zip(x1,x2,x3)))
print(dict(zip(x1,x2)))

def validator(fun):
    def wrapper(a,b):
        if isinstance(a,int) and isinstance(b,int):
            return fun(a,b)
        else:
            return f"invalid input"
    return wrapper
@validator
def add(a,b):
    return a+b
print(add(1,2))


x = [1,2,3,4,5,6]

def two_of(x):
    if x % 2 == 0:
        return x
    else:
        return None

print(list(filter(two_of,x)))

words = ['Hello', 'World', 'Python']
print(''.join(words))

text = "   Hello, World!"
print(text)
print(text.strip())
print(text.split("e"))

with open("hello.txt",'r') as f:
    x = f.read()
    print(x[::-1])

def hello(*args):
    return sum(args)
print(hello(1,2,3,4,5,6))

def hello1(**kwargs):
    return sum(kwargs.values())

print(hello1(a=1, b=2, c=3))  # Output: 6
print(__name__)


x = np.array([1,2,3,4,5,6])
y = np.array(range(6))
print(x)
print(y)

g = "hello"
print(g.lower())


o = [1,2,[4,5,6],6,7,[5,6,7],[5,6,7]]

def flatten(type1):
    fl = []
    for elements in type1:
        if isinstance(elements,list):
            fl.extend(flatten(elements))
        else:
            fl.append(elements)
    return fl
print(flatten(o))

"""
def pr():
    v = int(input("enter a number :"))
    for i in range(1,v+1):
        x1 = int(input(f"enter first element of {i} pair of numbers :"))
        x2 = int(input(f"enter second element of {i} pair of numbers :"))
        print(math.gcd(x1,x2))

pr()
"""
def star(x):
    for i in range(1,x+1):
        print(" "*(x-i),end="")
        print(" *"*i)

print(star(5))

x = [3,4,5,6,32,3,45,6,6,756,5]

def buble(x):
    for i in range(1,len(x)+1):
        for j in range(1,len(x)):
            if x[j-1] > x[j]:
                x[j-1] , x[j] = x[j], x[j - 1]
    return x

print(buble(x))



dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict12 = {"a": 1, "b": 2}
dict22 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)

class square:
    def __init__(self, x):
        self.x = x

    @property
    def area(self):
        return self.x * self.x

sq = square(3)
print(sq.area)

class animal:
    def dog(self):
        return "bow bow"

do = animal()
print(do.dog())

def cat():
    return "mow"

do.dog = cat
print(do.dog())

li = [1,2,3,4]
c = li.copy()
print(c)

cf = [1,2,3,4,34,5,3,43,43,434,67,57,56,67,2,1,1,2,345,5]
print(sorted(set(cf))[-2])

kl = "hello"
gh = "listen"
kh = "silent"

def anagram(a,b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False
print(anagram(kh,gh))