x = lambda a:a+10
print(x(5))
print(x(10))
y = lambda k:k*10
print(y(10))

def lamda_test(n):
    return lambda a:a*n

new = lamda_test(5)
print(new(10))
