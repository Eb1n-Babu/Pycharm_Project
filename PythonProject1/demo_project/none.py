# Return None if input is negative, otherwise return square
def compute_square(value):
    if value < 0:
        return None
    return value ** 2

print("Square of 4:", compute_square(4))
print("Square of -3:", compute_square(-3))
