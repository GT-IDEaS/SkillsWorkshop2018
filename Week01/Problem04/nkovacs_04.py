prod = []
for x in range(100,1000):
	for y in range(100,1000):
		prod.append(x*y)

prod.sort()

for p in prod[::-1]:
	if str(p) == str(p)[::-1]:
		print(p)
		break