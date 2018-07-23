def IsPal(num):
    numstr=str(num)
    if numstr==numstr[::-1]:
        ans= True
    else:
        ans= False
    return ans

def LargestPali():
    Palnumbers=[]
    for i in range(999,10,-1):
        for j in range(999,10,-1):
            mul=i*j
            if IsPal(mul):
                Palnumbers.append(mul)

    return max(Palnumbers)


print(LargestPali())

