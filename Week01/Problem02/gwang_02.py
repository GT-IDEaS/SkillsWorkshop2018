#gwang_02.py
UL = 4000000
m = 1
n = 2
p = m + n
r = n
while p < UL:
	m = n
	n = p
	p = m + n
	if p % 2 == 0:
		r += p
print(r)