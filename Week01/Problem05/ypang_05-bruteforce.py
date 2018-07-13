test = 20
for i in range(test,10000000000, test):
    isSolu = True
    for j in range(3,test): # no need to check 1 (integer) and 2 (even)
        if(i%j!=0):
            isSolu = False
            continue
    if(isSolu):
            break

print(i)
