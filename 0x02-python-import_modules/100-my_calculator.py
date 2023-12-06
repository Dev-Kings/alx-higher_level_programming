#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg_count = len(sys.argv)
    if arg_count < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if sys.argv[2] in ['+', '-', '*', '/']:
            if operator == '+':
                result = add(a, b)
            elif operator == '-':
                result = sub(a, b)
            elif operator == '*':
                result = mul(a, b)
            elif operator == '/':
                result = div(a, b)
            print("{} {} {} = {}".format(a, operator, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
