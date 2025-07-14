import numpy

arr = numpy.array([[1, 2, 3, 4, 5],[6,7,7,7,7]])
print(arr[0:1])
print(arr[0:2])
x = arr.copy()
print(x)
arr[0:1] = 42
print(arr)
x = 5
print(x)
for i in arr:
    print(i)

split = numpy.split(arr,2)
print(split)