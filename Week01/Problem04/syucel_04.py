# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:46:58 2018

@author: sezen
"""

palindrome = []
for a in range(100,1000):
    for b in range(100,1000):
        num = a*b
        text_num = str(num)
        if text_num == text_num[::-1]:
            palindrome.append(num)

print(max(palindrome))