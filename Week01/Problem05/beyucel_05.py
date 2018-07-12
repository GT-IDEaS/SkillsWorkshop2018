#First Solution
def SmallestDivisiable(MaxRange):
    D=20
    while True:
        Divisors=[]
        for i in range(1,MaxRange+1):
            if D%i!=0:
                break
            Divisors.append(i)

        if len(Divisors)==MaxRange:
            break
        D+=1
    return D

#print (SmallestDivisiable(20))

# Answer  232792560
# It is a really in efficient code and almost took 2-3 min to solve it

#Second Solution  much Faster solution with Prime number factorization
from collections import Counter
import numpy as np
def Factorize(Max):
    globalFactors=[]
    for n in range(2,Max+1):
        PrimeDivisors=[]
        i=2
        while n>=i:
            if n%i==0:
                n=n/i
                PrimeDivisors.append(i)
            else:
                i+=1

        combined = Counter(globalFactors) | Counter(PrimeDivisors)
        globalFactors=list(combined.elements())

    return (np.prod(globalFactors))


print(Factorize(20))
