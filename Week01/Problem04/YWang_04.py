# Problem 4
# Palindrome Product

# function for testing palindrome
def isPalindrome(n):
  # convert number to string
  num2str = str(n)
  # init an empty string
  reverseStr = ""
  # reserse input string
  for i in range(len(num2str)-1,-1,-1):
    reverseStr += num2str[i]
  return num2str == reverseStr


# function for finding the largest palindrome
def find_lagest_Palindrome():
  temp = 0
  # find the largest palindrome made from the product of two 3-digit numbers
  for x in range(999,99,-1):
    for y in range(x,99,-1):
      if isPalindrome(x*y) and x*y>temp:
        temp = x*y
  return temp
  

# print results
print(find_lagest_Palindrome())
