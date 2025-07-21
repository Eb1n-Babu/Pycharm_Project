import math


def primeNumber(n):
    if n >= 2:
        for i in range(2,math.ceil(math.sqrt(n))+1,1):
            if n % i == 0:
                return f"{n} is  not a prime number"
            else:
                return f"{n} is   a prime number"
    else:
        return f"{n} is  not a prime number"


if __name__ == '__main__':
    for k in range(0,100):
        print(primeNumber(k))