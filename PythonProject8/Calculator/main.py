from CalcultorIndex import Calculator

def main():
    trigger = input("Press 'q' to start: ").strip().lower()
    if trigger != 'q':
        print("Exiting: You didn't press 'q'")
        return

    calc = Calculator()

    print("Choose operation: add, sub, mul, div")
    op = input("Operation: ").strip()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operations = {
        'add': calc.add,
        'sub': calc.sub,
        'mul': calc.mul,
        'div': calc.div
    }

    if op in operations:
        result = operations[op](a, b)
        print("Result:", result)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()