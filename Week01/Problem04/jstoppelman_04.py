#!/usr/bin/env python

palindrome=0
for i in range(100, 1000,1):
    for a in range(i, 1000,1):
        product=i*a
        if product>palindrome:
            p=str(product)
            if p == p[::-1]:
                palindrome=i*a
print(palindrome)
