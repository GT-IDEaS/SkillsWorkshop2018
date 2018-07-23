# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Solution:
    def sumofmultiples(self,limit):
        numbers = []
        for i in range(1,limit):
            if i % 3 == 0 or i % 5 == 0:
                numbers.append(i)
        print(sum(numbers))
        return sum(numbers)
    
sol = Solution();
sol.sumofmultiples(1000)
        
    
        