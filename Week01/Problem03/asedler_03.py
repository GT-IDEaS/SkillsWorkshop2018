"""
This script implements a solution to Project Euler Problem 03
by finding the largest prime factor of 600851475143.

@author Andrew Sedler
"""

# Assign the number to be factored
x = 600851475143

# Start with the smallest prime
i = 2

while i*i <= x:
    if x % i:
        i+=1
    else:
        x //= i

print(x)
