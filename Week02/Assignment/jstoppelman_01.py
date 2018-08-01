#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
from scipy.optimize import curve_fit

def curve3(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d
def BIC(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B
x = [ 1.,   1.5,  2.,   2.5,  3.,   3.5,  4.,   4.5,  5.,   5.5,  6.,   6.5,  7.,   7.5, 8.,   8.5,  9.,   9.5, 10. ]
y = [3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45, 14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86]

x=np.asarray(x)
y=np.asarray(y)
coeff=np.polyfit(x,y,1)
t=np.poly1d(coeff)
params, covar = curve_fit(curve3,x,y)
y3=np.asarray(curve3(x,*params))
bt3=BIC(y, y3,3)
print(bt3)
bt=BIC(y,t(x),1)
print(bt)

#print("area=", simps(t3(x),x))

plt.scatter(x,y)
plt.plot(x,t(x),'-')
plt.plot(x,curve3(x,*params),'-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Week 2 Plot')
plt.text(6,5,"area={}".format(simps(curve3(x,*params)),x))
plt.savefig("jstoppelman_01.png")

