def CheckDivisibility(number, maxDivisor):
    for n in range(1, maxDivisor+1):
        if (number % n != 0):
            return False
        
    return True

i = 20
while(not CheckDivisibility(i, 20)):
    i += 20
    
print(i)
    