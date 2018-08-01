## Description
## Finds the sum of all multiples of 3 or 5 bellow 1000

## Weekly Journal
## Use of the "%" operator 

## Questions
## None

vector=list(range(1,1000))
multiples=[]
for number in vector:
    if number % 3 == 0 or number % 5 == 0:
        multiples.append(number)
result=sum(multiples)
print(result)
