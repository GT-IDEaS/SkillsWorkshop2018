#this is very brute force but I cant come up with something better
#assume only 6 figure numbers, determines if it is a palindrome
def PalCheck(x):
   NumStr=str(x)
   if NumStr[0]==NumStr[-1] and NumStr[1]==NumStr[-2] and NumStr[2]==NumStr[-3]:     return True
   else:
     return False
#compares 2 numbers returns the largest one
def Max(num1,num2):
   if num1 > num2:
      return num1
   else:
      return num2
ProdOld=0
#Loops over all 3 digit numbers, checks if it is a palindrom, uses Max function #to track  the largest palindrome
for a in range(100,999):
  for b in range(100,999):
    ProdNew=a*b
    if PalCheck(ProdNew)==True:
       ProdOld=Max(ProdOld,ProdNew)
print(ProdOld)

   
