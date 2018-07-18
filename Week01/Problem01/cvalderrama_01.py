import numpy as np



limit=1000
cumSum=0;
for i in range(1,limit):
        if i%3==0 or i%5==0:
             print i
             cumSum=cumSum+i
            
            
print cumSum