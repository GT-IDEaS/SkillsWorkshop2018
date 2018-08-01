# Week 02 Assignment: Fitting and Plotting
# Fit a linear curve to the data
# Fit a cubic curve using the SciPy library
# Find the area underneath the cubic curve over the domain of the data using the tools in SciPy
# Plot the data, the linear fit, and the cubic fit in Matplotlib. Make sure to give the plot a title and an x and y label. Save this figure and include it in your pull request!
# Put the area of the curve on the plot somewhere as text using Matplotlib
# Use the Bayesian information criterion to justify which model (linear or cubic) is preferable. Include this justification in your journal entry for the week.

# import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.integrate import simps
from matplotlib.patches import Polygon


# input data
x = np.array([ 1.,1.5,2.,2.5,3.,3.5,4.,4.5,5.,5.5,6.,6.5,7.,7.5,8.,8.5,9.,9.5,10.])
y = np.array([3.43,4.94,6.45,9.22,6.32,6.11,4.63,8.95,7.8,8.35,11.45,14.71,11.97,12.46,17.42,17.0,15.45,19.15,20.86])


# 1 Fit a linear curve to the data
slope, intercept, r_value, p_value, std_err = linregress(x,y)


# 2 Fit a cubic curve using the SciPy library
coefficients = np.polyfit(x,y,3)
p = np.poly1d(coefficients)


# 3 Find the area underneath the cubic curve over the domain of the data using the tools in SciPy
t = np.linspace(min(x),max(x),num=100)
area = simps(p(t),t)
print("area =",area)


# 4 Plot the data, the linear fit, and the cubic fit in Matplotlib
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting');
# plot data
plt.scatter(x,y,c='k',label='Data')
# plot linear fit
plt.plot(x,x*slope+intercept,'--r',label='Linear Fit')
# plot cubic fit
plt.plot(t,p(t),'-b',label='Cubic Fit')
plt.legend()
# save figure
plt.savefig('YWang_02.png')


# 5 Put the area of the curve on the plot somewhere as text using Matplotlib
fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting');
# plot data
plt.scatter(x,y,c='k',label='Data')
# plot linear fit
plt.plot(x,x*slope+intercept,'--r',label='Linear Fit')
# plot cubic fit
plt.plot(t,p(t),'-b',label='Cubic Fit')
plt.legend()
# plot area under cubic curve
verts = [(min(x), 0)] + list(zip(t, p(t))) + [(max(x), 0)]
poly = Polygon(verts,facecolor='0.9',edgecolor='0.5',alpha=0.5)
ax.add_patch(poly)
# insert text
plt.text(0.5 * (min(x) + max(x)), 5, r"Shaded Area",
         horizontalalignment='left', fontsize=20)
# save figure
plt.savefig('YWang_02.png')

# 6 Use the Bayesian information criterion to justify which model (linear or cubic) is preferable

# define function for Bayesian information criterion
def BIC(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B

# calculate BIC for linear fit
BIC_Linear = BIC(y,x*slope+intercept,1)
# calculate BIC for cubic fit
BIC_Cubic = BIC(y,p(x),3)
