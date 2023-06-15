#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ["+", "-", "/", "*"]
    i = sys.argv[2]

    if i not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if i == "+":
        print("{} {} {} = {}".format(a, i, b, add(a, b)))
    elif i == "-":
        print("{} {} {} = {}".format(a, i, b, sub(a, b)))
    elif i == "/":
        print("{} {} {} = {}".format(a, i, b, div(a, b)))
    elif i == "*":
        print("{} {} {} = {}".format(a, i, b, mul(a, b)))
