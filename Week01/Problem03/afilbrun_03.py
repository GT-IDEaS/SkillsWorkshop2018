# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:32:50 2018

@author: afilbrun
"""

# Problem 3.

import math
value = 600851475143;

factors = [];
prime_factors = [];

for n in range(int(math.sqrt(value)),2,-1):
    if value % n == 0:
        factors.append(n);
        x = [];
        for i in range(n-1,1,-1):
            if n % i == 0:
                x.append(i);
        if not x:
           # prime_factors.append(n);
           max_prime_factor = n;
           break
           
print (max_prime_factor) 