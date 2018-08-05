import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

frame=pd.read_csv("data/bouldercreek_09_2013.txt",sep='\t')
print(frame)
newframe=frame[['datetime','04_00060']]
newframe.columns=['time','stream']
newframe=newframe.iloc[1:]
print(newframe)
x,k=newframe.shape
newframe.sort_values(by=['stream'])
x=range(x)
y=newframe['stream']
plt.plot(x,y)
plt.ylim(0,500)
plt.yticks(range(0,400,50))
plt.subplots()
plt.savefig("plotname.png")
