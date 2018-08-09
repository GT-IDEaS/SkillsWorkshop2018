# -*- coding: utf-8 -*-
"""
uses the x, y data below to complete the tasks in parts 1-6 below.

1. Fit a linear curve to the data
2. Fit a cubic curve using the SciPy library
3. Find the area underneath the cubic curve over the domain of the data using the tools in SciPy
4. Plot the data, the linear fit, and the cubic fit in Matplotlib. Make sure to give the plot a title and an x and y label. Save this figure.
5. Put the area of the curve on the plot somewhere as text using Matplotlib
6. Use the Bayesian information criterion to justify which model (linear or cubic) is preferable. Include this justification in your journal entry for the week.


Created on Mon Jul 23 16:54:15 2018

@author: Sam Li
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def BIC(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B

x = [ 1.,   1.5,  2.,   2.5,  3.,   3.5,  4.,   4.5,  5.,   5.5,  6.,   6.5,  7.,   7.5, 8.,   8.5,  9.,   9.5, 10. ]
y = [3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45, 14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86]

plt.figure()
plt.scatter(x, y)

coefficients_lin = np.polyfit(x, y, 1)
y_lin = np.poly1d(coefficients_lin)

coefficients_cubic = np.polyfit(x, y, 3)
y_cubic = np.poly1d(coefficients_cubic)

area = quad(y_cubic, np.min(x), np.max(x))

plt.plot(x, y_lin(x), 'r-', label='Linear')
plt.plot(x, y_cubic(x), 'g-', label='Cubic, Area = ' + str(area[0]))
plt.fill_between(x, y_cubic(x), alpha='0.2', color='green')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Linear and Cubic Fit')
plt.savefig('SamLi_01.png')

lin_bic = BIC(y,y_lin(x),2)
cub_bic = BIC(y, y_cubic(x), 4)
print('Linear BIC = ', lin_bic)
print('Cubic BIC = ', cub_bic)
