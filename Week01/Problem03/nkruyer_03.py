# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 21:19:54 2018

@author: nkruyer3
"""

#Week 1 Assignment: Problem 3 - Nick Kruyer
#Correct anser 6857

n = 600851475143

#define function to determine if a number is prime
#if test = 1, number is not prime. If test = 0, number is prime
def prime(x):
    test = 0
    for i in range(2,x):
        if x%i == 0:
            test = 1
            break
    return test   

def factors(y):
    facts = [1,y]
    for i in range(2,y):
        if facts.count(i) > 0:
            break
        elif y%i == 0:
            facts.append(i)
            facts.append(y//i)
    return sorted(facts)

facts = factors(n);

for i in range(1,len(facts)):
    test = prime(facts[-i])
    if test == 0:
        print(facts[-i])
        break

            
        
        