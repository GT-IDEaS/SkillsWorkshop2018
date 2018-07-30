import numpy as np

#
#Here is a general solution to the largest palindrome problem. The input is two arrays with the range of values we want to find the largest palindrome for:
#For our example, x = [100, 999], y = [100, 999]
#
def large_palin(x, y):
    pals = []
    z = np.arange(x[0], x[1] + 1)
    t = np.arange(y[0], y[1] + 1)
    for i in z:
        for j in t:
            a = str(i*j)
            if a == a[::-1]:
                pals.append(int(a))
    return 'The largest palindromic number is ' + str(np.max(pals))

#
# Alternatively, here is the direct solution which will print upon typing `python dskinner_04.py`
#
z = np.arange(100, 999 + 1)
t = np.arange(100, 999 + 1)
pals = []
for i in z:
    for j in t:
        a = str(i*j)
        if a == a[::-1]:
            pals.append(int(a))
print('The largest palindromic number is ' + str(np.max(pals)))