import numpy as np

#
# Here is a solution to the general problem for multiples of 2 numbers (a, b) below a certain value. This can be imported to another script:
#
def multiples(a, b, value):
    arr = np.arange(value)
    num = []
    for i in arr:
        if (((i/a).is_integer()) == True) or (((i/b).is_integer()) == True):
            num.append(int(i))
        else:
            continue
    return 'The sum of all the multiples of ' + str(a) + ' and ' + str(b) + ' is ' + str(np.sum(num)) +'!'

#
# Alternatively, here is the direct solution which will print upon typing `python dskinner_01.py`
#
a = 3
b = 5
arr = np.arange(1000)
num = []
for i in arr:
    if (((i/a).is_integer()) == True) or (((i/b).is_integer()) == True):
        num.append(int(i))
    else:
        continue
print('The sum of all the multiples of ' + str(a) + ' and ' + str(b) + ' is ' + str(np.sum(num)) +'!')