from django.template.defaultfilters import length

a = 2
b = 6
print(a,b)
a , b = b , a
print(a,b)

value_1 = [4,3,35,6,74,3,34,2,2,5]

for i in range(length(value_1)):
    for j in range(length(value_1)-1):
        if value_1[j] > value_1[j+1]:
            value_1[j], value_1[j+1] = value_1[j+1], value_1[j]
print(value_1)

def add(*args):
    return sum(args)

print(add(1,2,34))

x = [i * 2 for i in range(5)]
print(x)

d = {'a': 1}
print(d)

if 'a' in d:
    print(d['a'])

str_1 = "heelo"
print(list(str_1))
print(str_1.split())

print(zip(i for i in range(10)))

y = [x/2 for x in range(2,13,2)]
print(y)


# This is our decorator function
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

# This is the function we want to decorate
@my_decorator
def say_hello():
    print("Hello, EBIN!")

# Call the decorated function
say_hello()

def a1(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@a1
def say_hello():
    print("Hello, EBIN!")

say_hello()


def new_func(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@new_func
def say_hello():
    print("Hello, EBIN!")
say_hello()

y = {x:x**2 for x in range(10) if x % 2 == 0}
print(y)


c = 0
while c < 10:
    print(c)
    c += 1

a = lambda s,h : s*h
print(a(2,3))