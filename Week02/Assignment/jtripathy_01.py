
# coding: utf-8

# In[35]:


import numpy as np
import matplotlib  
import matplotlib.pyplot as plt 
from IPython.display import Image 
from numpy import trapz
from scipy.integrate import simps
import scipy, pylab


x = np.array([ 1.,   1.5,  2.,   2.5,  3.,   3.5,  4.,   4.5,  5.,   5.5,  6.,   6.5,  7.,   7.5, 8.,   8.5,  9.,   9.5, 10. ])
y = np.array([3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45, 14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86])
# y = y.astype('float64')
plt.subplot(2,1,1)
plt.scatter(x,y)
fit_1 = np.polyfit(x,y,1)
fit_lin = np.poly1d(fit_1) 
plt.plot(x, fit_lin(x),'g', label="Linear_fit")
# plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('x-y curve with Linear and Cubic Fits')
plt.legend()
# Compute the area using the composite trapezoidal rule.
area_t = trapz(y, dx=0.5)
print("area_t =", area_t);
plt.text(5, 5, 'area_t='+  "%f" %area_t)
plt.legend()
# plt.show()  by executing the step to "show the plot" here, the subplotting gets undone. 
# it requires both the parts to be plotted once at the very end.



plt.subplots_adjust(hspace=.5)
plt.subplot(2,1,2)
plt.scatter(x,y)
fit_3 = np.polyfit(x,y,3)
fit_cubic = np.poly1d(fit_3)
plt.plot(x,fit_cubic(x),'r',label="Cubic_fit")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#plt.title('x-y curve with Cubic Fit')

# Compute the area using the composite Simpson's rule.
area_s = simps(y, dx=0.5)
print("area_s =", area_s);
##
plt.text(5, 5, 'area_s=' +  str(area_s)) # using "%f" % automatically considers the string type.
plt.legend()
plt.show()


# plt.subplot(2,1,1)
plt.plot(x,y, 'b*')
fit_1 = np.polyfit(x,y,1)
fit_lin = np.poly1d(fit_1) 
plt.plot(x, fit_lin(x),'g', label="Linear_fit")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('x-y Curve with Linear and Cubic Fits')
plt.legend()
fit_3 = np.polyfit(x,y,3)
fit_cubic = np.poly1d(fit_3)
plt.plot(x,fit_cubic(x),'r',label="Cubic_fit")
plt.text(5, 5, 'area_s=' +  str(area_s))
plt.text(5, 3, 'area_t=' +  str(area_t))
plt.legend()
plt.show()

def BIC(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B

h_Linear = BIC(y,fit_lin(x),2) # for 1st order there are two coefficients
print("h_Linear=",h_Linear)

h_Cubic = BIC(y,fit_cubic(x),4) # 4 coefiicients for order 3
print("h_Cubic=",h_Cubic)

err = []
poly_range = range(1,10)
for i in poly_range:
    coefficients = np.polyfit(x, y, i)
    p = np.poly1d(coefficients)
    err.append(BIC(y,p(x),i))

plt.plot(range(1,10),err)
plt.ylabel('BIC')
plt.xlabel('polynomial order')

plt.show()

