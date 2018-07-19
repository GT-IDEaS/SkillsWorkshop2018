#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:38:16 2018

@author: baijiepeng
"""
class Solution:
    ## DP approach
    def smallMul(self,num):
        
        dp = [0 for i in range(num+1)]
        dp[1]=1
        for currentNum in range(2, num+1): 
            for j in range(1,currentNum+1): #j is multiplyers looped
                dp[currentNum]=dp[currentNum-1]*j
                if dp[currentNum] % currentNum == 0:
                    break
        return(dp[-1])
                
sol = Solution()
sol.smallMul(20)
                
        