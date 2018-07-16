
import math


def Palindromic(x):
      number=x
      reverse=0
      while number != 0:
            
         reverse = reverse * 10 +  number % 10
         number = number//10
            
            
      if x==reverse:
         
             return True



min_num=99
max_num=999
result=0
for i in range (max_num,min_num,-1):
      for j in range (i,min_num,-1):
      
          num=i*j 
          
          if Palindromic(num) and num>result:
             result=num
          
          
      
print('The Palindromic number is {}'.format(result)) 









