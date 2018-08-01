
def getSmallestFactor(number):
    for n in range(2, number):
        if(number % n == 0):
            return n
        
    return number


tre= 600851475143

primes = []
while(True):
    prime = getSmallestFactor(tre)
    primes.append(prime)
    if (prime == tre):
        break
        
    tre = tre // prime
  
    
print(max(primes))
    

