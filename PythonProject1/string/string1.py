str1 = "hello world"
for i in range(0,len(str1)):
    print(str1[i],end=" ")

print(" ")


str3 = "hello world"
for i in range(len(str3)-1,-1,-1):
    print(str3[i],end=" ")

print()

str4 = "REAL MADRID"
print(str4[0])
print(str4[1])
print(str4[-1])
print(str4[0:1])
print()
print(str4[1:0])
print(str4[0:2])
print(str4[0:4])
print(str4[1:5])
print(str4[1:-1])
print(str4[::-1])
print(str4[::1])


for ch in str4:
    print(ch)

