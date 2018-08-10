#gwang_03.py
PF = 600851475143
m = int(PF**(1/2.0))
k = 1
for i in range(m,1,-1):
	if (PF % i) == 0:
		n = int(i**(1/2.0))
	    for j in range(2,n+1):
	        if i % j == 0:
				break
		else:
			k = i
	if k > 1:
		break
print(k)