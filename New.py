"""""
import pywhatkit
from pywhatkit.remotekit import start_server
from datetime import datetime
from flask import Flask, request
now = datetime.now()

chour = now.strftime("%H")
mobile = input('Enter Mobile No of Receiver : ')
message = input('Enter Message you wanna send : ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(mobile,message,hour,minute)
"""


import pandas as pd
import numpy as np
#data=pd.read_csv(r'D:\abc.csv')
#print(data)
#data.head(10)


#code to open file directly from any where
from tkinter import filedialog as fd
#filename = fd.askopenfilename()












#Generate random numbers
#6 Digit random number
from random import randint
#for i in range (6):
#    print(randint(0,9),end='')



#4 Digit random number
#from random import randint
#for i in range (4):
#    print(randint(0,9),end='')


#ERP Number Starting with letter S
#from random import randint
#for i in range (3):
#    print("S1132210",randint(0,9),'\n',end='',sep='')



# Erp number
import random as r

erp = ["S1132210"]

# the first number should be in the range of 6 to 9
erp.append(r.randint(8, 9))

# the for loop is used to append the other 9 numbers.
# the other 9 numbers can be in the range of 0 to 9.
for i in range(2):
    erp.append(r.randint(0, 9))

# printing the number
for i in erp:
     print(i,end='')
'''

'''''
#Vehicle number
from random import randint
Kolhapur_passing= ["MH-09-NS-"]

# the for loop is used to append the other 9 numbers.
# the other 9 numbers can be in the range of 0 to 9.
for i in range(0, 4):
    Kolhapur_passing.append(randint(0, 9))

# printing the number
for i in Kolhapur_passing:
     print(i,end='')
'''
'''''
#Pan card number
pan = ["ABCDE"]

# the first number should be in the range of 0 to 2
pan.append(randint(0, 2))

# the for loop is used to append the other 9 numbers.
# the other 9 numbers can be in the range of 0 to 9.
for i in range(0, 4):
    pan.append(randint(0, 9))
# printing the number
for i in pan:
     print(i,end='')
'''

'''''
#License number generator
# import module
import random as r

L_no = ["MH09 2017"]

# the first number should be in the range of 6 to 9
L_no.append(r.randint(8, 9))

# the for loop is used to append the other 9 numbers.
# the other 9 numbers can be in the range of 0 to 9.
for i in range(6):
    L_no.append(r.randint(0, 9))

# printing the number
for i in L_no:
     print(i,end='')



from random import randint
r1=[]
for i in range (4):
    print(randint(0,9),end='',sep='')
r2=[]
for j in range (4):
    print(randint(0,9),end='',sep='')
r3=[]
for e in range (4):
    print(randint(0,9),end='',sep='')
r4=[]
for n in range (4):
    print(randint(0,9),end='',sep='')




from  random import randint
DL_No= ["6522-56"]


for i in range(0, 10):
   DL_No.append(randint(0, 9))

for i in DL_No:
     print(i,end='')
'''


'''''
#Adhar Number
import random as r

Adhar = []

# the first number of adhar card are from 2 to 9
Adhar.append(r.randint(2, 9))

# the for loop is used to append the other 11 numbers.
# the other 9 numbers can be in the range of 0 to 9.
for i in range(11):
    Adhar.append(r.randint(0, 9))

# printing the number
for i in Adhar:
     print(i,end='')



import random
randomlist = []
#for i in range(0,5):
#   n = random.randint(1,30)
#    randomlist.append(n)
#print(randomlist)




import pandas as pd
a =pd.read_csv('path')
print(a)


####choose dataset from files directly################
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)


"""""
#Cleaning the data
import pandas as pd
import numpy as np
data = pd.read_csv('dataset.csv')
data.isnull()  # getting null values
data.isnull().sum()
#now we start to drop the data i.e clean it
remove = ['abc ','xyz']
data.drop(remove, inplace =True, axis =1)
data.duplicated()
data.drop_duplicates()
#remove outliers
data['abc'].describe()
data.loc[10,'Rating'] = 1 #mention row number and column name


import seaborn as sns
df = sns.load_dataset("D:/tips.csv")
print(df)
"""""