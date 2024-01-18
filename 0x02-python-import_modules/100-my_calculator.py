#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4 or sys.argv[2] not in "+-*/":
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, operator, b = map(int, sys.argv[1:])
    operations = {"+": add, "-": sub, "*": mul, "/": div}

    result = operations[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))

