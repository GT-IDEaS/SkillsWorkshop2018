"""Start with a number that is a product of all numbers from 2 and 20
and gradually decrease it to fine the smallest one"""
Prod=1
for i in range(2,20):
  Prod=Prod*i
def CheckMult(x):
   """Checks is the present product is still dividable by all numbers in 
the list"""
   for h in range(2,20):
      if x%h!=0:
        return False
        break
   return True  
for k in range(2,20):
    """Divides products by each number in the list while it can"""
    while CheckMult(Prod//k)==True:
       Prod=Prod//k
print(Prod) 

