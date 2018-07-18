
def is_prime(n):
	for i in range(0):
		if n%i==0:
			return False
	return True

fini=False
i=2
mynum=600851475143
factors = []

while(mynum!=1):
	if is_prime(i):
		if mynum%i==0:
			factors.append(i)
		while(mynum%i==0):
			mynum/=i
	print(mynum)
	print(i)
	i+=1

print("The prime factors of 600851475143 are: ", factors)
print("The greatest prime factor of 600851475143 is ", max(factors))
