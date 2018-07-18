def LCM(start,end):
    import numpy as np
    limit=np.linspace(start,end,end-start+1)
    tmp=np.linspace(start,end,end-start+1)
    while (tmp==min(tmp)).all()!= True:
        tmp[tmp==min(tmp)] = tmp[tmp==min(tmp)] +  limit[tmp==min(tmp)]
    return(tmp[0])

n1=LCM(1,10)
n2=LCM(11,15)
n3=LCM(16,20)

limit=np.array([n1,n2,n3])
tmp=np.array([n1,n2,n3])
while (tmp==min(tmp)).all()!= True:
    tmp[tmp==min(tmp)] = tmp[tmp==min(tmp)] +  limit[tmp==min(tmp)]
print(tmp[0])

# To speed up the computation, I divided the range of 1:20 to 3 sections
