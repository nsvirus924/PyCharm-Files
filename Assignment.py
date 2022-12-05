"""""
from statsmodels.sandbox.stats.runs import runstest_1samp

#create dataset
data=[12, 16, 16, 15, 14, 18, 19, 21, 13, 13]
#performing run test
x=runstest_1samp(data, correction=False)
print(x)
"""""



import random
import numpy as np
import matplotlib.pyplot as plt
mylist=[]
for i in range(0,10000):
    casino=random.randint(0,36)
    mylist.append(casino)
print(mylist)
plt.bar(mylist,casino)
plt.show()



#auto correlation
import pandas as pd
import statsmodels.api as spi
nik = spi.tsa.acf(casino)
#print(nik)
#n=pd.plotting.autocorrelation_plot(nik)
#plt.show()



def gap_test(casino):
    pass
gap_test(casino)








""""
from scipy.stats import chisquare
observed=[315,101,108,32]
expected=[0.5625,0.1875,0.1875,0.0625]
a=chisquare(observed,axis=None)
b=chisquare(expected,axis=None)
print(a,'\n',b)
""


""
from statsmodels.sandbox.stats.runs import runstest_1samp
import random
data= randomlist = []
for i in range(0,10000):
 casino = random.randint(0,36)

casino=data
n=runstest_1samp(casino, correction=False)
print(n)
"""""


"""""
from numpy.random import seed
from numpy.random import poisson
from scipy.stats import kstest
#set seed
seed(0)
#generate dataset of 100 values that follow a Poisson distribution with mean=5
data = poisson(5,100)
print(data)
#perform Kolmogorov-Smirnov test
x=kstest(data, 'norm')
print(x)
"""