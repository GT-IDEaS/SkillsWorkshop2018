# import packages
import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import linregress
from scipy.integrate import simps
#from matplotlib.patches import Polygon

# input data
x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5,9, 9.5, 10])
y = np.array([3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45, 14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86])

# 1: fit linear
l_co = np.polyfit(x, y, 1)
l_fit = np.poly1d(l_co)

# 2: fit cubic
c_co = np.polyfit(x, y, 3)
c_fit = np.poly1d(c_co)

# 3: Find the area underneath the cubic curve
t = np.linspace(1, 10, 200)
area = simps(c_fit(t),t)
print("Area under cubic line = ",area)

# 4 & 5: Plot the data, the linear fit, and the cubic fit; Put the area on the plot

plt.scatter(x,y, label = 'Data')
plt.plot(x,l_fit(x),'r', label = 'Linear Fit')
plt.plot(t,c_fit(t),'g', label = 'Cubic Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting the data')
plt.legend()
plt.text(0.8,16,'Area under cubic line = '+str(area))
plt.savefig('ylu_data_fitting.pdf')

# 6: Justify preferable model (linear or cubic) by BIC
def BIC(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B
linear = BIC(y,l_fit(x),len(l_co)) # k = number of coefficients
cubic = BIC(y,c_fit(x),len(c_co))
print('BIC(linear):',linear)
print('BIC(cubic):',cubic)
if linear <= cubic:
    print('linear model is preferable')
else:
    print('cubic model is preferable')    