fibonacci=[1,2]
k=2
flag=True
while flag:
  if (fibonacci[k-1]+fibonacci[k-2])<4e6:
    fibonacci.append(fibonacci[k-1]+fibonacci[k-2])
    k +=1
  else:
    flag=False
#print(fibonacci)
sum = 0
for i in range(len(fibonacci)):
  if fibonacci[i]%2==0:
    sum += fibonacci[i]
print(sum)
