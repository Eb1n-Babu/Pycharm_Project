import datetime
from collections import deque
from os.path import split

x = "hello"
y = "world"
z = [2,3,45,6,6,8,8]

a = tuple(zip(x,y))
b = list(zip(x,y))
c = dict(zip(x,y))

print(type(a))
print(type(b))
print(c)
print(list(zip(x,z)))

def square(element):
    return element * element

print(list(map(square,z)))

print(list(filter(lambda x: x%2==0,z)))

h = lambda m,n:m*n
print(h(3,4))

x = [x for x in range(10)]
x = [x for x in range(10) if x%2==0]

#x = {x:x for x in range(10)}

y = deque(x)
print(y.popleft())
print(y)


class Maths_class:
    name = 'heelo'
    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1

    @property
    def a1(self):
        return self.a

    @a1.setter
    def a1(self, value):
        self.a = value

    @a1.deleter
    def a1(self):
        del self.a



    @staticmethod
    def add(x1, y1):
        return x1+y1

    def sum(self):
        return self.a+self.b

    @classmethod
    def hello(cls):
        return cls.name

obj = Maths_class(1, 2)
print(obj.sum())
print(obj.name)
print(obj.a)
print(obj.hello())






gt = datetime.datetime.now()
print(gt)
print(type(gt))

yu = gt.strftime("%Y-%m-%d %H:%M:%S")
print(yu)
print(type(yu))



xy = "19990923"

dt = datetime.datetime.strptime(xy, "%Y%m%d")
print(dt)
print(type(dt))

de = datetime.date(1999, 9, 23)-datetime.date(1998,4,5)
print(de)


count = 0

def counting():
    global count
    for i in range(100):
        if i % 5 == 0:
            count += 1
    return count
print(counting())
print(count)


def validation(func):
    def wrapper(num1,num2):
        if type(num1)==int and type(num2)==int:
            return func(num1,num2)
        else:
            return f"{num1} and {num2} are not integer"
    return wrapper

@validation
def add(num1,num2):
    return num1+num2

print(add(1,2))



def validate(fun):
    def wrapper(num1,num2):
        if type(num1)==int and type(num2)==int:
            return fun(num1,num2)
        else:
            return f"{num1} and {num2} are not integer"
    return wrapper

@validate
def add(num1,num2):
    return num1+num2
print(add(1,2))

CF = [3,4,5,6,6,7,[45,[45,67]],67,[5,[56.78,67,6]],67]

def flat(input_value):
    flat_element = []
    for element in input_value:
        if isinstance(element,list):
            flat_element.extend(flat(element))
        else:
            flat_element.append(element)
    return flat_element

print(flat(CF))

x1 = [1,2,3,4,5]
x2 = [2,3,456,6]
x12 = [x1+x2]
print(x12)

CF = [3,4,5,6,6,7,[45,[45,67]],67,[5,[56.78,67,6]],67]

help(str)
dir(str)