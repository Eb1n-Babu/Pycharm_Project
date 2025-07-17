from PythonProject8.exception2.oprations import operations


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = input("enter operations to be performed: ")


if __name__ == '__main__':
    try:
       operations(x,y,z)
    except ZeroDivisionError:
        print("You can't divide by zero")
    except TypeError:
        print("invalid TypeError")
    except RuntimeError:
        print("invalid operation")
    except ValueError:
        print("invalid value")


