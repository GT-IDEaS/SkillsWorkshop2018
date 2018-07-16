#!/usr/bin/env python

fibonacci=[]
fibonacci.append(1)
fibonacci.append(2)
evensum=2
i=1
fibonaccinum=0
while (fibonaccinum<4000000):
    fibonaccinum=fibonacci[i-1]+fibonacci[i]
    fibonacci.append(fibonaccinum)
    if fibonaccinum%2==0:
        evensum=evensum+fibonaccinum
    i+=1
print(evensum)
    
