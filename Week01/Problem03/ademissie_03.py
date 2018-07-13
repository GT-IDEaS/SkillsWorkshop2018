# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:23:54 2018

@author: ademissie6
"""

import math

number =600851475143
 
def isPrime(factor):
    for pfactors in range(2,int(math.sqrt(factor))+1):
        if factor % pfactors == 0:
            return False
 
    return True

for pfactors in range(2, number + 1):
      if isPrime(pfactors) and number % pfactors == 0:
         
         print(max(pfactors))
    