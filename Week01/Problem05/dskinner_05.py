import numpy as np

max = range(2520, 10000000000, 2520)
div = np.arange(1, 21)
for i in max:
    sam = i/div
    if all(item.is_integer() == True for item in sam) == False:
        #print('nope ' + str(sam))
        continue
    elif all(item.is_integer() == True for item in sam) == True:
        print('this is the one ' + str(i))
        break