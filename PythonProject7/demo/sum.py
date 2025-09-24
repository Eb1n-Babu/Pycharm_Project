def sumOf(n):
    y = n * (n + 1) / 2
    return f"some of {n} is {y}"


if __name__ == '__main__':
    for i in range(100):
        print(sumOf(i))
