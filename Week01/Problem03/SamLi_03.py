# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 02:15:17 2018

@author: Sam Li
"""

the_number=600851475143
primes_array=[]
upperlimit = the_number
ii=2
while ii <= upperlimit:
    if the_number % ii == 0:
        ii_is_not_prime = 0
        for prime_num in primes_array:
            if ii % prime_num == 0:
                ii_is_not_prime = 1
                break
        if ii_is_not_prime == 0:
            primes_array.append(ii)
            if len(primes_array)==1:
                upperlimit=the_number/primes_array[0]
    ii=ii+1                
the_largest_prime_factor=primes_array[-1]   # this is the answer