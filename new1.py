"""import random
casino=random.sample(range(0,10000),1000)
print(casino)
def gap_test(casino):
    pass
nik=gap_test('casino')
print(nik)
"""

# tree handles this case.
#18/07/2022
"""Lab session 1 Python"""

#It is my first python lab
"""Welcome to SY MSc Statistics"""

print("Hello World")
print('hello world')


#Data Types
A=None
print(A,type(A))
x=4
print(x,type(x))
a=3.7
print(type(a))
c=True
print(type(c))

###
z=3.7
print(z, type(z))
z1=z-2
print(z1)
z2=z/3
print(z2)
z3 =z
print(z3)
z4= z **2
print(z4)
z5= z4**0.5
print(z5)
z6=pow(z, 2)
print(z6)
z7=round(z)
print(z7)
z8 =(int(z))
print(z8, type(z8))

####
import math
x=4
print(math.sqrt(x))
print(math.pow(x,2))
print(math.log(x,2))
print(math.exp(x))
print(math.fabs(-4))
print(math.factorial(x))


####
z=3*math.pi
print(z)
print(math.sin(z))

##
x=math.inf
print(math.isinf(x))
x=math.nan
print(math.isnan(x))

"""19/07/2022"""
import math
z=0.2
print(math.ceil(1561.75))
print(math.ceil(-1561.75))
print(math.floor(2.4))
print(math.floor(z))
print(math.floor(14.76))


#logical operations
y1=True
y2=False
print(y1 and y2)
print(y1 or y2)
print(y1 and not y2)

#string
string_1="Hello"
string_2="World!"
print(string_1+string_2)

string='Recursion...'*5
print(string)

string= "Im stuck in a"+"loop..."*5
print(string)

s= 'Hello'
s+= 'world'

print(len("MIT-WPU World Famous University"))

text="writing python is quite fun."
print(text.find("quite"))
print(text.find("at"))

text = "I haven't been this choked up since I got a hunk of moussaka caught in my throat! - Hadas."
text2="I"
print(text.find(text2))
print(text.find(text2,10))
print(text.find(text2,40))

text="The MITWPU university is famous for its greenery"
text_count=text.count('e')
print("the count of e is",text_count)



"""20/07/2022 Lab Session"""
text="hello,world"
print(text[6:12])

text= "the code runs fast"
print(text[3:7:2])
print(text[4:11:2])

text1= "the code runs fast"
print(text1[11:4:-2])

text = "hello world"
print(text.startswith("H"))
print(text.endswith("d"))

text= '       a short break'
print(text.strip())
print(text.rstrip())
print(text.lstrip())

text= "when life gets you down you know what you've gotto do? Just keep swimming! - Finding Nemo"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())


text="To be or not to be, that is the question"
print(text.partition(('to be')))
print(text.split())

text= ['one','two', 'three', 'four']
print(','.join(text))



"""Friday 22/07/2022"""
import math
z=0.2
print(math.ceil(z))
print(math.floor(z))
print(math.trunc(z))

thislist=["apple","banana","cherry"]
print(thislist)

# Duplicate
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# type
thislist = ["apple", "banana", "cherry"]
print(type(thislist))



list1 = ["aba", 34, True, 40, "male"]
print(list1)
print(type(list1))



thislist = ["apple", "banana", "cherry"]
print((thislist[1]))

thislist = ["apple", "banana", "cherry"]
print((thislist[-1]))

thislist = ["apple", "banana", "cherry"]
print((thislist[-2]))

thislist = ["apple", "banana", "cherry", "orange", "kivi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kivi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kivi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kivi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry", "orange", "kivi", "melon", "mango"]
print(thislist[-1:-4])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrent"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[2] = "blackcurrent"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kivi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# append               It added in the end
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


# for loop
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


# while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1



"""Saturday 23/07/2022"""

fruits=["apple","banana", "cherry","kivi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

fruits=["apple","banana", "cherry","kivi","mango"]
newlist=[x for x in fruits if x!="apple"]
print(newlist)

fruits=["apple","banana", "cherry","kivi","mango"]
newlist=[x for x in range(10)]
print(newlist)

newlist=[x for x in range(10) if x<5]
print(newlist)

fruits=["apple","banana", "cherry","kivi","mango"]
newlist=[x.upper() for x in fruits]
print(newlist)

fruits=["apple","banana", "cherry","kivi","mango"]
newlist=["Hello!" for x in fruits]
print(newlist)

fruits=["apple","banana", "cherry","kivi","mango"]
fruits[1]="orange"
print(fruits)

fruits=["apple","banana", "cherry","kivi","mango"]
newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)

#sort
thislist=["orange","mango","kivi","pineapple","banana"]
thislist.sort()
print(thislist)

#reverse
thislist=["orange","mango","kivi","pineapple","banana"]
thislist.sort(reverse=True)
print(thislist)

thislist=[1,2,3,4,5,6]
thislist.sort(reverse =True)
print(thislist)

thislist=["banana","Orange","Kivi","cherry"]
thislist.sort()
print(thislist)

thislist=["banana","Orange","Kivi","cherry"]
thislist.reverse()
print(thislist)

thislist=["apple","banana","cherry"]
mylist= list(thislist)
print(mylist)

list1=["apple","banana","cherry"]
list2=[1,2,3]
list3=list1+list2
print(list3)

#append
list1=["apple","banana","cherry"]
list2=[1,2,3]
for x in list2:
    list1.append(x)
print(list1)

#extend
list1=["apple","banana","cherry"]
list2=[1,2,3]
list1.extend(list2)
print(list1)

#Tuple
thistuple=("apple","banana","cherry","apple","cherry")
print(thistuple)
print(type(thistuple))
print(len(thistuple))

thistuple=("apple",)
print(thistuple)
print(type(thistuple))


""" Thursday 28/07/2022"""

fruits = ("apple","banana","cherry")
mytuple= fruits*2

thisset= {"apple","apple","cherry"}
print(thisset)

thistuple = {"apple","apple","cherry"}
print(thistuple)

thislist = {"apple","apple","cherry"}
print(thislist)

set1 = {"abc",30,True,40,"male"}
print(set1)

thisdict= {
    "brand":"ford",
    "Model":"Mustang",
    "year": 1964,
}
print(thisdict)

thisdict= {
    "brand":"ford",
    "Model":"Mustang",
    "year": 1964,
    "year": 2004
}
print(thisdict)

thisdict= {
    "brand":"ford",
    "model":"Mustang",
    "color":["red","white","pink"],
    "year": 2022
}
print(thisdict)
x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)

thisdict = {
    "model":"Mustang",
    "color":["red","white","pink"],
    "year":2022
}
thisdict ["color"] = "black"
print(thisdict)

# Using if-else statement
x = 10
if x % 2 == 0:
    print("x=",x, "is even")
else:
    print("x=",x, "is odd")

if x > 0:
    print("x=",x, "is positive")
elif x < 0:
    print("x=",x, "is negative")
else:
    print("x=",x, "is neither positive nor negative")



"""Machine Learning Lab 4/08/2022"""

import pandas as pd
l1=[1,2,3,4,5]
l2=[7,8,9,5,3]
l3=['a','b','c','d']

d1=pd.DataFrame(zip(l1,l2,l3))
print(d1)

#empty frame
d2=pd.DataFrame()
print(d2)

d2['column1']=l1
d2['column2']=l2
d2['column3']=l2
print(d2)

#access particular element
print(l1)
print(l1[0:3])
print(l1[0:4])
print(l1[0:])

#fetching columns and rows together
print(d2.iloc[0:2,0:2]) # iloc = fetching the data with respect to the indices

print(d2.iloc[[0,2],[0,2]])


#We can also fetch the details directly by giving column names
print(d2.loc[[0],['column1','column3']])


#fetch a particular columns from dataset
#2 ways
print(d2.column1)
print(d2['column2'])
#fetch one or more columns at same time
print(d2[ ['column1','column2']])




"""EDA-Exploratory Data analysis"""
import seaborn as sns
import pandas as pd
df = pd.read_csv("D:\Iris.csv")
print(df)

print(df['Species'].unique())

sns.histplot(df['sepal_length'])
sns.kdeplot(df['sepal_length']) #kernal density estimator

l1=[1,2,3,4,5,6,7]
sns.kdeplot(l1)


import numpy as np
a=np.mean(l1)
n=np.median(l1)
print("The mean is",a)
print("The median is",n)

l2=[1,2,3,4,5,6,100]
b=np.mean(l2)
c=np.median(l2)
print("The mean is",b)
print("The median is",c)

sns.kdeplot(l2)

import matplotlib.pyplot as plt
plt.axvline(np.mean(l1),label='mean',color='red')
plt.axvline(np.median(l1),label='median',color='green')
plt.legend()
plt.show()

"""Right Skewed Distribution for positively skewed distribution ,mean>median"""
l1=[96,98,99,97,100]
print(l1)
print('Mean is',np.mean(l1))
print('Median is',np.median(l1))

l1=[2,98,99,97,100]
print(l1)
print('Mean is',np.mean(l1))
print('Median is',np.median(l1))


sns.kdeplot(l2)
plt.axvline(np.mean(l1),label='mean',color='red')
plt.axvline(np.median(l1),label='median',color='green')
plt.legend()
plt.show()
"""Right Skewed Distribution for positively skewed distribution ,mean<median"""

#boxPlot
nik=sns.boxplot(df['sepal_length'])
plt.show()

#find Outliers
#IQR : Q3-Q1
## Lower limit : Q1 + 1.5 * IQR
## Upper limit : Q3 + 1.5 * IQR
l1=[2,98,99,97,100]
nik=sns.boxplot(l1)
plt.show()

print(df.head())

print(df['Species'].value_counts())
#countplot - one categorical and one numerical wise graph
nik=sns.countplot(df['Species'])
plt.show()

#mean median over categorical variables
print(df['Species'].mode())


"""Bivariate Numeric Analysis"""
#Numeric Vs Numeric
print(df.head())
#corelation of all columns
x=df.corr()
print(x)

nik=sns.heatmap(x)
plt.show()
###Petal width and petal length are strongly positively correlated


nik=sns.scatterplot(df['PetalLengthCm'],df['PetalWidthCm'],data=df)
plt.show()
###Petal_length and Petal width have strong positive correlation


###2 One Categorical, One Numeric
nik=sns.boxplot(x='Species',y='PetalWidthCm',data=df)
plt.show()





"""Machine Learning Lab Session 10/08/2022 """

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df=pd.read_csv("D:/tips.csv")
print(df)

nik=sns.countplot(df['sex'],hue=df['smoker'])
plt.show()

df['smoker'].unique()
nik=sns.scatterplot(df['total_bill'],df['tip'],hue=df['sex'])
plt.show()

nik=sns.scatterplot(df['total_bill'],df['tip'],hue=df['sex'])
plt.show()

df.head()

print(df.skew()) #skewness of each column

"""""
a=['total_bill']
m=a.mean()
stdv=a.std()

df['total_bill_scaled'] = (df['total_bill'] - m)/stdv

df['total_bill_scaled'].skew(),df['total_bill'].skew()

nik=sns.kdeplot(df['total_bill_scaled'])
plt.show()
"""

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
df['total_bill_sklearn'] = ss.fit_transform(df[['total_bill']])

nik=sns.kdeplot(df['total_bill_sklearn'])
plt.show()

n=df['total_bill'].describe()
print(n)

a=df['total_bill'].skew()
print(a)

w=df['log_total_bill'] = np.log(df['total_bill'])
print(w)

#transformations
print(df['log_total_bill'].skew(),df['total_bill'].skew())


df['sqrt_total_bill'] = df['total_bill']**0.5
nik=sns.kdeplot(df['sqrt_total_bill'])
plt.show()


print(df.describe())

print(df.describe(include='object'))

print(df.shape)

print(len(df))

print(df.isnull().sum())


"""Loading Titanic dataset"""

a = pd.read_csv("D:\Titanic.csv")
print(a)

print(a.describe(include='object'))

print(a.isnull().sum())

print(a.isnull().sum()/len(a)*100)

#drop column having missing values more than 50-55%
df = a.drop('Cabin',axis=1,inplace=True)
#df = a.drop('Cabin',axis=1)

#check again the missing values percentage
print(a.isnull().sum()/len(a)*100)
print(df)

print(a['Age'].skew())


print(a['Age'].mean(),a['Age'].median())


mage=a['Age'].mean
print(mage)

c=a['Age'] = a['Age'].fillna(a['Age'].mean(mage))
print(c)

df = a.dropna(subset = ['Embarked'])
print(df)

print(a.isnull().sum()/len(a)*100)

print(a.head())

print(a['Embarked'].mode()[0])





