import numpy as np


##answer:4613732 

def  Even_Fibonacci_Numbers(n):
    x1 = 0
    x2 = 1
    fibonacci_sum=x1
    x3 = x1 + x2
    while x3<n:
        x3 = x1 + x2
        if x3 % 2== 0 :
            fibonacci_sum += x3
        x1 = x2
        x2 = x3
    return(fibonacci_sum)

n=4000000
print(Even_Fibonacci_Numbers(n))
