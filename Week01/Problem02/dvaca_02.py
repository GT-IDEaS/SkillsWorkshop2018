
# coding: utf-8

# In[50]:


## Description
## Adds the Fibonacci numbers smaller than 4 million

## Weekly Journal
## When using while True, "break" MUST be used to avoid infinite loops

## Questions
## None

fib=[1,2]
counter=1
while True:
    if fib[counter]>4000000:
        flag=0
        break
    else:
        fib.append(fib[counter]+fib[counter-1])
        counter+=1
fib=fib[0:len(fib)-1]
total=sum(fib)
print(total)

