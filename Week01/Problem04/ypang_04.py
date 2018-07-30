from numpy import sqrt 

def makePalindrome(x):
    x_str = str(x)
    ans = x_str + x_str[::-1]
    return int(ans)


""" MAIN """
test = 1000
factorFound = False

# largest possible = 99 * 99 = 9801 < 9889
# smallest possible = 1001
for i in range(test-3, test//10-1, -1):
    x = makePalindrome(i)

#find factors
    for j in range(test-1, int(sqrt(x)), -1):
        if(x%j == 0):
            fac1 = j
            fac2 = x//j
            factorFound = True
            break

    if(factorFound):
        break

print(x, "=", fac1, "x", fac2)


