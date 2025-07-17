from PythonProject8.exception2.oprations import operations


if __name__ == '__main__':
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        z = input("enter operations to be performed: ")
        operations(x,y,z)
    except ZeroDivisionError:
        print("You can't divide by zero")
    except TypeError:
        print("invalid TypeError")
    except RuntimeError:
        print("invalid operation")
    except ValueError:
        print("invalid value")


