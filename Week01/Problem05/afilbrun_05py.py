# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:32:50 2018

@author: afilbrun
"""

# Problem 5

divisible = [];
test = 2520;

while divisible == []:
    if all (test % val == 0 for val in range(11,21)):
        divisible.append(test);
    test += 2520
print (divisible);