import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from scipy.optimize import curve_fit
from scipy.integrate import quad

def line(x,c,m):
    return m*x + c

def cubic(x,a0,a1,a2,a3):
    return a0 + a1*x + a2*x*x + a3*x*x*x

def bic(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B

x = np.array([ 1.,   1.5,  2.,   2.5,  3.,   3.5,  4.,   4.5,  5.,   5.5,  6.,
    6.5,  7.,   7.5, 8.,   8.5,  9.,   9.5, 10. ])
y = np.array([3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45,
    14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86])
dense_x = np.linspace(x[0],x[-1],int((x[-1]-x[0])/0.1) + 1)

# linear regression
slope, intercept, *t = linregress(x,y)
print("linear fit: ", slope, intercept, ", BIC = ", 
        bic(y,line(x, intercept, slope),2))

# cubic fit
params, params_covariance = curve_fit(cubic,x,y)
print("cubic fit: ",params, ", BIC = ", bic(y,cubic(x, *params),4))

# find area
area, err = quad(cubic, x[0], x[-1], args=tuple(params))
print("area under cubic fit: ", area)

# plot
fig, ax = plt.subplots()

ax.scatter(x,y, label="orig data")
ax.plot(x,line(x,intercept, slope), label="linear fit")
ax.plot(dense_x, cubic(dense_x, *params), label="cubic fit")
ax.text(6, 3, "Area = " + str(area))

ax.set_title("Data with linear and cubic fit")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

fig.savefig('ypang_01.png')
plt.show()
