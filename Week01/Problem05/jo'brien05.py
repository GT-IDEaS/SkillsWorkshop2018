
potential_factors = []
mult=1

for i in range(1,21):
	potential_factors.append(i)

good_factors=potential_factors
print(potential_factors)

for i in range(2,19):
	for j in range(1,potential_factors[19-i]-2):
		if potential_factors[19-i]%j==0:
			good_factors[j-1]=1

print(good_factors)
	

