import matplotlib
import numpy
import math as m 
def FacMult(x,y):
    """Determines what to multiply y with such that it is divided by x"""
    if y%x==0:
        """returns 1 if now multiplication is needed"""
        return [1]
    else:
      """otherwise it factorizes x and stores the factors in Factor list"""
      count=0
      Max=x/2
      Max=int(Max)
      Factor=[1]
      Mult=[1]
      for i in range(2,Max):
        if x%i==0:
           Factor=Factor+[i]
      if len(Factor)==1:
          """If x is a prime number"""
          Factor=Factor+[x]
      for h in range(1,len(Factor)):
        """Then it checks which multiples of x y needs to be multiplied with"""
        M=Factor[h]
        if y%M==0:
           y=y/M
        else:
          Mult=Mult+[M]
      return Mult
Start=20    
for Num in range(3,19):
    MultList=FacMult(Num,Start)
    for M in range(1,len(MultList)):
        P=MultList[M]
        Start=Start*P
print(Start)
