import math


def prime(x):
    if x >=2:
        for i in range(2,int(math.sqrt(x)+1)):
            if x % i == 0:
                return False
        return True
    else:
        return False






