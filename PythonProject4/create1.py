import os

with open("demo1.txt", "a") as new_file1:
    new_file1.write("Hello")

with open("demo1.txt") as new_file1:
    print(new_file1.read())

with open("demo1.txt","w") as new_file1:
    new_file1.write("Hello world")

with open("demo1.txt") as new_file1:
    print(new_file1.read())

os.remove("demo1.txt")