"""
This script implements a solution to Project Euler Problem05 
by finding the smallest number that is evenly divisible by 
every number smaller than 20.

@author: Andrew Sedler
"""

# Define function to compute the Greatest Common Denominator
gcd = lambda a, b: (gcd(b, a % b) if a % b else b)

# Compute number that factors with every number from 1 to 20.
# When it doesn't it factor, it will be multiplied by that number so
# it does.
n = 1
for fac in range(1,21):
    g = gcd(n, fac)
    n = n * fac / g

print(int(n))

