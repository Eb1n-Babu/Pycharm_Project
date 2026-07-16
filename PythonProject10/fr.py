xt = "hello world"
print(xt[::-1])

def reverse(x):
    for i in range(-1,-len(x),-1):
        print(("".join(x[i])).strip(),end="")
reverse(xt)

def palindrome(word):
    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    else:
        return False

print()
print(palindrome("hello"))
print(palindrome("malayalam"))

asort = [1,2,3,45,34,5,76]
#sort.sort()
#print(sort)

def sorting(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
            else:
                continue
    return array

print(sorting(asort))

du = "hello world"

def remove_duplicate(element):
    unique_elements = []
    duplicated_elements = []
    for el in element:
        if el in unique_elements:
            duplicated_elements.append(el)
        else:
            unique_elements.append(el)
    return duplicated_elements,unique_elements

print(remove_duplicate(du))
