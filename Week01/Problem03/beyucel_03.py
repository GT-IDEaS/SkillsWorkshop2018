def LargestPrimeFactor(n):
    PrimeDivisors=[]
    i=2
    while n>=i:
        if n%i==0:
            n=n/i
            PrimeDivisors.append(i)
        else:
            i+=1
    print (PrimeDivisors)
    return max(PrimeDivisors)

print(LargestPrimeFactor(600851475143))
