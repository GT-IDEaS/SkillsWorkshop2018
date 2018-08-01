"""
This script implements a solution to Project Euler Problem 4
by finding the largest palindromic number that is a product
of two three-digit numbers.

@author: Andrew Sedler
"""

import numpy as np

nums = np.arange(100, 1000)

products = sorted([n1*n2 for n1 in nums for n2 in nums], reverse=True)

for product in products:
    if str(product) == str(product)[::-1]: break

print(product)
