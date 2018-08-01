#sum of all multiples of 3 and 5 below 1000
#function for calculating the multiple of x up to the value y
def MultSum(x,y):
#x is used as a the multiplier, while the Mult variable is used to keeping
#track of the current multiple  
  Mult=x
  Sum=0
  while(Mult<y):
    Sum+=Mult
    Mult+=x 
  return Sum
#the result is the sums of two multiples are calculated separately and added 
#together minus the sum of multiple of 15, 5*3 which were counted twice
Result=MultSum(5,1000)+MultSum(3,1000)-MultSum(15,1000)
print(Result)
