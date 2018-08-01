import math
def Fac(x):
#finds the largest factor for x, or returns that it is a prime number
#the max number that should be considered
   Max=math.sqrt(x)
   MaxNum=int(Max)
#starting number is two
   Fact=2
   while Fact<=MaxNum:
#increases the potential factorial until a factorial number is found  
     if x%Fact==0:
#if a factorial is found it returns x/factorial, that is the largest factorial
#of x, and breaks the loop
       return int(x/Fact)
       break
     else:
       Fact+=1
#if the loop was never broken x must be a prime number and that will be returned
   return "Prime"

number=600851475143
while Fac(number)!="Prime":
#determines the largest factorial recursively untill it finds one that is a 
#prime number
   LastFac=number
   number=Fac(number)
print(number) 

