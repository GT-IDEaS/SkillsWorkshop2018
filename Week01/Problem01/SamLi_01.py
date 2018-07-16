# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:08:03 2018

@author: Sam Li
"""

upperlimit = 1000
integer1 = 3
integer2 = 5
integer3 = integer1*integer2
highest_multiplier1 = upperlimit//integer1
highest_multiplier2 = upperlimit//integer2
highest_multiplier3 = upperlimit//integer3
sum1 = integer1 * highest_multiplier1*(highest_multiplier1+1)/2
sum2 = integer2 * highest_multiplier2*(highest_multiplier2+1)/2
sum3 = integer3 * highest_multiplier3*(highest_multiplier3+1)/2
sum_final = sum1+sum2-sum3   # This is the answer