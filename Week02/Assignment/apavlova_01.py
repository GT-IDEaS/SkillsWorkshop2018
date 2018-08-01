import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy
from  scipy.stats import linregress as lin 
from scipy.optimize import curve_fit as fit
from scipy.integrate import quad
x = [ 1.,   1.5,  2.,   2.5,  3.,   3.5,  4.,   4.5,  5.,   5.5,  6.,   6.5,  7.,   7.5, 8.,   8.5,  9.,   9.5, 10. ]
y = [3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45, 14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86]
"""Linera regression"""
slope, intercept, r_value, p_value, std_err = lin(x,y)
"""apparently a float conversion is needed to avoid numpy errors"""
x=np.float64(x)
LinFit=x*slope+intercept
"""Cube fitting"""
def CubeFun(x,a,b,c,d):
   return a*(x**3)+b*(x**2)+c*x+d
params, params_covariance=fit(CubeFun,x,y)
CubeFit=CubeFun(x,*params)
"""integration"""
A=quad(lambda x:CubeFun(x,*params),min(x),max(x))
"""BIC calculation"""
def BIC(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B
LineError=BIC(y,LinFit,2)
CubeError=BIC(y,CubeFit,4)
LineError=round(LineError,2)
CubeError=round(CubeError,2)
   
"""plotting of data"""
Fig=plt.figure()

axes = Fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
plt.xticks(np.arange(int(min(x)-2), int(max(x)+2), 2))
plt.yticks(np.arange(int(min(y))-3, int(max(y))+3, 3))

plt.scatter(x,y,color='black',label='Data points')
"""Plotting of linear fit"""
plt.plot(x,LinFit,'r',label='Linear fit, BIC=%s'%(LineError))
plt.plot(x,CubeFit,'g',label='Cubic fit, BIC=%s'%(CubeError))
Area=A[0]
Area=round(Area,2)
plt.text(5,19,'Area=%s'%(Area))
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Fitting of data')
plt.legend()
Fig.savefig('DataPlot.pdf')
