def divide(x, y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("zero division error")
    except TypeError:
        print("wrong type")
    except NameError:
        print("wrong name")
    except IndexError:
        print("wrong index")


divide(1, 2)
divide(1, "5")
divide(1, -1)
divide(1, str(5))
divide(1, y = "c")