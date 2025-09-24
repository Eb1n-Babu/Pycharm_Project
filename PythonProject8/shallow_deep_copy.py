import copy

original = [1, 2, 3]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0] = 99
deep[1] = 88

print(original)  # [1, 2, 3]
print(shallow)
print(deep)


original_1 = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original_1)
deep_copy = copy.deepcopy(original_1)

shallow_copy[0][0] = 45
deep_copy[0][1] = 56
print(original_1)
print(shallow_copy)
print(deep_copy)


x = set(range(10))
print(x)

dic_1 = {"name":"1","age":"2"}
for element in dic_1:
    print(element  , dic_1[element])

dic_2 = {"name1":"1","age1":"2"}

dic_1.update(dic_2)
print(dic_1)
