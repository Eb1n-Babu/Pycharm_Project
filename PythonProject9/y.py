from itertools import groupby

from fontTools.misc.cython import returns
from numpy.f2py.auxfuncs import flatlist

nested = [1, [2, [3, 4], 5], 6,[5,6,7,[5,6,7]]]


print(flatlist(nested))

def flatlist(a):
    x = []
    for elements in a:
        if isinstance(elements,list):
            x.extend(flatlist(elements))
        else:
            x.append(elements)
    return x

print(flatlist(nested))
input_str = "aaeeadbsssbdddccahhhh"
print("".join(reversed(input_str)))


for i,group in groupby(input_str):
    print(f"{len("".join(group))}{i}",end="")


for i in range(0,10):
    print(i*" *")

list1 = [2, 3, 4, 3, 10, 3, 5, 6, 3]

def duplicates(a):
    unique = []
    duplicate = []
    for i in range(len(list1)):
        if list1[i] in unique:
            duplicate.append(list1[i])
        else:
            unique.append(list1[i])
    return sorted(unique)

print(duplicates(list1))

b=(1)
print(type(b))
b=(1,)
print(type(b))