# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:04:38 2020

@author: Antonio García Marín

Example of fitting: exponential curve and residuals plotting.

Extra info can be found here: https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509

"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
# Import curve fitting package from scipy
from scipy.optimize import curve_fit

#defining the exponential curve.
def exponential(x, a, b):
    return a*np.exp(b*x)

# Generate dummy dataset
x = np.linspace(start=5, stop=15, num=50)
y = exponential(x, 0.5, 0.5)
# Add noise from a Gaussian distribution
noise = 5*np.random.normal(size=y.size)
y = y + noise

#Figure 1. Plotting curve
plot1 = plt. figure(1)
plt.plot(x,y, alpha=0.4, marker='.')

plt.title('Curve plot')
plt.xlabel('X variable')
plt.ylabel('Y variable')

#in case you want legend: 
plt.legend(['Legend here'], loc='best')
   

"""
# After these lines, the data will be fitted
f — function used for fitting (in this case exponential)
xdata — array of x-data for fitting
ydata — array of y-data for fitting
p0 — array of initial guesses for the fitting parameters (both a and b as 0)
bounds — bounds for the parameters (-∞ to ∞)
"""
pars, cov = curve_fit(f=exponential, xdata=x, ydata=y, p0=[0, 0], bounds=(-np.inf, np.inf))
print(pars)

#Plotting the fit in Figure 1.
plt.plot(x,exponential(x, *pars), alpha=0.4, linestyle='--', linewidth=2, color='black')

# Get the standard deviations of the parameters (square roots of the # diagonal of the covariance)
stdevs = np.sqrt(np.diag(cov))
# Calculate the residuals
res = y - exponential(x, *pars)
ss_res = np.sum(res**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
print("r^2 =", r_squared)

#Figure 2. Plotting residuals
plot2 = plt. figure(2)
plt.plot(x,res, alpha=0.4, marker='.')
