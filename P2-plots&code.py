import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from ggplot import *

%matplotlib inline
%pylab inline


cd python/p2

data=pd.read_csv('turnstile_weather_v2.csv')  

#P2 - visualization 1 - stacked histogram
plt.figure()
data[data['rain']==0]['ENTRIESn_hourly'].hist(label='No Rain', bins = 120) # your code here to plot a historgram for hourly entries when it is raining
data[data['rain']==1]['ENTRIESn_hourly'].hist(label = 'Rain', bins = 120)# your code here to plot a historgram for hourly entries when it is not raining
plt.legend(loc='upper right')
plt.title("Hourly Entries - Histogram (Rain VS No Rain)")
plt.xlabel("ENTRIESn_Hourly" )
plt.ylabel("FREQUENCY")
plt.xlim([0,10000])
plt.show()



#We aggregate the dataset to have the average number of entries by hour
avg_ENTRIESn_rain_hourly=data[data['rain']==1].groupby("hour").ENTRIESn_hourly.mean()
ggplot(avg_ENTRIESn_rain_hourly,aes(avg_ENTRIESn_rain_hourly.index,avg_ENTRIESn_rain_hourly.values))+geom_point() +\
geom_line(color='red')+xlab("Hour")+ ylab("Average number of entries (Rainy days)")+ggtitle("Average number of entries by time of day (on Rainy days)")+xlim(0,24)


#We aggregate the dataset to have the average number of entries by hour
avg_ENTRIESn_norain_hourly=data[data['rain']==0].groupby("hour").ENTRIESn_hourly.mean()
ggplot(avg_ENTRIESn_norain_hourly,aes(avg_ENTRIESn_norain_hourly.index,avg_ENTRIESn_norain_hourly.values))+geom_point() +\
geom_line(color='red')+xlab("Hour")+ ylab("Average number of entries (Non-Rainy days)")+ggtitle("Average number of entries by time of day (on non-rainy days)")+xlim(0,24)
