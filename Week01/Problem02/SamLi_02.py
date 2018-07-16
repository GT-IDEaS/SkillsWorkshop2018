# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 01:28:10 2018

@author: Sam Li
"""

upperlimit = 4E6
Fibonacci_number1=1
Fibonacci_number2=2
sum_final = Fibonacci_number2
Fibonacci_number3 = 0
Fibonacci_number3=Fibonacci_number1+Fibonacci_number2
Fibonacci_count = 1
while Fibonacci_number3 <= upperlimit:
    if Fibonacci_count == 3:
        sum_final = sum_final + Fibonacci_number3 #this is the answer
        Fibonacci_count = 0
    Fibonacci_number1=Fibonacci_number2
    Fibonacci_number2=Fibonacci_number3
    Fibonacci_number3=Fibonacci_number1+Fibonacci_number2
    Fibonacci_count = Fibonacci_count+1
