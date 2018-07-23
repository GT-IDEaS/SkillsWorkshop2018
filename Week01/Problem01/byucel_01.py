def Multiplesof3and5(Max):
    sum=0
    for i in range(Max):
        if i%3==0 or i%5==0 :
         sum+=i
    return sum

print(Multiplesof3and5(1000))


