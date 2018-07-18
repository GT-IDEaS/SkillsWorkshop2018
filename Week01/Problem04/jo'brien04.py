imdone=False
for i in range(999):
	a=int(str(999-i)+str(999-i)[::-1])
	for k in range(1,999):
		if a%k == 0:
			if a/k < 1000:
				print("a is ", a)
				print("k is ", k)
				print("a/k is ", a/k)
				imdone=True
		if imdone:
			break
	if imdone:
		break
