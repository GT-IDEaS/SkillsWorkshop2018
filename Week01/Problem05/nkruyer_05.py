# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:38:06 2018

@author: nkruyer3
"""

#Week 1 Assignment: Problem 5 - Nick Kruyer
#Correct answer = 232792560

x = 0
num = 0
add = 20

while x == 0:
    div = 19
    num += div*add
    y = num%div
    while y == 0:
        div -= 1
        y += num%div
        if div == 10:
            x = 1
            y = 1
    
print(num)
    