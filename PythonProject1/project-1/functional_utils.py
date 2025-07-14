square = lambda x: x ** 2

def apply_map(numbers):
    return list(map(lambda x: x ** 2, numbers))

def apply_filter(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))
