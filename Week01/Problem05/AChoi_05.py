def smallestMult():
	num = 1
	List = [1]
	for i in range(2,21):
		for item in List:
			#print(item)
			if i%item == 0: 
				i = i/item
		List.append(i)
	for item in List:
		num = num*item
	num = int(num)
	#print(List)
	print(num)		
			



smallestMult()	
