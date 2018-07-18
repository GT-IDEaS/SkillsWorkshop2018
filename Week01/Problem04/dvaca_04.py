
# coding: utf-8

# In[29]:


## Description
## Calculates the highest palindrom number coming from multiplication of 3-digit numbers

## Weekly Journal
## The code assumes that there will be palondrom numbers with 6-digits. Otherwise, it is neccesary to check the 
#5-digit numbers. The code also identifies the two 3-digit numbers that produced the palindrom number

## Questions
## None

numbers1=list(range(100,1000))
numbers2=list(range(100,1000))
palin=[]
factors=[]
for num1 in numbers1:
    for num2 in numbers2:
        prod=num1 * num2
        prod_str=str(prod)
        if len(prod_str)==6:
            if prod_str[0]==prod_str[5] and prod_str[1]==prod_str[4] and prod_str[2]==prod_str[3]: 
                palin.append(prod)
                factors.append([num1,num2])
i=palin.index(max(palin))
print(max(palin))
print(factors[i])

            
        

