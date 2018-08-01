#!/usr/bin/env python

def divis(x):
    for i in range(1,21):
        if x%i!=0:
            return False
        else:
            if i==20:
                return True
product=1
for i in range(1,21):
    product=i*product
print(product)
for i in range(21,product):
    if divis(i):
        print(i)
        break
