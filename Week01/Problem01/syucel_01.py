# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 14:10:26 2018

@author: sezen
"""
import math
a = 3
b = 5
num = 1000-1
max_a = math.floor(num/a)
max_b = math.floor(num/b)

multiples_a = []
multiples_b = []

for i in range(1,max_a+1):
    multiples_a.append(i*a)
for i in range(1,max_b+1):
    multiples_b.append(i*b)
    
all_multiples = list(set(multiples_a) | set(multiples_b))

print(sum(all_multiples))