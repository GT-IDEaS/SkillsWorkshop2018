# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:32:50 2018

@author: afilbrun
"""

# Problem 2.

sequence = [1,2];
even_values = [2];
while (sequence[-1] + sequence[-2]) < 4000000:
    sequence.append(sequence[-1] + sequence[-2]);
    if sequence[-1] % 2 == 0:
        even_values.append (sequence[-1])
        
print (sum(even_values))