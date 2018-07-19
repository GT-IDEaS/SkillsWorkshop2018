def max_factors(num):
    '''Check for the largest prime factor of a number '''
    
    factors = []
    d  = 2
    
    while num > 1:
        while num % d == 0: #Checking if d is a multiple of the initial number
            factors.append(d)
            num = num / d #This will keep factoring the number
        
        if d ==2:
            d = d + 1 #changing the factoring number
        else:
            d = d+2 # 2 is the only even prime number, so we can skip all the even factors
        
        if d*d > num > 1:  #we just have to check until the square root of a prime number to determine if it is prime or not
            factors.append(num)
            break
    return factors.pop()

    
print max_factors(6*11-1)