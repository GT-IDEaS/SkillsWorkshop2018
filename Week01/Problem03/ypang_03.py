import numpy as np

"""This program aim to:
    1) on the fly construct a list of prime number
    2) strip out all the prime factor from target """

input_num = 600851475143
#input_num = 13195 

#INT
primes = np.empty(1000,dtype=int)
counters = np.empty(1000,dtype=int)
target = input_num
factors = []
n = 0

print("TARGET = ", target)

#manual check 2
while(target % 2 == 0):
    target //= 2
    factors.append(2)

print("Try dividing by: 2, remainder =",target)


# Loop through all the odd numbers to find primes
# until all the factors are found
i = 3
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

# try strip factors from target using the newly found prime
        while(target % i == 0):
            target //= i
            factors.append(i)


        print("Try dividing by:",i, ", remainder =",target)

    i += 2
        

# OUTPUT
if(target == 1):
# write a pythonic statement in case my TA complains I am writing C
    print(input_num, "=", " x ".join([str(x) for x in factors]))
    print("LARGEST PRIME FACTOR = ", primes[n-1])
else:
    factors.append(target)
    print(input_num, "=", " x ".join([str(x) for x in factors]))
    print("LARGEST PRIME FACTOR = ", target)

