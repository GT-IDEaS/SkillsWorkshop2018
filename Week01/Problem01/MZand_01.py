# This program computes Multiplies of two numbers X or Y in range of 1 to M.


import numpy  
import math
M=1000     # M is the maximum number  
X=3        # First number
Y=5        # Second number
Sum_mult=0

Xind=range(1,math.ceil(M/X))
Yind=range(1,math.ceil(M/Y))
XYind=range(1,math.ceil(M/(X*Y)))
X_Mult=[k*X for k in Xind]
Y_Mult=[k*Y for k in Yind]
XY_Mult=[X*Y*k for k in XYind]   # this line is to identify common multiplies of X and Y

Sum_Mult=sum(Y_Mult)+sum(X_Mult)-sum(XY_Mult)  # compute summation of unique multiplies of X and Y



print('The Summation of the values is {}'.format(Sum_Mult))
