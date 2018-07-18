
# coding: utf-8

# In[62]:


## Description
## Calculates the smallest positve number divisible by all numbers from 1 to 20

## Weekly Journal
## We need to calculate the prime factors of that unknown 
# To do that, we calculate the prime numbers from 1 to 20. Then, check if the composite numbers need an
# extra factor to be calculated and add them to the list. Finally, multiply all numbers
# Only works from 1 to 20 since all the non-prime numbers from 1 to 20 hav2 2 or 3 as factors

## Questions
## None

n=20
primes=[1,2]
for number in list(range(3,n,2)):
    isPrime = True
    for num in list(range(3,number+1,2)):
        if number % num == 0 and number != num:
            isPrime = False
            break
    if isPrime:
        primes.append(number)
primes        
result=1
for i in primes:
    result*=i
for j in list(range(1,n+1)):
    if result % j != 0:
        if (-1)**j == 1:
            result=result*2
        else:
            result=result*3
print(result)
for k in list(range(1,n+1)):
    print(result/k)

    
    

    


