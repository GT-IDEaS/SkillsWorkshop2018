# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:28:32 2018

@author: sezen
"""

#lpf = largest prime factor
def lpf(x):
    
    factors = []
    factor = 2
    while factor <= x:
        if x % factor == 0:
            x=x/factor
            factors.append(factor)
        else:
            factor = factor + 1
            
    return max(factors)
            

print(lpf(600851475143))
