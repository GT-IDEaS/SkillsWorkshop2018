import numpy as np

def buildPrimeList(maximum):
    primes = [2]

    for i in range(3,maximum+1,2):  # even numbers can be skipped
        isPrime = True
        for p in primes[1:]:
            if(i%p == 0):
                isPrime = False
                break

        if(isPrime):
            primes.append(i)

    return primes


""" MAIN """
target = 13195

myPrimes = buildPrimeList(target)
print(myPrimes)

ans = 1    
for i in reversed(myPrimes):
    if(target % i == 0):
        ans = i
        break

print(i)

