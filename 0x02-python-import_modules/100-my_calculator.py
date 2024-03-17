#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div
from sys import argv
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(argv[1])
sign = argv[2]
b = int(argv[3])

if sign == '+':
    result = add(a, b)
elif sign == '-':
    result = sub(a, b)
elif sign == '*':
    result = mul(a, b)
elif sign == '/':
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print(f"{a} {sign} {b} = {result}")
