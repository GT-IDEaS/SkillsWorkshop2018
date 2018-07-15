#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:39:27 2018

@author: baijiepeng
"""

import math
class Solution:
    
    def prifactor(self,number):
        priFactor = -1
        while number%2 == 0:
            priFactor = 2
            n /= 2

        for i in range(3, int(math.sqrt(number)+1),2):
            while number % i == 0:
                priFactor = i
                number /= i
                
        if number > 2:
            priFactor = number
        return priFactor

sol = Solution()
print(sol.prifactor(600851475143))