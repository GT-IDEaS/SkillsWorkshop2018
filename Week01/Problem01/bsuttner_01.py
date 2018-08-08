#! /usr/bin/env python3

#Sum the multiples of 3 or 5 that are below 1000. The range function does not include the last number, so only goes up to 999
# "%" is the modulus/remainder operator, if the remainder of a Number between 0 and 999 divided by 3 or 5 is equal to 0, then sum it. 	
print(sum(i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0))