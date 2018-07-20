import numpy

def factors(num):
    '''Check for the prime factors in the range of a chosen number '''
    #reusing the code from the previous lesson
    
    factors = []
    d  = 2
    
    multiple=1
    for i in range(1,num+1):
        multiple = multiple * i
        
    while multiple > 1:
        while multiple % d == 0: #Checking if d is a multiple of the initial number
            factors.append(d)
            multiple = multiple / d #This will keep factoring the number
        
        if d ==2:
            d = d + 1 #changing the factoring number
        else:
            d = d+2 # 2 is the only even prime number, so we can skip all the even factors
        
        if d*d > multiple > 1:  #we just have to check until the square root of a prime number to determine if it is prime or not
            factors.append(multiple)
            break
    
    return list(set(factors)) #returns a list of the prime numbers in the chosen range


def smallest_multiple(num):
    '''Returns the smallest positive number that is evenly divisible by all of the numbers from 1 to num'''
    
    primes = factors(num)    
    
    exponent =[]
    for i in primes:
        exp=1
        while i**exp <= num: #check for the highest exponent of each prime number inside the chosen number
            exp+=1
                        
            if i**exp> num:
                exponent.append(exp-1)
                
    multiples =[]
    for i in range(len(exponent)): #calculates the prime number elevated to its exponent
        numbers = (primes[i])**(exponent[i])
        multiples.append(numbers)
    
    return numpy.prod(multiples) #multiplies all the numbers in the list
                          
            
print smallest_multiple(20)