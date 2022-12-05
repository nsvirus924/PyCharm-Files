###Seaborn
#used for data visualization and is based on matplotlib
#allows the creation of statistical graphis

#--functions
#allows comparison between multiple variables
#supports multiplot grids
#available univariate and bivariate visualizations
#availability of different colour palettes
#estimates and plots linera regression automatically



#plotting seaborn functions
#scatter plot and line plot
#we'll use relplot function

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a=pd.read_csv(r'D:\diabetes.csv')
#nik=sns.relplot(x="BloodPressure",y="Age",data=a)
#plt.show()


#nik=sns.relplot(x="BloodPressure",y="Age",hue="Glucose",data=a)
#plt.show()
#This plot is scatter plot



#for line plot
#same data
#nik=sns.relplot(x="BloodPressure",y="Insulin",data=a,kind="line")
#plt.show()


#categorical data
#catplot function
a=pd.read_csv(r'D:\diabetes.csv')
#nik=sns.catplot(x='BloodPressure',y='Insulin',data=a.head(100))
#plt.show()


#nik=sns.catplot(x='BloodPressure',y='Age',kind="violin",data=a.head(10))
#plt.show()


#nik=sns.catplot(x='BloodPressure',y='Age',kind="boxen",data=a.head(10))
#plt.show()






#Plotting univariate and birvariate distributions

from scipy import stats
#c=np.random.normal(loc=5,size=100,scale=2)
#nik=sns.distplot(c)
#plt.show()

#bivariate data....example




#Multiplot Grids
#side by side

#facegrid function
a=pd.read_csv(r'D:\diabetes.csv')
#d=pd.read_csv(r'D:\Iris.csv')
#nik=sns.FacetGrid(a.head(4),col="BloodPressure")
#nik=map(plt.hist,"Age")
#plt.show()



#nick=sns.PairGrid(a.head(4))
#nik=map(plt.scatter,"Age")
#plt.show()





##Plot--Aesthetics(Decorate plots)

#a=pd.read_csv(r'D:\diabetes.csv')
#nik=sns.set(style='darkgrid')    #dark, white etc.
#b=sns.PairGrid(a.head(4))
#b=map(plt.scatter,'BloodPressure')
#plt.show()

sns.set(style='white',color_codes=True)
a=pd.read_csv(r'D:\diabetes.csv')
b=sns.boxplot(x='BloodPressure',y='Age',data=a)
#plt.show()


#despine function
sns.set(style='white',color_codes=True)
a=pd.read_csv(r'D:\diabetes.csv')
b=sns.boxplot(x='BloodPressure',y='Age',data=a)
c=sns.despine(offset=10,trim=True)
#plt.show()



#colour pallete function
c=sns.color_palette()
a=sns.palplot(c)
plt.show()





