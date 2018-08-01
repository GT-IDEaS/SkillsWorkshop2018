def multiples():
    ''' Find the sum of all the multiples of 3 or 5 below 1000.'''
    
    numbers = []
    for i in xrange(1000):
        if ((i%3) ==0) or ((i%5) ==0): #if the rest of the division between the number and 3 or 5 is 0, then the number is a multiple of either 3 or 5 
            numbers.append(i) # add the number to a list
        
    return sum(numbers) #sum the content of the list
