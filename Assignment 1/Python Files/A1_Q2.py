#!/usr/bin/env python
# coding: utf-8

# In[1]:


#hassas48, 400188482, Shaheer Hassan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests


# In[2]:


#import csv from local save

heart_disease = pd.read_csv('heart_disease.csv')
#heart_disease.info() #to see which columns have missing data entries (Part 1) and datatype

#Remove all rows with missing values (have only rows that have data values for all categories) - Part 1
HD_rowremove=heart_disease.dropna()
#HD_rowremove.info()


# In[3]:


#Part 2, remove the columns that are irrelavent to the question 
cleaned_HD= HD_rowremove.drop(columns=['Sex','Chest Pain','Trestbps','Chol','Fbs','Restecg','Thalach','Exang','Oldpeak','Ca','Thal'])
#cleaned_HD.info() #check the columns after removing 


# In[4]:


#convert these specific categories' arguements into a numeric type of float or int, setting to 'coerce' error (Part 2)
cleaned_HD["Age"]=pd.to_numeric(cleaned_HD["Age"],errors='coerce') #since this is in object, must convert to numeric float
cleaned_HD["Slope"]=pd.to_numeric(cleaned_HD["Slope"],errors='coerce') #object, must convert
#cleaned_HD.dtypes


# In[5]:


pd.options.display.float_format='{:.3f}'.format


# In[6]:


#Remove entire rows with missing data points above to get complete dataset 
cleaned_HD_null=cleaned_HD.dropna()
#cleaned_HD_null.describe()


# In[7]:


column = cleaned_HD_null["Age"]
max_value = column.max() 
#print(max_value)


# In[8]:


Age1 = cleaned_HD_null[(0<cleaned_HD_null.Age)&(cleaned_HD_null.Age<100)] #Age requirements for Q3
Slope = (cleaned_HD_null.Slope>=1)&(cleaned_HD_null.Slope<=3)


# In[9]:


#Obtain values with limitations of Age and slope defined above 

#cleaned_HD=cleaned_HD_null[Age1 & Slope]
#cleaned_HD.describe()


# In[10]:


#Part 4
#Ages variable with their conditions 
Age2 = cleaned_HD_null[(cleaned_HD_null.Age<=40)&(cleaned_HD_null.Age>0)]
Age3 = cleaned_HD_null[(cleaned_HD_null.Age>=41)&(cleaned_HD_null.Age<=50)]
Age4 = cleaned_HD_null[(cleaned_HD_null.Age>=51)&(cleaned_HD_null.Age<=60)]
Age5 = cleaned_HD_null[(cleaned_HD_null.Age>60)&Slope]

#Slope Categories
Slope1=cleaned_HD_null[(cleaned_HD_null.Slope==1.0)]
Slope2=cleaned_HD_null[(cleaned_HD_null.Slope==2.0)]
Slope3=cleaned_HD_null[(cleaned_HD_null.Slope==3.0)]

#Heart Disease Categories

HD_yes = cleaned_HD_null[(cleaned_HD_null.Heart_Disease==1)]
HD_no = cleaned_HD_null[(cleaned_HD_null.Heart_Disease==0)]

#"1" = Ages <= 40
#"2" = Ages >= 41 & <= 50
#"3" = Ages >= 51 & <= 60
#"4" = Ages > 60

#dataframe for all ages

Age_All = pd.DataFrame({"Age of patients": Age1.Age})

#dataframe variable that has different categories of ages 
Age_Category = pd.DataFrame({"Ages <= 40": Age2.Age, " Ages >= 41 & <= 50": Age3.Age, "Ages >= 51 & <= 60": Age4.Age, "Ages > 60": Age5.Age})
Age_Category_Slope = pd.DataFrame({"Slope = 1": Slope1.Slope, "Slope = 2": Slope2.Slope, "Slope = 3": Slope3.Slope})
HD = pd.DataFrame({"Heart Disease Positive": HD_yes.Heart_Disease, "Heart Disease Negative": HD_no.Heart_Disease})

#Test to see if object can provide correct count, mean, etc. 
#cleaned_HD=cleaned_HD_null[df_Age["1"] & Slope]
#cleaned_HD.describe()


# In[13]:


#Create Figures (Part 5)

ax = Age_All.plot.hist(bins=18)
plt.title('Age Frequency Plot', size=13)
plt.savefig('AgeHistogramQ2.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()

#histogram plot for age category 
fig2 = plt.figure()
ax = Age_Category.plot.hist(bins=18, alpha=0.5)
plt.title('Age Category Frequency Plot', size=13)
plt.savefig('AgeCategoryHistogramQ2.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()

fig3 = plt.figure()
ax = Age_Category_Slope.plot.hist(bins=18)
plt.title('Frequency of Slopes Plot', size=13)
plt.savefig('SlopeHistogramQ2.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()

fig4 = plt.figure()
ax = HD.plot.hist(bins=18)
plt.title('Frequency of Heart Disease Presence Plot', size=13)
plt.savefig('HDHistogramQ2.jpg', dpi=300, format='jpg', bbox_inches = 'tight', transparent='false')
plt.show()


# In[ ]:




