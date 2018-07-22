import numpy as np

#
#Here is a general solution to the largest prime numbers problem.:
#
def largest_prime(n):
    p = 2
    primes = []
    while p*p <= n:
        if (n%p) == 0:
            primes.append(p)
        p += 1
    #Check each value in list to ensure they are prime numbers.
    for i in primes:
        x = np.arange(2, i)
        for j in x:
            if (j<i) and (i/j).is_integer():
                ind = np.where(primes == i)
                primes = np.delete(primes, ind)
    return 'The largest prime factor of ' + str(n) + ' is ' + str(np.max(primes))

#
# Alternatively, here is the direct solution which will print upon typing `python dskinner_03.py`
#
n = 600851475143
p = 2 
prime = []
while p*p <= n:
    if (n%p) == 0:
        prime.append(p)
    p += 1
#Check each value in list to ensure they are prime numbers.
for i in prime:
    x = np.arange(2, i)
    for j in x:
        if (j<i) and (i/j).is_integer():
            ind = np.where(prime == i)
            prime = np.delete(prime, ind)
print('The largest prime factor of ' + str(n) + ' is ' + str(np.max(prime)))