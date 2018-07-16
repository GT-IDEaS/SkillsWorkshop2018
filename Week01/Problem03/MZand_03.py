# finding the largest prime factor of a number


num=600851475143

i=2

while i^2<num:
      while num % i ==0 :
            num=num/i 
            
      i=i+1 
    
print('The largest prime factor is {}'.format(num))
