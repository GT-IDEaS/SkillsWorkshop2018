termination = 4000000

previous = 1
current = 2

total = 2

while(True):
    new = current+ previous
    previous = current
    current = new
    if(current >= termination):
        break
    if(current % 2 == 0):
        total = total + current
    
print(total)    
    