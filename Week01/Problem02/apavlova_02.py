#Fib1 is the lower fibonacci number and Fib2 is the higher one
Fib1=1
Fib2=2

Sum=0
#Sum is updated untill the higher number reaches 4000000
while Fib2<4000000:
    if Fib2%2==0:
       Sum+=Fib2
#FibNew is used for calculating the new number in the series
    FibNew=Fib2+Fib1
#and the last 2 numbers in the series are updated
    Fib1=Fib2
    Fib2=FibNew
print(Sum)

