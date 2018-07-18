
##answer:232792560

def factor(n):
    if n > 1: return n * factor(n - 1)
    elif n >= 0: return 1
    else: return -1


def isMultiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True


def Smallest_Multiple(n):
    for i in range(n, factor(n) + 1, n):
        if isMultiple(i, n):
            return i
    return -1


print (Smallest_Multiple(20))
