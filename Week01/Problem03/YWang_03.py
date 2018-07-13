# Problem 3
# Largest Prime Factor

# set number
NUM = 600851475143

# find largest prime factor
i = 2
while i*i < NUM:
  while NUM%i == 0:
    NUM = NUM // i
  i = i + 1

# print results
print(NUM)
