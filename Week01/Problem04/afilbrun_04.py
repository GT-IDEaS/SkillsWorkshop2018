# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:32:50 2018

@author: afilbrun
"""

# Problem 4
palindrome = []; 
for first in range (100,1000):
    for second in range (100,1000):
        num = first * second;
        if str(num) == str(num)[::-1]:
            palindrome.append(num)
print (max(palindrome));