def fibo(n):
    '''Calculates the nth term of the Fibonacci sequence'''
    fibonacci = [1,2] #first two terms of Fibonacci sequence
    if n<0:
        return None
        
    elif 0<=n<2:
        return 1
        
    else:
        while n > 2:
            i = fibonacci[-1]+fibonacci[-2] # Calculating the next term
            fibonacci.append(i) #Adding the calculated term
            n = n-1
        
        return fibonacci.pop() #returns the last calculated term

def soma():
    ''' return the sum of the even numbers of Fibonacci sequence that are smaller than 4000000'''
    numbers = []
    n=0
    while fibo(n)<4000000:
        if ((fibo(n))%2 ==0):
            numbers.append(fibo(n)) #it will add just the even numbers to the list
        n = n+1
    
    return sum(numbers) # it will sum the numbers in the list        