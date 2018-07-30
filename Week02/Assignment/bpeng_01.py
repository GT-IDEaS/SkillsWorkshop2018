#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:04:18 2018

@author: baijiepeng
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import scipy as sp
from scipy.integrate import simps

np.random.seed(1)

x = [ 1.,   1.5,  2.,   2.5,  3.,   3.5,  4.,   4.5,  5.,   5.5,  6.,   6.5,  7.,   7.5, 8.,   8.5,  9.,   9.5, 10. ]
y = [3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45, 14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86]
color = np.random.rand(len(x),3)
x = np.float64(x)
y = np.float64(y)


slope, intercept, r_value, p_value, std_err = linregress(x,y)

parameter = sp.polyfit(x,y,3)
plt.scatter(x,y,c=color)
plt.plot(x,x*slope+intercept, c = "black")
plt.plot(x,parameter[0]*x**3+parameter[1]*x**2+parameter[2]*x+parameter[3], c ='red')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('title')
plt.legend(['linear fit','cubic fit','orignal data'],loc = 4)

plt.text(x[4], y[1], 
         r'$y =%s{x}+%s$'%(round(slope,2),round(intercept,2))
,color='black', fontsize=14)
plt.text(x[0], 18,
         r'$y =%s{x}^3+%s{x}^2+%s{x}+%s$'%(round(parameter[0],4),round(parameter[1],2),round(parameter[2],2),round(parameter[3],2),)
         ,color='red', fontsize=14)

x_simps = np.linspace(x[0],x[-1],1000)
y_simps = np.poly1d(parameter)
area = simps(y_simps(x_simps),dx = 0.01)
print (area)
plt.text(6.5,9,'Area under curve \n is %s'%round(area,2), color = "red", fontsize = 14)

## Bayesian infomation criterion

def BIC(y, y_hat, k, weight = 1):
    err = y - y_hat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B

err = []
poly_range = range(1,100)
for i in poly_range:
    coefficients = sp.polyfit(x, y, i)
    p = np.poly1d(coefficients)
    err.append(BIC(y,p(x),i))
plt.figure()
plt.plot(range(1,100),err)
plt.ylabel('BIC')
plt.xlabel('polynomial order')