import json

with open(r"hello.json","r") as f:
   print(f.read())


x = {
  "id": 101,
  "name": "Ebin",
  "email": "ebin@example.com",
}

y = json.loads(x)
print(y)