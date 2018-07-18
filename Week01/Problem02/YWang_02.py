# Problem 2
# Even Fibonacci Numbers

# set upper limit
lim_UB = 4000000

# initialize save space
fib_List = list()

# find all even Fibonacci numbers
OLD = 0 # first Fibonacci number
NEW = 1 # second Fibonacci number
while NEW < lim_UB:
    if NEW%2 == 0:
        # add even Fibonacci number into list
        fib_List.append(NEW)
    # generate the next Fibonacci number
    TMP = OLD + NEW
    OLD = NEW
    NEW = TMP

# print results
print(sum(fib_List))
