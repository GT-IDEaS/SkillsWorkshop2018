#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:59:00 2018

@author: baijiepeng
"""
class Solution:
    def isParlindrome(self,number):
        numberString = str(number)
        lenNumber = len(numberString)
        parlindrome = False
        for i in range(lenNumber//2 + 1):
            if numberString[i] != numberString[-i-1]:
                parlindrome = False
                break
            elif numberString[i] == numberString[-i-1]:
                parlindrome = True
        return parlindrome
        
        
    def LPP(self,bound):
        maxNum = 0
        product = 0
        for i in range(bound):
            for j in range(bound):
                product = i*j
                parlindrome = self.isParlindrome(product)
                if parlindrome == True:
                    maxNum = max(maxNum,product)
        return maxNum

sol = Solution()
print(sol.LPP(1000))
                