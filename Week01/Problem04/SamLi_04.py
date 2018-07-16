# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 03:54:12 2018

@author: Sam Li
"""

the_largest_palindrome=0
for ii in range(000, 1000):
    for jj in range(000, 1000):
        the_num = ii*jj
        if the_num > the_largest_palindrome:
            bb=str(the_num)
            if bb==bb[::-1]:
                the_largest_palindrome=the_num # this is the answer
            