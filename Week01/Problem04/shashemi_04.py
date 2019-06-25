palindrome=[]
for i in range(1000,100,-1):
    for j in range(1000,i,-1):
        candidate=i*j
        tst=str(candidate)
        if len(tst)%2==0:
            if tst[-1]==tst[0] and tst[-2]==tst[1] and tst[-3]==tst[2]:
                palindrome.append(candidate)
        else:
            if tst[-1]==tst[0] and tst[-2]==tst[1]:
                palindrome.append(candidate)
print(max(palindrome))
