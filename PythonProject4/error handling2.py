try:
    for i in range(10):
        y = 10/i
except ZeroDivisionError:
    print("division by zero")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

