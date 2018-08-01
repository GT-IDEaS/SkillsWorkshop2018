#!/usr/bin/env python

def seeifprime(i):
    for x in range(2,int(1+i/2)):
        if i%x==0:
            return False
    return True
num=600851475143
a=2
prime=[]
for i in range(a,int((num)**(0.5))):
    if num%i==0:
        if seeifprime(i):
            print(i)
        

