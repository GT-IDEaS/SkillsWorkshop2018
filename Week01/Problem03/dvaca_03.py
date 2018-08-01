
# coding: utf-8

# 
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
# 

# In[2]:


## Description
## Calculates the highest prime factor of a number

## Weekly Journal
## At the beginning, the for loop run until n, but it was taking too long to solve. Searching in Internet, I found that it
## the iterarion must be until sqrt(n). That reduced subtantially tthe time to solve.

## Questions
## None
import math
n=600851475143
factors=[]
#In case n is even, divides n by 2
while n%2==0:
    n=n/2
    factors.append(2)
for number in list(range(3,int(math.sqrt(n))+1,2)):
    while n % number==0:
        n=n/number
        factors.append(number)
if n>2:
    factors.append(number)
max_factor=max(factors)
print(factors)
print(max_factor)


    

