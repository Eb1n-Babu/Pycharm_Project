from fontTools.misc.cython import returns

str_1 = 'hello world'
print(str_1[::-1])

str_2 = 'hello world hello'
print(str_2.replace(" ",""))
print(str_2.strip())



def check(str_2):
    uniq = []
    dupl = []
    for element in str_2:
        if element not in uniq:
            uniq.append(element)
        else:
            dupl.append(element)

    for el in uniq:
        if el not in dupl:
            print(el)
            break


check(str_2)

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

print(sorted(x+y))
