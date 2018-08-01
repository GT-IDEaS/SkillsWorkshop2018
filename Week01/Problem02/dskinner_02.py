import numpy as np

#
#Here is a general solution to the even fibonacci numbers problem. Only input needed is the max value:
#
def even(max_val):
    fib = [1, 2]
    val = 0
    while np.max(fib) < max_val:
        next_val = fib[-1] + fib[-2]
        if next_val < max_val:
            fib.append(fib[-1] + fib[-2])
        else:
            break
    val = 0
    for i in fib:
        if (i/2).is_integer():
            val += i
    return 'The sum of the even-valued terms in the Fibonnaci sequence up to ' + str(max_val) +  ' is '+ str(val)

#
# Alternatively, here is the direct solution which will print upon typing `python dskinner_02.py`
#
fib = [1, 2]
while np.max(fib) < 4000000:
    next_val = fib[-1] + fib[-2]
    if next_val < 4000000:
        fib.append(fib[-1] + fib[-2])
    else:
        break

val = 0
for i in fib:
    if (i/2).is_integer():
        val += i
print('The sum of the even-valued terms in the Fibonnaci sequence up to 4,000,000 is '+ str(val))