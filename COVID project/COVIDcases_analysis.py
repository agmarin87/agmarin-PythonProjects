# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:19:21 2020

@author: Antonio Garcia marin
"""
import pandas as pd
import matplotlib.pyplot as plt

def Countryinclude(country):
    #Slice and create the dataframes
    df_country = df.loc[df['location'] == country]
    #Starting to plot data from the country
    x = df_country['date']
    y = df_country['new_cases_per_million']
    plt.scatter(x,y, label=country, linewidth=0.2, alpha=1, marker='.')
    plt.title('COVID cases')
    plt.xlabel('Date')
    plt.ylabel('New cases per million of habitants')
    plt.legend(loc='best')
    
#read the real-time data online from this website.
df = pd.read_csv("https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv", header=0)

#Plot everything in one Figure
plot1 = plt.figure(1)

#Call the function. Just write the countries you want in the plot.
Countryinclude('Czech Republic')
Countryinclude('Spain')
Countryinclude('Poland')
Countryinclude('Italy')
Countryinclude('France')
Countryinclude('Germany')

#set a limit for y axis
plt.ylim(0, 800)

#set manually the number of ticks to 30 and the number of x labels to the number of data divided by 30.
#number n should be the same for both lines.
n=30

#Forcing to have a specific number of ticks. All countries have the same amount of data
df_time = df.loc[df['location'] == 'Czech Republic']
x = df_time['date']

plt.xticks(x, x[::n], rotation=45)
plt.locator_params(axis='x', nbins=len(x)/n)