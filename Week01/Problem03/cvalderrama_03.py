# -*- coding: utf-8 -*-
import numpy as np


def isPrime(x):
    counter=0
    i=2
    while i<np.sqrt(x) and counter==0:
        if x%i == 0:
            counter=counter+1
        i = i+1
    return counter==0



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
 