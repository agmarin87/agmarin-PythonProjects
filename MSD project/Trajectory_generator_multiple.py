# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:43:38 2020

@author: Antonio Garcia Marin
"""
from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numbers

#The msd_fft and autocorrFFT fuctions were taken from the website: https://stackoverflow.com/questions/34222272/computing-mean-square-displacement-using-python-and-fft
def msd_fft(r):
  N=len(r)
  D=np.square(r).sum(axis=1) 
  D=np.append(D,0) 
  S2=sum([autocorrFFT(r[:, i]) for i in range(r.shape[1])])
  Q=2*D.sum()
  S1=np.zeros(N)
  for m in range(N):
      Q=Q-D[m-1]-D[N-m]
      S1[m]=Q/(N-m)
  return S1-2*S2

def autocorrFFT(x):
  N=len(x)
  F = np.fft.fft(x, n=2*N)  #2*N because of zero-padding
  PSD = F * F.conjugate()
  res = np.fft.ifft(PSD)
  res= (res[:N]).real   #now we have the autocorrelation in convention B
  n=N*np.ones(N)-np.arange(0,N) #divide res(m) by (N-m)
  return res/n #this is the autocorrelation in convention A

alldf = []
n = 2 #number of generated tracks
N = 100 #Number of generated points in each track

for i in range(n):
    r = np.cumsum(np.random.choice([-1., 0., 1.], size=(N, 3)), axis=0)
    #create a dataframe from an array 'r' including the MSD calculation (MSD elegant)
    df = pd.DataFrame({'POSITION_X': r[:, 0], 'POSITION_Y': r[:, 1], 'POSITION_Z': r[:, 2], 'MSD': msd_fft(r)}) 
    df.insert(loc=0, column='TIME', value=np.arange(len(df))) #add a column of time as the first column (loc=0)
    #The next set of 10 lines with calculations are made to obtain the second way to get the MSD (MSD average)
    df['diffX'] = df['POSITION_X'] - df['POSITION_X'].iloc[0]
    df['diffY'] = df['POSITION_Y'] - df['POSITION_Y'].iloc[0]
    df['diffX2'] = df['diffX']**2
    df['diffY2'] = df['diffY']**2
    df['MSD1'] = df['diffX2'] + df['diffY2']

    #Add each dataframe into a list called alldf
    alldf.append(df)    
    #plot data
    x = df['TIME']
    y = df['MSD']
    z = df['POSITION_Z']
    plt.figure() #This line is important. Without this line, it will show all trayectories in one Figure
    plt.scatter(df['POSITION_X'],df['POSITION_Y'],c=x, cmap="viridis", alpha=0.4, marker='.')
    plt.title('Example of Trajectory')
    plt.xlabel('X position')
    plt.ylabel('Y position')

#create a single dataframe with all the data from the list
alldf_together = pd.concat(alldf, axis=1)

#these lines are doing some steps in order to make the average of the MSD columns
alldf_together_trans = alldf_together.transpose()
alldf_together_trans_mean = alldf_together_trans.groupby(by=alldf_together_trans.index, axis=0).apply(lambda g: g.mean() if isinstance(g.iloc[0,0], numbers.Number) else g.iloc[0])
alldf_final = alldf_together_trans_mean.transpose()

#NOW THE CODE TO PLOT THE MSD DATA
#Plot MSD (first method)
plot1 = plt.figure(n+1)
x = alldf_final['TIME']
y = alldf_final['MSD']
plt.yscale('log')
plt.xscale('log')
#set a limit for y axis
#plt.ylim(0, 5000)
plt.plot(x,y, label='MSD elegant method', alpha=1.0, marker='.')
plt.title('MSD elegant method' + ', ' + str(n) + ' trayectories' + ', ' + str(N) + ' points')
plt.xlabel('Time')
plt.ylabel('MSD value')
plt.legend(loc='best')

#Plot MSDaverage (second method)
plot1 = plt.figure(n+2)
x = alldf_final['TIME']
y = alldf_final['MSD1']
plt.yscale('log')
plt.xscale('log')
#set a limit for y axis
#plt.ylim(0, 5000)
plt.plot(x,y, label='MSD average method', alpha=1.0, marker='.')
plt.title('MSD average method' + ', ' + str(n) + ' trayectories' + ', ' + str(N) + ' points')
plt.xlabel('Time')
plt.ylabel('MSD value')
plt.legend(loc='best')

#Plot MSDaverage and MSD together
plot1 = plt.figure(n+3)
x = alldf_final['TIME']
y = alldf_final['MSD1']
plt.plot(x,y, alpha=1.0, marker='.')
x = alldf_final['TIME']
y = alldf_final['MSD']
plt.yscale('log')
plt.xscale('log')
#set a limit for y axis
plt.ylim(-10, 5000)
plt.plot(x,y, alpha=1.0, marker='.')
plt.title('Both methods for MSD' + ', ' + str(n) + ' trayectories' + ', ' + str(N) + ' points')
plt.xlabel('Time')
plt.ylabel('MSD value')
plt.legend(['MSD average method', 'MSD elegant method'], loc='best')
