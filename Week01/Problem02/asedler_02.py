"""
This script implements a solution to Project Euler Problem 02
by summing the even-valued terms of the Fibbonacci sequence
that are less than 4 million.

@author: Andrew Sedler
"""

fib = [1,2]

while fib[-1] < 4000000:
    fib.append(fib[-2] + fib[-1])

even_sum = sum([n for n in fib[:-1] if not n % 2])

print(even_sum)
