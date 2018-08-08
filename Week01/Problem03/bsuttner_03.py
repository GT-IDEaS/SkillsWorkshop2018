# What is the largest prime factor of the number 600851475143 ?

n= 600851475143
factor = 2

while factor * factor < n:  #bc largest prime factor will never be > the sqrt of n
	while n % factor == 0:
		n = n/factor
	factor += 1
	
print(n)


