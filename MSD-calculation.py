# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:51:23 2020

@author: Antonio Garcia Marin
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

N = 1000 #Number of points generated
r = np.cumsum(np.random.choice([-1., 0., 1.], size=(N, 3)), axis=0) #this line creates a 3D array 'r'

#For the MSD calculation. Info found in https://stackoverflow.com/questions/34222272/computing-mean-square-displacement-using-python-and-fft
def autocorrFFT(x):
  N=len(x)
  F = np.fft.fft(x, n=2*N)  #2*N because of zero-padding
  PSD = F * F.conjugate()
  res = np.fft.ifft(PSD)
  res= (res[:N]).real   #now we have the autocorrelation in convention B
  n=N*np.ones(N)-np.arange(0,N) #divide res(m) by (N-m)
  return res/n #this is the autocorrelation in convention A

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

#create a dataframe from an array 'r' including the MSD calculation
df = pd.DataFrame({'POSITION_X': r[:, 0], 'POSITION_Y': r[:, 1], 'POSITION_Z': r[:, 2], 'MSD': msd_fft(r)}) 
df.insert(loc=0, column='TIME', value=np.arange(len(df))) #add a column of time as the first column (loc=0)


#plt.plot(df['POSITION_X'],df['POSITION_Y'], alpha=0.4, marker='.') #para plotear la trayectoria

x = df['TIME']
y = df['MSD']
z = df['POSITION_Z']
plt.yscale('log')
plt.xscale('log')
plt.title('Example of MSD plot')
plt.xlabel('Time')
plt.ylabel('MSD')
plt.plot(x,y, alpha=0.4, marker='.')
