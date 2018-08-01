"""
This script implements a solution to Project Euler Problem01
by finding the sum of the multiples of 3 or 5 below 1000.

@author: Andrew Sedler
"""

import numpy as np

nums = np.arange(1000)
multiples = []

for num in nums:
    if not num % 3 or not num % 5:
        multiples.append(num)

print(sum(multiples))
