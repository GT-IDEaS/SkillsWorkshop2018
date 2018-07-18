# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:12:57 2018

@author: nkruyer3
"""

#Week 1 Assignment: Problem 4 - Nick Kruyer
#correct answer = 906609

#reverses a string
def rev_str(x):
    rev = ''
    x = str(x)
    for i in range(1,len(x)):
        rev += x[-i]
    return rev+x[0]

#determines if a number is a palindrome (test = 0, no - test = 1, yes)
def is_pal(x):
    x=str(x)
    rev = rev_str(x)
    if x == rev:
        test = 1
    else:
        test = 0
    return test

top = 0
for i in range(100,999):
    for j in range(100,999):
        num = i*j
        if is_pal(num) == 1:
            if num > top:
                top = num
            else:
                top = top
        else:
            top = top
 

print(top)           