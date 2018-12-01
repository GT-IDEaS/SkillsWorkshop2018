
#This script finds the sum of all multiples of 3 or 5 < 1000
sum=0         

def Check(subject):
	if subject%3==0 or subject%5==0:
		answer=True
	else:
		answer=False
	return answer

for i in range(1000):	
	will_add=Check(i)
	print(will_add)
	if will_add:
		sum+=i
print(sum)

