# This program is for adding even numbers of the Fibonacci sequence less than 4 million

import copy
M=4000000   # This is the maximum value for fibonacci sequence


Xt=1
Xdt=1
X=1
FSum=0
while Xt < M:
      X=Xt
      Xt=Xt+Xdt
      Xdt=X
      R= Xt % 2
      if R == 0:
         FSum=FSum+Xt

print('The summation of even numbers in Fibonacci sequence is {}'.format(FSum))
