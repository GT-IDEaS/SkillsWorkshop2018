# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:24:58 2018

@author: sezen
"""  
#function for finding prime factors          
def pf(x):  
    factors = []
    factor = 2
    while factor <= x:
        if x % factor == 0:
            x=x/factor
            factors.append(factor)
        else:
            factor = factor + 1
                
    return factors

#counting occurrence of each prime factor
from collections import Counter
cnt = Counter(pf(2))

for i in range(3,21):
    l = pf(i)
    cnt = cnt | Counter(l) #union of all prime factor occurences

all_primes = list(cnt.elements()) #list version of Counter object

#multiplication of the elements in 'all_primes' list
import numpy as np
result = np.prod(np.array(all_primes)) 
print(result)