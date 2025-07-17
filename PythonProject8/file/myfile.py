with open("hello.txt","rt") as f:
    print(f.read())

with open("hello.txt","at") as f:
    f.writelines("second hello")

with open("hello.txt","rt") as f:
    print(f.read())
