# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:11:19 2018

@author: ademissie6
"""

def divisiblenum(x):
    for i in range (11, 21):
        if x % i != 0:
            return False
        
    return True

x = 2520

while True:
    if divisiblenum(x):
        break

    x += 2520
    
print(x)