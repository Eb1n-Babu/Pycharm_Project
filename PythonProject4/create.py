""""x" - Create - will create a file, returns an error if the file exists
"a" - Append - will create a file if the specified file does not exists
"w" - Write - will create a file if the specified file does not exists"""

"""f = open("new_test.txt", "x")"""
with open("new_test.txt", "a") as f2:
    f2.write("hello world new")

with open("new_test.txt") as f:
  print(f.read())
"""To overwrite the existing content to the file, use the w parameter:"""
with open("new_test.txt", "w") as f2:
    f2.write("hello world newrrrr")

with open("new_test.txt") as f2:
    print(f2.read())

