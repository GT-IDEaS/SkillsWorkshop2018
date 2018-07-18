import math


##answer:6857
def Largest_Prime_Factors(n):

    largestPrime = -1

    while n % 2 == 0:
        largestPrime = 2
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largestPrime = i
            n = n / i

    if n > 2:
        largestPrime = n

    return int(largestPrime)

n = 600851475143
print(Largest_Prime_Factors(n))
