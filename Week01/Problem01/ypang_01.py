maxnum = 1000

threemul = set(range(3, maxnum, 3))
fivemul  = set(range(5, maxnum, 5))

muls = threemul | fivemul
print(muls)
print("sum = ", sum(muls))
