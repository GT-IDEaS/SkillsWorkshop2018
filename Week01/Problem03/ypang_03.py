import numpy as np

target = 600851475143
#target = 13195 

#INT
primes = np.empty(1000,dtype=int)
counters = np.empty(1000,dtype=int)
n = 0
i = 3

print("TARGET = ", target)

#manual check 2
while(target % 2 == 0):
    target /= 2;

print("Try dividing by: 2, remainder =",target)


while i*i <= target:
    for j in range(n):
        counters[j] += 2
        if(counters[j] >= primes[j]):
            counters[j] -= primes[j]

# if none of the counters are zero, it is a prime
    if not any(counters[:n] == 0):
        primes[n] = i
        counters[n] = 0
        n += 1

        while(target % i == 0):
            target //= i;

        print("Try dividing by:",i, ", remainder =",target)

    i += 2
        

if(target == 1):
    print("LARGEST PRIME FACTOR = ", primes[n-1])
else:
    print("LARGEST PRIME FACTOR = ", target)

