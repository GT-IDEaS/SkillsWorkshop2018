# -*- coding: utf-8 -*-

import numpy as np


top = 4000000

fibo1 = 2
fibo2=  1
cumSum = 2
while fibo1 < top:
    temp = fibo1
    fibo1 = fibo1+fibo2
    fibo2 = temp
    
    if fibo1%2==0 and fibo1<top:
        print fibo1
        cumSum=cumSum+fibo1
        

  
  

print cumSum
