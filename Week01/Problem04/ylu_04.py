answer = 0

for a in range(100,1000):
	for b in range(100,a):#This step makes a and b become different numbers.
		m = a * b
		n = str(m)
		# answer (int.) could not comare with n(str). So we need to define m first.
		if n == n[::-1]: #n == n[::-1] means n is a palindromic number
			if answer < m:
				answer = m
				
print (answer)