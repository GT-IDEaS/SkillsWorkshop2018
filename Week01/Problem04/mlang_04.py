
def isPalindrome(number):
    string = str(number)
    length = len(string)
    for index in range(0,length//2):
        if(string[index] != string[-(index + 1)]):
            return False
    return True
      
limit = 1000
biggest = 0
for n in range(1,limit):
    for k in range(1,limit):
        temp = n*k
        if (isPalindrome(temp)):
            if(temp > biggest):
                biggest = temp
                
print(biggest)