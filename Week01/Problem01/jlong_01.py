import numpy as np


###answer:233168


def  Multiples_of_3_and_5(up_limit):
    x=0
    multiples_sum=0
    while x<up_limit:
        if x % 3 == 0 or x % 5 == 0:
                multiples_sum += x
        x+=1
    return(multiples_sum)

up_limit = 1000
print(Multiples_of_3_and_5(up_limit))
