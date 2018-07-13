# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:03:15 2018

@author: ademissie6
"""

def ispalindrome(a):
    return str(a) == str(a)[::-1]

biggestpalindrome = 0
for a in range(100, 999):
    for b in range(a+1, 1000):
        p = a * b
        if ispalindrome(p) and p > biggestpalindrome:
            biggestpalindrome = p

print (biggestpalindrome)