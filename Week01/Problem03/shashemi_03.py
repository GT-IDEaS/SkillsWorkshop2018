num=600851475143
prime=[]

for i in range(2,int(num/2)+1):
    while num%i==0:
      prime.append(i)
      num /= i
    if num==1:
          break
    if prime==[]:
        prime.append(num)

print(max(prime))
