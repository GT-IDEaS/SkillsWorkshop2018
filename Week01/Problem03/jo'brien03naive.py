print(1)

def is_prime(n):
        for i in range(0):
                if n%i==0:
                        return False
        return True

print(2)

factors=[]

print(3)

for i in range(600851475143):
	print(4)
	print(i)
	if 600851475143%i==0:
		if is_prime(i):
			factors.append(i)

print(factors)
print(max(factors))

