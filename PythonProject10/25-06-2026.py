import copy

hello = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

demo = iter(hello)
print(next(demo))
print(next(demo))

def count(num):
    for i in range(1,num+1):
        yield i


add = lambda a,b: a+b
print(add(1,6))


class Name:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

obj1 = Name("amal",60)
print(obj1.name)

f = "hello"
print(type(f))
print(isinstance(f,str))


def adding(*num):
    return sum(num)
print(adding(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))

def add(*args):
    return sum(args)

def name(**names):
    for key,value in names.items():
        print(key,"have age of ",value)
name(name="amal",age=12)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2 = list1
print(id(list1))
print(id(list2))

list3 = copy.copy(list1)
print(id(list3))


counter = 0

def increment():
    global counter
    counter += 1
    return counter
def reset():
    global counter
    counter = 0
    return counter
print(increment())
print(increment())
print(increment())
print(reset())

x = {1,3,4,5,6,7,8,9,10,11,12,13,14,15}
print(type(x))

y = frozenset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(type(y))

def hello():
    """

    Returns:hello

    """
    pass


print(hello.__doc__)