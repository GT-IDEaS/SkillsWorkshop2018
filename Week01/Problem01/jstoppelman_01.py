#!/usr/bin/env python

sum3=3
sum5=5
for i in range(6,1000,3):
    sum3 = i + sum3
for a in range(10,996,5):
    if not (a/3).is_integer():
        sum5 = a + sum5
sumtotal=sum3+sum5
print(sumtotal)
