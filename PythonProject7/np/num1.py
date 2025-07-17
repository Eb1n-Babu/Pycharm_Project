import numpy as np

new_array = np.arange(10)
print(new_array)

print(type(new_array))

list_1 = [1,3,3,5]
new_list_1 = np.array(list_1)
print(new_list_1)
list_2 = [1,3,3,5]

new_list_2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(new_list_2)
print(new_list_2.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

new_arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(new_arr)
print((new_arr.reshape(3,4)))
new_arr1 = new_arr.reshape(3,4)
for x in new_arr1:
    print(x)


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr3 = np.concatenate((arr1, arr2))
print(arr3)

arr4 = np.concatenate((arr1, arr2),axis=1)
print(arr4)