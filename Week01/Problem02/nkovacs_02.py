def fib(max_value=100):
	fib_seq = [1]
	new_term = 2
	while new_term <= max_value:
		fib_seq.append(new_term)
		new_term += fib_seq[-2]

	return(fib_seq)

def sum_evens(num_list):
	ans = 0
	for x in num_list:
		if x % 2 == 0:
			ans += x
	return(ans)

print(sum_evens(fib(4000000)))