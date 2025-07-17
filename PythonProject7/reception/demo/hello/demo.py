import os

if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    os.mkdir("hello.txt")