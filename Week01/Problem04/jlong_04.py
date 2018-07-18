import math

##answer:906609

def is_palindrome(num):
    return str(num) == str(num)[::-1]


def Largest_Palindrome_Product(digit):
    palindrome = -1

    x = digit-1
    i_left=0
    i_right=0
    while x>=0:
        i_left += int(math.pow(10,x)) * 9
        if x < digit-1:
            i_right += int(math.pow(10,x)) * 9
        x -= 1

    for i in range (i_left, i_right, -1):
        for j in range (i, i_right, -1):

            if is_palindrome(i * j) and i * j > palindrome:
                palindrome = i * j

    return palindrome;

digit_number=3
print (Largest_Palindrome_Product(digit_number))
