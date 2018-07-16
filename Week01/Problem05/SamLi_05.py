# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 04:19:19 2018

@author: Sam Li
"""


jj=20
jj_is_the_smallest_positive_number=0
while jj_is_the_smallest_positive_number==0:
    jj_is_the_smallest_positive_number=1
    for ii in range(2, 21):
        if jj % ii !=0:
            jj_is_the_smallest_positive_number=0
            break
    if jj_is_the_smallest_positive_number==1:
        the_smallest_positive_number=jj  # this is the answer
        break
    else:
        jj=jj+20