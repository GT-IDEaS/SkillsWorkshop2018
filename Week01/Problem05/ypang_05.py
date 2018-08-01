import numpy as np

# Too lazy to copy Q3 ans, so just predefine primes
primes = np.array([2,3,5,7,11,13,17,19])
buckets = np.zeros_like(primes)

def findFactors(x):
    factors = []
    for i in range(len(primes)):
        p = primes[i]
        while(x % p == 0):
            x //= p
            factors.append(i)

    return factors

for i in range(2,21):
    factors = findFactors(i)
    print(i, ":", [primes[x] for x in factors])

    mybuckets = np.zeros_like(buckets)
    for j in factors:
        mybuckets[j] += 1

    for j in range(len(mybuckets)):
        if(buckets[j] < mybuckets[j]):
            buckets[j] = mybuckets[j]

ans = 1;
for i in range(len(primes)):
    ans *= primes[i] ** buckets[i]

print(ans)

