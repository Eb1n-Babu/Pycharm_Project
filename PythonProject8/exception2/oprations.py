def operations(x, y, z):
    operation = ['+', '-', '*', '/']
    if z in operation:
        if z == '+':
            print(x + y)
        elif z == '-':
            print(x - y)
        elif z == '*':
            print(x * y)
        elif z == '/':
            print(x / y)
            print(x % y)
    else:
        raise RuntimeError

