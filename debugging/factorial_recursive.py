#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number using recursion.
    
    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.
    
    Returns:
    int: The factorial of the number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Taking an integer input from command line arguments and computing its factorial
f = factorial(int(sys.argv[1]))

# Outputting the factorial result
print(f)