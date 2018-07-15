# -*- coding: utf-8 -*-
import numpy as np



def findMaxPali():
    
    maxNum = 0
    for i in range(1000,99,-1):
        for j in range(1000,99,-1):
            p = i*j
            p_str=str(p)
            v=p - int(p_str[::-1])==0                      
            if p - int(p_str[::-1])==0:
               if maxNum<p:
                   maxNum=p
                   print maxNum
    
    return maxNum