def palindrome():
    '''Finds the largest palindrome made from the product of two 3-digit numbers'''
    palindromes = []
    for i in [a*b for a in xrange(999,100,-1) for b in xrange(999,100,-1)]: #creates all the combinations for 3-digits numbers
        if is_palindrome(i) == True:
            palindromes.append(i)
    
    return max(palindromes)
        

def is_palindrome(num):
    ''' Checks if a number is a palindrome'''
    num_string = str(num) #transforms a number into a string
    rev = num_string[::-1] #reverses that string
    
    if num_string == rev: #compares both strings
        return True

print palindrome()