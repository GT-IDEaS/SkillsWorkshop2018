#gwang_04.py
def palindrome(num):
    return str(num) == str(num)[::-1]
min = 100
max = 999
NN = min * min
MM = max * max
for i in range(MM,NN,-1):
    if palindrome(i):
        for j in range (max,min,-1):
            o = i/j
            m = int(o)
            if m == o and min < m and m < max:
                print (m, " *  ", j, " = ", i )
                break
        else:
            continue
        break