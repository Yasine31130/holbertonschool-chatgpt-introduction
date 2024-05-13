#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Error: Factorial of a negative number is not defined."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if len(sys.argv) > 1:
    try:
        input_number = int(sys.argv[1])
        f = factorial(input_number)
        print(f)
    except ValueError:
        print("Error: Please provide a valid integer number as an argument.")
else:
    print("Usage: python3 script.py <number>")