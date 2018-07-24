variable1 = 1
variable2 = 1
sum = 0
while variable1 <= 4000000:
    if variable1 % 2 == 0:
        sum += variable1
    variable1, variable2 = variable2, variable1+variable2  
print (sum)