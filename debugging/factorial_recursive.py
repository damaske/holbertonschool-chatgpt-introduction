#!/usr/bin/python3
import sys

def factorial(n):
    """
    colculate the factorial recursively
    n (int): factorial calculated for this integer
    return: factorial of `n`. If `n == 0`, returns 1, as 0! = 1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Reading the argument from the command line, converting it to an integer, and calculating the factorial
f = factorial(int(sys.argv[1]))
# Printing the result of the factorial calculation
print(f)
