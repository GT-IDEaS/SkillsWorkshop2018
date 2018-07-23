import numpy as np

def getFibonacci(maximum):
    n = 2
    maxlen = 1000
    ans = np.empty(maxlen, dtype=int)
    ans[0] = 1
    ans[1] = 2

    for i in range(2,maxlen):
        ans[i] = ans[i-2] + ans[i-1]
        if(ans[i] > maximum):
            break
        n += 1
        
    return ans[:n]


def getEven(array):
    n = 0
    ans = np.empty(len(array), dtype=int)

    for i in array:
        if(i%2 == 0):
            ans[n] = i
            n += 1

    return ans[:n]
        



"""MAIN"""

fibSeq = getFibonacci(4000000)
evenfibSeq = getEven(fibSeq)

print(fibSeq)
print(evenfibSeq)

print(sum(evenfibSeq))
