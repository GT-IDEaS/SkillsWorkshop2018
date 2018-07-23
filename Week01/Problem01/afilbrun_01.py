# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:32:50 2018

@author: afilbrun
"""

# Problem 1.

multiples = list();
for value in range(1000):
    if value % 3 == 0 or value % 5 == 0:
     multiples.append(value);

print (sum(multiples));