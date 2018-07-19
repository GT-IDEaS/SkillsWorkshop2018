import matplotlib.pyplot as plt, matplotlib,numpy as np
from IPython.display import Image
from pylab import *
from scipy.stats import linregress
from scipy.optimize import curve_fit
from scipy.integrate import quad

def figure(x, y,xr=None,yr=None,integral = None):
    '''  Plots a scatter plot using x as the independent variable and y as the 
    dependent variable; also, if a regression is performed, it plots the regression as well '''
    
    fig = plt.figure() #creates the object figure

    axes = fig.add_axes([0.1, 0.12, 0.85, 0.8]) # left, bottom, width, height (range 0 to 1))

    axes.plot(x,y, 'ro') #plots the data
    axes.set_xlabel('Independent variable / A.U.') #gives name to the x-axis
    xlim(0, max(x)+2) #sets the limits of the x axis
    axes.set_ylabel('Dependent variable / A.U.') #gives name to the y-axis
    ylim(0, max(y)+5) #sets the limits of the y axis
    axes.set_title(raw_input('Name of plot: ')) #gives a title to the graph
    
    # Only show ticks on the left and bottom spines
    axes.yaxis.set_ticks_position('left')
    axes.xaxis.set_ticks_position('bottom')
    
    if yr !=None:
        if xr!=None:
            #if regression data is available, include that in the plot
            plt.plot(xr,yr)
            if integral != None:
                #if this argument is given, fill the area under the curve and include the value of the integral
                plt.fill_between(xr,yr,color="lightblue", hatch="XX", edgecolor="lightblue", linewidth=0.0)
                plt.text(xr[len(xr)/4], 1, '%f A.U.' %integral ,size = '25', ) # includes the Area under the curve value
    
    matplotlib.rcParams.update({'font.size': 17}) #Changes the font size

    matplotlib.pyplot.show() # shows the figure
    
    fig.savefig(raw_input('Name of file to save: ') +'.pdf') #Saves a pdf of the plot in the directory the user is, asking for a file name

def linear_reg(x,y):
    '''returns the parameters from a linear regression'''
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    return slope, intercept

def cubic(x,a,b,c,d):
        return a*(x**3) + b*(x**2) + c*(x) + d

def cubic_reg(x,y,cubic):
    '''returns the xr and yr from a cubic fitting regression'''

    params, params_covariance = curve_fit(cubic,x,y)
    
    xr = np.linspace(x[0],x[-1],100)
    yr = cubic(np.linspace(x[0],x[-1],100),*params)
    
    return xr,yr,params


#Data set
x = [ 1.,   1.5,  2.,   2.5,  3.,   3.5,  4.,   4.5,  5.,   5.5,  6.,   6.5,  7.,   7.5, 8.,   8.5,  9.,   9.5, 10. ]
y = [3.43, 4.94, 6.45, 9.22, 6.32, 6.11, 4.63, 8.95, 7.8, 8.35, 11.45, 14.71, 11.97, 12.46, 17.42, 17.0, 15.45, 19.15, 20.86]

def BIC(y, yhat, k, weight = 1):
    '''Calculates the Bayesian information criterion (BIC) of the fitted model'''
    err = y - yhat
    sigma = np.std(np.real(err))
    n = len(y)
    B = n*np.log(sigma**2) + weight*k*np.log(n)
    return B

def plotting_linear(x,y): #Calculates and plots the parameters for the linear regression
    line_param = linear_reg(x,y)
    a,b = line_param
    linear = [((i*a)+b) for i in x]
    figure(x,y,x,linear)
    return line_param


def plotting_cubic(x,y): 
#Calculates and plots the parameters for the cubic model, integrating the area under the curve
    xr,yr,params = cubic_reg(x,y,cubic)
    a,b,c,d = params
    I = quad(cubic, xr[0], xr[-1], args = (a,b,c,d))
    i,error = I
    figure(x,y,xr,yr, i)
    
    return params

def BIC_comp(x,y):
    '''Compares the Bayesian information criterion (BIC) of the fitted models'''
    
    q = np.poly1d(plotting_linear(x,y))
    p = np.poly1d(plotting_cubic(x,y))
    
    
    BIC_cubic = BIC(y,p(x),3)
    BIC_linear = BIC(y,q(x),1)
    
    if BIC_cubic <= BIC_linear:
        print 'Cubic model (BIC: %f) is preferable over linear model (BIC: %f)' %(BIC_cubic,BIC_linear)
    else:
        print 'Linear model (BIC: %f) is preferable over cubic model (BIC: %f)' %(BIC_linear,BIC_cubic)

figure(x,y)
BIC_comp(x,y)