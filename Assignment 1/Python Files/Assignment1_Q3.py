#hassas48, 400188482, Shaheer Hassan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

#read covidcases csv file from folder (saved file locally) 
covidcases = pd.read_csv('covidcases.csv')

#replace all the '_' in the columns with a ' ' (space)
covidcases.columns = covidcases.columns.str.replace('[_]', ' ')

#fill all NA values with an int value of 0
remove_null=covidcases.fillna(0)
remove_null.info

#Cleaning Files Steps to format files for Time Series Graph (Halton)  

cleaned=remove_null.drop(remove_null.columns[[range(1,9,1)]], axis=1) #remove all data entries before halton entries
cleaned_1=cleaned.drop(remove_null.columns[[range(10,36)]], axis=1) #remove all data entries after halton entries 
cleaned_halton=cleaned_1.drop(labels=range(0,648),axis=0)
cleaned_halton.reset_index(drop=True, inplace=True)

#Format dataframe to calculate means for all municipalities for bar graph 
cleaned_mean=remove_null.drop(remove_null.columns[[0,35]],axis=1)
mean=cleaned_mean.mean() # calculate mean value of all the covid cases for each municipality 
mean=mean.sort_values(ascending=False) # sort all series values in ascending order for a horizontal graph (see below)

#Creating Graphs/Figures Code 
plt.close('all')
fig1 = plt.figure()
bar_graph=mean.plot.barh(figsize=(7,9), fontsize=10, color='green', rot=0)
plt.ylabel("Municipality",size=14)
plt.xlabel("Number of COVID Cases", size=14)
plt.title("Average Number of COVID Cases by Municipalities", size=15)
plt.savefig('BarplotQ3.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()

fig2 = plt.figure()
time_series=cleaned_2.plot(figsize = (9,6), color='green',linewidth=1)
plt.xlabel("Day in 2022", size=14)
plt.ylabel("Number of COVID Cases", size=14)
plt.title("Number of 2022 COVID Cases in the Halton region", size=15)
plt.savefig('TSQ3.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()
