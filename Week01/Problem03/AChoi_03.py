def prime():
	number = 600851475143
	list = []
	for i in range(2,number):
		while number%i == 0:
			number = number/i
			list.append(i)
		if number == 1:
			break	

	maxnum = max(list)		
	print(list)
	print("The maximum prime number is " + str(maxnum)+"!")
		

prime()
