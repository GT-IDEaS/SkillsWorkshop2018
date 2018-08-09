answer = []
y = 1
x = 232711111
while y < 20:
    if x % y == 0:
        y+=1
    else:
        x +=1
        y = 1
if y == 20:
    if x % y == 0:
        answer.append(x)
        
print (answer[-1])