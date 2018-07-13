# Problem 5
# Smallest Multiple

# function for computing the greatest common divisor
def gcd(x,y):
    while y > 0:
        x,y = y,x%y
    return x

# function for computing the least common multiple
def lcm(x,y):
    return x*y//gcd(x,y)

# set number
NUM = 20

# find the smallest positive number that is  divisible by all of the numbers from 1 to 20
temp = 1
for i in range(2,NUM+1):
  temp = lcm(temp,i)

# print results
print(temp)
