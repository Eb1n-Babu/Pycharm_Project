def fib(x):
    list1 = [0,1]
    for i in range(0,x-2):
        list1.append(list1[-1]+list1[-2])
    return list1
print(fib(5))
print(fib(10))