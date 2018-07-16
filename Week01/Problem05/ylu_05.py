
def gcd (a ,b): #define "Greatest common divisor"
	if a<b:
		a,b=b,a
	while a%b !=0:
		a,b = b,a%b
	return b

# gcd could also be express as: "gcd = lambda a, b: (gcd(b, a % b) if a % b else b)"
# from Wikipedia	

answer = 1
for n in range(1,21):	
	m = gcd(n,answer)
	answer = answer*n/m #Least common multiple = multiple divided by GCD

print(answer)



