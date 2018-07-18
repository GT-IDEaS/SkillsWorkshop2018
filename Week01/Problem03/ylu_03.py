n = 600851475143
answer = 2

while n > answer:
    if n % answer == 0:
        while n % answer == 0:
            n = n / answer
    #divide all of the same factor, so the next factor found by this loop will still be a prime number
    #python doesn't need to type 'else' & 'end'
	answer = answer + 1
	

print(answer)