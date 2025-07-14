dictionary  = {'name':'Albin','age':10,'year':2004}
for key in dictionary:
    print(dictionary[key])

dictionary["colour"] = "colour"
print(dictionary)
dictionary.pop("name")
print(dictionary)
print(dictionary.values())