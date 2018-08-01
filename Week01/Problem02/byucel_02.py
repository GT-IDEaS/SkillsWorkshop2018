def evenFibonaccitill4Mil(Max):
    StarterList=[1,2,3]
    sum=2
    while True:
        newfib=StarterList[-1]+StarterList[-2]
        if newfib>Max:
            break
        elif newfib%2==0:
            sum+=newfib

        StarterList.append(newfib)
    return (sum)

print(evenFibonaccitill4Mil(4000000))


