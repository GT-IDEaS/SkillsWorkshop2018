def fib(x):
	#x represents the the number of terms in fibonacci sequence
	fibseq = []
	for i in range(x):
		if i <= 1:
			fibseq.append(1)
		else:
			num = fibseq[i-1]+fibseq[i-2]	
			fibseq.append(num)	
	counter = 0 
	for n in fibseq:
		if n %2 == 0 and counter+n < 4000000:
			counter = counter + n
		if counter+n > 4000000:
			print("Number is too large!")
			x = 1 
			break	
	
	if x!= 1:
		print("Max sum of even valued terms of the fibonacci series is " + str(counter)+"!")	

			
			
#fib(32)
#fib(33)			
