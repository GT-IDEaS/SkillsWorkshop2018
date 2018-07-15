# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:00:33 2018

@author: nkruyer3
"""

#Week 1 Assignment: Problem 1 - Nick Kruyer
#correct answer 233168

total = 0

for i in range(1000):
    if i%3 == 0:
        total += i
    elif i%5 == 0:
        total += i

print(total)
    
    