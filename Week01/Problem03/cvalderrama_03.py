# -*- coding: utf-8 -*-
import numpy as np






n = 600851475143 

maxPrime=-1
while n % 2 == 0:
    maxPrime = 2
    n = n/2 
        
print n
for i in range(3,int(np.sqrt(n)) + 1,2):
    while n % i == 0:
        maxPrime = i
        n = n / i
        

if n > 2:
    maxPrime = n
    
print maxPrime
 
