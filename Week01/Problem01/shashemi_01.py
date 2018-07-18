sum = 0
limit = 1000
for i in range(1,limit):
  if i%3==0 or i%5==0:
    #print(i)
    sum += i
print(sum)
