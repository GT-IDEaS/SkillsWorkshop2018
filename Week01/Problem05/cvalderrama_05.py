# -*- coding: utf-8 -*-
import numpy as np


numbers = np.arange(2,21)
factors= np.array([])

factor=2
while sum(numbers)!=numbers.size:    
    stop = False
    while not stop:
        thereIs = False
        for i in range(numbers.size):
            if numbers[i]%factor==0:
                numbers[i] = numbers[i] /factor
                thereIs = True
                
        
        if not thereIs:
            stop=True
            factor=factor+1
            
        else:
            factors = np.append(factors,factor)
    

print np.prod(factors)