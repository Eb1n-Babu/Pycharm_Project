class hello:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print(self.name)

def simple_gen():
    yield 1
    yield 2
    yield 3

for value in simple_gen():
    print(value)

name = [1,23,4,5,6,78,3]
alpha = ['s','v','f','f','s','v','f']

z = zip(name,alpha)
print(list(z))


for i in zip(name,alpha):
    print(i)

x = 5
print(isinstance(x,int))
print(id(x))


def hello():
    """hello"""
    pass

print(hello.__doc__)


str_1 = 'helooosnsdbhdvbdh'

dupl =[]
uniq =[]

for i in str_1:
    if i in uniq:
        dupl.append(i)
    else:
        uniq.append(i)

print(dupl)
print(uniq)

fib_s = [0, 1]

def fib(n):
    for m in range(n):
        c = fib_s[-1] + fib_s[-2]
        fib_s.append(c)
    return fib_s

print(fib(10))

uniq_ = []
repeat = []

def non_first():
    for r in str_1:
        if r in uniq_:
            repeat.append(r)
            break
        else:
            uniq_.append(r)

non_first()
print(repeat)
print(uniq_)

from collections import deque

fg = deque([1,2,3,4])
fg.append('a')
print(fg)
fg.appendleft('b')
print(fg)