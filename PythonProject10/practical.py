import math


def reverse(word):
    return word[::-1]

print(reverse("banana"))

def palindrome(word):
    try:
        x = word[::-1]
        if x == word:
            return True
        else:
            return False
    except TypeError:
        return False
    except ValueError:
        return False

print(palindrome("malayalam"))

def prime(x:float):
    if x >= 2:
        for i in range(2,int(math.sqrt(x)+1)):
            if x % i == 0:
                return False
            continue
        return True
    else:
        return False

print(prime(5))
print(prime(10))


def fibonacci(n):
    a = [0, 1]
    for i in range(2,n+1):
        a.append(a[i-1] + a[i-2])
    return a

print(fibonacci(5))


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(factorial(5))