def factors(n):
	output = []
	f = 2
	while f * f <= n:
		if n % f == 0:
			output.append(f)
			n = n / f
		else:
			f = f + 1
	output.append(int(n))
	return(output)

print(factors(600851475143)[-1])