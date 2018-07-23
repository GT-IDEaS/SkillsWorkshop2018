# INIT
num1 = 1
num2 = 2
even1 = False
even2 = True

mysum = 2
newnum = num1 + num2
neweven = even1 == even2  #even + even = even, odd + odd = even, else odd


# RUN
while(newnum < 4000000):
    print(newnum, "(is even?", neweven, ")")

    if(neweven):
        mysum += newnum

# iteract
    num1 = num2
    num2 = newnum
    even1 = even2
    even2 = neweven

    newnum = num1 + num2
    neweven = even1 == even2  #even + even = even, odd + odd = even, else odd



print("\n\nSUM = ",mysum)
