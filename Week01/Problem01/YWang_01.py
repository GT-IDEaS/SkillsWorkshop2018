# Problem 1
# Multiples of 3 and 5

# set upper limit
lim_UB = 1000

# initialize save space
multi_List = list()

# find all the multiples of 3 or 5 below lim_UB
for i in range(1,lim_UB):
    if i%3 == 0 or i%5 == 0:
        multi_List.append(i)

# print results
print(sum(multi_List))
