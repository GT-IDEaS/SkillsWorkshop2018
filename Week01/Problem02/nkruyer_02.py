# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 21:06:54 2018

@author: nkruyer3
"""

#Week 1 Assignment: Problem 2 - Nick Kruyer
#Correct answer 4613732

fib_list = [1,2]

while fib_list[-1] + fib_list[-2] < 4000000:
    fib_list.append(fib_list[-1]+fib_list[-2])
    
total = 0
for i in range(len(fib_list)):
    if fib_list[i]%2 == 0:
        total += fib_list[i]
        
print(total)
