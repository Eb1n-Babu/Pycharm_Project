a = [12,14,15]
x,y,z = a
print(x,y,z)


x = "hello"
y = "world"
print(x+y)


print("hello","world")

y = 5
def x():
    global x
    print(x)

x = 5
print(complex(x))

x = "hello world"
print("hello" in x)

list_  = ((1,23,456,7,))
print(type(list_))

k = [1,2,3,4,5]
f = [4,5,6,7,8]
print(k+f)
print(f+k)
k.extend(f)
print(k)

x = "hello world"
print(x[::-1])
