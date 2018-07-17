
def four_million_fibs():
	odd_1 = 1
	evenn = 2
	odd_2 = 3
	run_bool = True
	sum = 2
	print(run_bool)
	while run_bool:
		print('running')
		odd_1 = evenn + odd_2
		evenn = odd_1 + odd_2
		odd_2 = odd_1 + evenn
		if (evenn < 4000000):
			sum+=evenn
			print(sum)
		else:
			run_bool = False
			print("sum is ", sum)
			return sum
			
four_million_fibs()

