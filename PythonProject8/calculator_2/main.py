from calculator_index import *

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = input("Enter operation: ")
op = ['+', '-', '/', '*']

if __name__ == '__main__':
    try:
        if z in op:
            if z == '+':
                print(x + y)
            elif z == '-':
                print(x - y)
            elif z == '*':
                print(x * y)
            elif z == '/':
                print(x / y)
        else:
            print("Invalid operation")
    except ZeroDivisionError:
        print("Invalid operation")
    except ValueError:
        print("Invalid operation")
    except ArithmeticError:
        print("Invalid operation")

