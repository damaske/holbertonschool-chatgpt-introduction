#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    return result

newf = factorial(int(sys.argv[1]))
print(newf)
