#Lots of Imports 
import numpy
import matplotlib
import scipy
import matplotlib.pyplot as plt
from scipy.interpolate import *
import numpy as np
from numpy import *
from scipy.optimize import curve_fit
from scipy.integrate import *
#DATA Set
x = [ 1., 1.5,  2., 2.5, 3.,3.5, 4., 4.5, 5., 5.5,  6., 6.5, 7., 7.5, 8.,8.5, 9., 9.5, 10.]
y = [3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45, 14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86]
plt.scatter(x,y,label = 'RAW DATA',color = '#000000')

#Linear Fit
poly1 = np.polyfit(x,y,1)
lin1poly = np.poly1d(poly1)
t = np.linspace(min(x),max(x),10)
plt.plot(t,lin1poly(t),('-'),label = 'Linear',color = 'green')
#Cubic Fit
poly3 = np.polyfit(x,y,3)
lin3poly = np.poly1d(poly3)
t = np.linspace(min(x),max(x),10)
plt.plot(t,lin3poly(t),('--'), label = 'Cubic')
#Integration using SciPy
area = scipy.integrate.quad(lin3poly,min(x),max(x))
area = area[0]

#Plotting / Saving
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Linear vs. Cubic Fitting Comparisson')
plt.legend()
plt.text(5,4,'Area is ' + str(area), fontsize = 12,color = 'black')
plt.fill_between(x,lin3poly(x),color = 'gray',alpha = '0.2',hatch = '.')
plt.savefig('ACHOI_02.png')
plt.show()


#Bayesian Information Criterion
def BIC(y, yhat, k, weight = 1):
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B

def BICtest():
	err = []
	for i in range(1,10):
		coefficient = np.polyfit(x,y,i)
		p = np.poly1d(coefficient)
		err.append(BIC(y,p(x),i))
	errorLinear = err[0]
	errorCubic = err[2]
	plt.scatter(range(1,10),err)
	plt.xticks(np.arange(min(x),10,1))
	plt.text(1,34,'Linear Bayesian = ' + str(errorLinear),fontsize = 10)
	plt.text(1,32,'Cubic Bayesian = ' + str(errorCubic),fontsize = 10)
	
	plt.show()
		

	
