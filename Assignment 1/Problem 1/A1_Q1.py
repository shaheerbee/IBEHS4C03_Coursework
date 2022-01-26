#!/usr/bin/env python
# coding: utf-8

# In[1]:


#APPENDIX A

#hassas48, 400188482, Shaheer Hassan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests


# In[2]:


Hospital_boards = pd.read_csv('hospital.csv')

cleaned_board = Hospital_boards.drop(columns=['Age', 'Id', 'Sex', 'Temp', 'WBC','Bact_cul', 'Service'])
antibody_pos = cleaned_board.loc[cleaned_board['Antibio']>0]
antibody_neg = cleaned_board.loc[cleaned_board['Antibio']<1]

DS_1=pd.DataFrame(antibody_pos)
DS_2=pd.DataFrame(antibody_neg)

stay_pos = DS_1['Dur_stay'].values.tolist() # add values to empty list for positive antibody and hospital stay
stay_neg = DS_2['Dur_stay'].values.tolist() # add values to empty list for negative antibody and hospital stay 

print ("antibiotic = positive, stdv = ", (round(np.std(stay_pos),2)),"\n")
print ("antibiotic = positive, mean = ",(round(np.mean(stay_pos),2)),"\n")
print ("antibiotic = positive, variance = ",(round(np.var(stay_pos),2)),"\n")
print ("antibiotic = positive, min,Q1,median,Q3,max = ",min(stay_pos),np.percentile(stay_pos,[25,50,75],interpolation='midpoint'),max(stay_pos))

print ("antibiotic = negative, means = ",(round(np.mean(stay_neg),2)),"\n")
print ("antibiotic = negative, stdv = ",(round(np.std(stay_neg),2)),"\n")
print ("antibiotic = negative, variance = ",(round( np.var(stay_neg),2)),"\n")
print ("antibiotic = negative, min,Q1,median,Q3,max = ",min(stay_neg),np.percentile(stay_neg,[25,50,75],interpolation='midpoint'),max(stay_neg))


#Create Box Plots for both positive and negative antibody
fig, ax=plt.subplots(nrows=1, ncols=2)
plt.yticks(np.arange(0,30,3))
ax[0].boxplot(stay_pos)
ax[1].boxplot(stay_neg)
plt.savefig('boxplotQ1.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()


#Create the Q1 Histogram (for positive antibody) 
sns.set()
h=sns.histplot(stay_pos, bins=[0,5,10,15,20,25,30])
plt.xlabel('Duration of Hospital Stay (Days)')
plt.ylabel('Count of Patients')
plt.title('Frequency of Patients and the Duration of their Stay (Antibody = +)', size=13)
h.set_xticks([2.5, 7.5, 12.5, 17.5, 22.5, 27.5])
h.set_xticklabels(["0-5", "5-10", "10-15", "15-20", "20-25", "25-30"])
plt.savefig('histogrampositiveQ1.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()

#Create the Q1 Histogram (for negative antibody) 
sns.set()
h=sns.histplot(stay_neg, bins=[0,5,10,15,20,25,30])
plt.xlabel('Duration of Hospital Stay (Days)')
plt.ylabel('Count of Patients')
plt.title('Frequency of Patients and the Duration of their Stay (Antibody = -)', size=13)
h.set_xticks([2.5, 7.5, 12.5, 17.5, 22.5, 27.5])
h.set_xticklabels(["0-5", "5-10", "10-15", "15-20", "20-25", "25-30"])
plt.savefig('histogramnegativeQ1.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()






# In[ ]:





# In[ ]:




