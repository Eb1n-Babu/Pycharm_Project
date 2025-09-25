from PythonProject1.demo_project.string import count


class hello:
    @staticmethod
    def hello_():
        print('hello')

hello.hello_()


import sys
x = [1, 2, 3 ,4]  # Ref count increases
print(sys.getrefcount(x))  # >1 due to internal refs


list1 = [1,2,[3,4,],5,[6,[7,[8],],6],7]

input_str = "aaabbcca"
output = "3a2b2c1a"
count = 0

for i in range (len(input_str)):
    if i > len(input_str):
        break
        if input_str[i] == input_str[i+1]:
            count+=1
        else:
            count += 1
    print(count)
