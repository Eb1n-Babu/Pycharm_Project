import math
from collections import deque

from websocket import continuous_frame

for i in range(1,11):
    for j in range(i):
        print("*",end=" ")
    print("")
for i in range(11,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("")


l = lambda x,y: x+y
print(l(6,6))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

factorial(5)
print(factorial(5))

def finPrime(n):
    if n >= 2:
        for i in range(2,int(math.sqrt(n))):
            if n % i == 0:
                return False
            else:
                continue
        return True
    else:
        return False

print(finPrime(5))
print(finPrime(2))

def fib(n):
    x = [0,1]
    for i in range(2,n):
        x.append(x[i-1]+x[i-2])
    return x
print(fib(5))


z1 = [1,2,3,4,5,6,7,8]
z2 = [3,5,7,8,0,8,0,9]
q1 ={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6"}
q2 ={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6"}

print(list(zip(z1,z2)))
print(list(zip(q1,q2)))

str1 = "hello world"
x = "".join(reversed(str1))
print(x)

def non_repeating(str1):
    uniq = []
    duplicate = []
    for elem in str1:
        if elem in uniq:
            duplicate.append(elem)
        else:
            uniq.append(elem)
    print(uniq[0])

non_repeating(str1)

dq = deque()
dq.appendleft(1)
dq.appendleft(2)
dq.append(5)
print(dq)