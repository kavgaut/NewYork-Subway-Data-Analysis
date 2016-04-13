     -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:04:50 2015

@author: kavyagautam
"""

import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from ggplot import *

def model_fit(y,X):
    ols_model = sm.OLS(y, X)
    ols_results = ols_model.fit()
    return ols_results
    
data=pd.read_csv('turnstile_weather_v2.csv')    
    
#For some visualization
#We aggregate the dataset to have the average number of entries by hour
avg_ENTRIESn_hourly=data.groupby("hour").ENTRIESn_hourly.mean()

ggplot(avg_ENTRIESn_hourly,aes(avg_ENTRIESn_hourly.index,avg_ENTRIESn_hourly.values))+geom_point() + geom_line(color="red") +\
xlab("Hour")+ ylab("Average number of entries")+ggtitle("Average number of entries by hour")+xlim(0,20)

#OR

#VISUALIZATION 1
#We aggregate the dataset to have the average number of entries by hour
avg_ENTRIESn_hourly=data.groupby("hour").ENTRIESn_hourly.mean()
ggplot(avg_ENTRIESn_hourly,aes(avg_ENTRIESn_hourly.index,avg_ENTRIESn_hourly.values))+geom_bar(stat='bar') +\
geom_line(color='red')+xlab("Hour")+ ylab("Average number of entries")+ggtitle("Average number of entries by hour")+xlim(0,24)

#VISUALIZATION 2
#We will try to aggregate average number of entries per Station with rain vs no rain depiction
avg_ENTRIESn_perunit=data.groupby("UNIT").ENTRIESn_hourly.mean()

ggplot(avg_ENTRIESn_perunit,aes(avg_ENTRIESn_perunit.index,avg_ENTRIESn_perunit.values))+geom_bar(stat='identity', width=10) +\
xlab("UNIT / STATION")+ ylab("Average number of entries") + ggtitle("Average number of entries by UNIT")

#(OR) Another way of doing avg num of entries by station (NOT COMPLETE)
result=data.groupby(['station','latitude','longitude']).ENTRIESn_hourly.mean().reset_index()
result=result.sort('ENTRIESn_hourly',ascending=False).head(15)

#Visualization 3
#Avergae entries by day
AVG_ENTRIESn_hourly_by_day=data.groupby("day_week").ENTRIESn_hourly.mean()
ggplot(AVG_ENTRIESn_hourly_by_day,aes(x=AVG_ENTRIESn_hourly_by_day.index,y=AVG_ENTRIESn_hourly_by_day.values))+geom_bar(stat = "identity")\
+ xlab("Day of the week")+ ylab("Average number of entries hourly")+ggtitle("Average number of entries hourly by day") +scale_x_discrete(breaks=range(0,7,1),
labels=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])

#Visualization 4 (DONT know hwy - but doesnt work)
ggplot(data, aes('Hour','ENTRIESn_hourly', fill = 'rain')) + geom_bar() + xlab('Hour of the day') + ylab('Hourly entries') + ggtitle('Hourly entries/Ridership based on the hour of the day and indicating Rain Vs no Rain')

#P2 - visualization 1 - stacked histogram
plt.figure()
data[data['rain']==0]['ENTRIESn_hourly'].hist(label='No Rain', bins = 120) # your code here to plot a historgram for hourly entries when it is raining
data[data['rain']==1]['ENTRIESn_hourly'].hist(label = 'Rain', bins = 120)# your code here to plot a historgram for hourly entries when it is not raining
plt.legend(loc='upper right')
plt.title("Hourly Entries - Histogram (Rain VS No Rain)")
plt.xlabel("ENTRIESn_Hourly" )
plt.ylabel("FREQUENCY")
plt.xlim([0,10000])

#P2 - Visualization 2 - ridership by day
hourly_entries_by_day = data.groupby("day_week").ENTRIESn_hourly.mean()
ggplot(hourly_entries_by_day,aes(hourly_entries_by_day.index,hourly_entries_by_day.values,fill = 'green'))+geom_bar()\
+ xlab("Day of the week")+ ylab("Number of entries hourly")+ggtitle("Number of entries hourly by day of the week")

