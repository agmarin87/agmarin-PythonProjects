# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:57:14 2020

@author: agm
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb #for the correlation heatmap
start_dir = r'D:\TRABAJO\Mis_programas\World happiness' 

#read the real-time data online from this website.
df = pd.read_csv('2019.csv', header=0)

#Correlation figure
plot1 = plt.figure(1)
plt.title('World happiness report 2019')
df_pearson = df.iloc[:,[2,3,4,5,6,7,8]] 
pearsoncorr = df_pearson.corr(method='pearson')
sb.heatmap(pearsoncorr, 
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            annot=True,
            annot_kws={"fontsize":12},
            linewidth=0.3)

#watermark
plt.text(-1, -1, 'By Antonio García Marín',
         fontsize=20, color='gray',
         ha='center', va='center', alpha=0.8)
#save plot
plt.savefig(r'D:\TRABAJO\Mis_programas\World happiness\Word_report_correl_2019.png', 
            dpi=100, bbox_inches='tight')

#second plot
plot1 = plt.figure(2)
labels=df['Country or region']
x = df['Overall rank']
y = df['Score']
plt.scatter(x,y, alpha=1, label=labels, marker='.')