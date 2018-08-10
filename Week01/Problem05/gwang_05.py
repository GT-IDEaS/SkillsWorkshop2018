#gwang_05.py
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
m = 20
j = 1
for i in range(1,m):
    j *= int(i/gcd(j,i))
print(j)