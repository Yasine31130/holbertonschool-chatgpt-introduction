#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) > 1:  # Check if an argument is provided
    try:
        input_number = int(sys.argv[1])  # Ensure the input can be converted to an integer
        f = factorial(input_number)
        print(f)
    except ValueError:  # Handle the case where the input is not an integer
        print("Please provide an integer number as an argument.")
else:
    print("Please provide a number as an argument.")