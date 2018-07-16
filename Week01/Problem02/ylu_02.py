a = 1
b = 1
evensum = 0

while b < 4000000:
	if b % 2 == 0:
		evensum += b
	a, b = b, a+b
	# definition of Fibonacci numbers
	
print (evensum)