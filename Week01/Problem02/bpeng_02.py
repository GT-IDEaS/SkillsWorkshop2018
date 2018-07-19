# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Solution:
    def fibon(self,limit):
        fibArray = list()
        fibArray.append(1)
        fibArray.append(2)
        i = 2
        
        while fibArray[-1] <= limit:
            newValue = fibArray[i-1]+fibArray[i-2]
            fibArray.append(newValue)
            i += 1
            
        lenth = len(fibArray)
        total = 0
        
        print (fibArray)
        for i in range(lenth):
            if fibArray[i] % 2==0:
                total += fibArray[i]
        return total
    
sol = Solution()
print(sol.fibon(4000000))
    
        