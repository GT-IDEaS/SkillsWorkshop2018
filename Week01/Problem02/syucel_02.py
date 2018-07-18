# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 14:20:52 2018

@author: sezen
"""

fib = []
fib.append(1)
fib.append(1)
fib_even = []
n = 0
while fib[n] <= 4000000:
        fib.append(fib[n] + fib[n+1])
        if fib[n] % 2 == 0:
            fib_even.append(fib[n])
        n = n+1
        
print(sum(fib_even))