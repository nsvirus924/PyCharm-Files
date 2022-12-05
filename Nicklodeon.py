# Variables and data types
# Variable data types
# [Numbers(numeric), String, List, Dictionary, Tuple, Set]

# Collections in Python:-
# Module in python =
# [nametuple(), chainmap, deque, counter,
# orderdict, defaultdict, userdict, userlist, userstring]
import random
from collections import defaultdict

a = defaultdict(int)
a[1] = 'python'
a[2] = 'edureka'

print(a)

# Arrays
import array

a = array.array('i', [1, 2, 3, 4, 5, 6])
print(a)

import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6])
print(a)

from array import *

a = array('i', [1, 2, 3, 4, 5, 6])
print(a)

# Accessing array elements
print(a[2])

# Basic array operations
# [1 finding length
# 2adding/change element
# 3 remove/delete elements
# 4 array concatenation
# 5 slicing
# 6 looping through an array]

# 1
import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6])
print(len(a))

# 2 append() Extend() Insert()
import array as arr

b = arr.array('d', [1.1, 2.1, 3.1])
b.append(3.2)
print("array b=", b)

b = arr.array('d', [1.1, 2.1, 3.1])
b.extend([4.5, 3.6, 7.2])
print("array b=", b)

b = arr.array('d', [1.1, 2.1, 3.1])
b.insert(2, 8.8)
print("array b=", b)

# 3 pop() remove()
import array as arr

nik = arr.array('d', [1.1, 2.1, 3.1, 5.5, 9.9, 4.5])
print("Popping last element", nik.pop())
print("Popping 4th element", nik.pop(3))
nik.remove(1.1)
print(nik)

# Array COncatenation(joining)
import array as arr

nik = arr.array('d', [1.1, 2.1, 3.1, 5.5, 9.9, 4.5])
nik2 = arr.array('d', [7.7, 0.5])
c = arr.array('d')
c = nik + nik2
print("array c = ", c)

# Array slicing

a = arr.array('d', [1.1, 2.1, 3.1, 5.5, 9.9, 4.5])
print(a[0:5])

# looping through an array
# 1)for and 2)while

# 1
import array as arr

n = arr.array('d', [1.1, 2.1, 3.1, 5.5, 9.9, 4.5])
print("All values")
for x in n:
    print(x)

# 2
import array as arr

a = arr.array('d', [1.1, 2.1, 3.1, 5.5, 9.9, 4.5])
temp = 0
while temp < len(a):
    print(a[temp])
    temp = temp + 1



# hash table and hashmap
# they are the type of data structures that maps keys to its value pairs
# dictionaries can be created by using curly braces or by using dict() function

my_dict = {'nik': '001', 'mike': '002', 'sam': '003'}
print(my_dict)
type(my_dict)

new_dict = dict()
print(new_dict)

new_dict = dict(nik='001', mike='002')
print(new_dict)

# Nested dictionaries [basically they are the dictionaries
# that lie within the other dictionaries]
emp_details = {'employee': {'dave': {'ID': '001', 'Salary': '2000', 'designation': 'Manager'},
                            'nik': {'ID': '007', 'Salary': '900000', 'designation': 'Manager'}}}

print(emp_details)

# Performing operations on hash table (or dict)
# accessing items
print(my_dict)
print(my_dict.values())
print(my_dict.get('nik'))

# access values using for loop.
for x in my_dict:
    print(x)

for x in my_dict.values():
    print(x)

for x, y in my_dict.items():
    print(x, y)

# updating values of dictionary.
my_dict['mike'] = '004'
my_dict['chris'] = '008'
print(my_dict)

# Delete items from dictionary.
my_dict['ava'] = '000'
print(my_dict)
my_dict.popitem()



# converting a dictionary into a Data Frame.
import pandas as pd
df = pd.DataFrame(emp_details['employee'])
print(df)


#Operators in python.
#{arithmetic
# assignment
# comparison
# logical
# membership
# identity
# bitwise}

#1 arithmetic
x=1
y=4
print(x+y)
# similar for substraction
# exponential(**), division, floordivision(//), modulus(%)



#2 assignment operator (=, +=, -=, *=, %= , **=, //=, |=, ^=, &=)
a=5
a+=5
a**=5
print(a)



#3 Comparison operator
#(equal==, notequal!=, greater than>, less than<,
# greater than or equal>=, less than or equal<=)
val=10
num1=20
compare = val==num1     #similar[!=,>, <, >=, <=]
print(compare)




#4 Logical operators
#logical operators are used to combine conditional statements
#If, elseif(elif), else(3 main conditional statements) discussed below

if val==num1:
    print('equal')
elif val > num1:
    print('greater')
else:
    print('smaller')

#logical operator(and, or, not)
x= 50
print(x>50 and x >25)
print(x>50 or x >25)
print(not(x>5 and x>25))



#5 Identity Operators (compares objects)
list1= [10, 20, 30]
list2= [10,20,30]
x=list1
print(x is list1)
print(list1 is list2)
print(list1 is not list2)




#6 membership operators
#[in and not in]
print(x in list1)
print(10 in list1)
print('apple' in list1)


#7 Bitwise Operators:these are used to compare binary numbers i.e 0 and 1
#{bitwise and &
# bitwise OR |
# bitwise XOR ^
# bitwise not ~
# left shift
# right shift}

print(10&12)
print(10|12)
print(10^12)
print(10<<2)#left shift
print(10>>2) #right shift


## Loops
#[while, for, nested]

#while is used when you don't know how many iterations are required
count = 0
while count < 9:
    print("number:", count)
    count = count + 1
print("good Bye")


#Guessing game:
'''
import random2
n=20
to_be_guessed = int(n * random.random())+1
guess = 0
while guess != to_be_guessed:
    guess = int(input("new number:"))
    if guess > 0:
        if guess > to_be_guessed:
            print("number too large")
        elif guess < to_be_guessed:
            print("number too small")
    else:
        print("sorry that you're giving up!")
        break
else:
    print("congratulation. You made it!")
'''

#For loop:
# [when no. of iteration is known i.e we know the range]
fruits = ['Mango', 'Banana', 'Watermelon']
for fruit in fruits:
    print("Current fruit:", fruit)
print("End")

# Calculate factorial with for loop:
"""
num = int(input("Number:"))
factorial = 1
if num < 0:
    print("must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1, num+1):
     factorial = factorial*i
print(factorial)  
"""

#Nested Loop: Loop inside another loop
'''
#Niks Bank
print("Welcome To Niks Bank")
restart=('Y')
chances=3
balance = 240000
while chances >= 0:
    pin = int(input("Please Enter Your Digit Pin: "))
    if pin == (1234):
        print("You May Proceed\n")
        while restart not in ('n', 'NO','no', 'N'):
            print("Please press 1 to check your balance\n")
            print("Please press 2 for withdrawl\n")
            print("Please press 3 to pay in\n")
            print("Please press 4 to return card\n")
            option = int(input("Choose any of the options to proceed:"))
            if option == 1:
                print("Your balance is Rupees",balance,'\n')
                restart = input("Would you like to go back?")
                if restart in ('n', 'NO','no', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ('Y')
                withdrawl = float(input("Enter amount:"))
                if withdrawl in [100,200,600,800,1000]:
                    balance = balance - withdrawl
                    print("\n Your Balance is Rupees", balance)
                    restart = input("Would you like to go back?")
                    if restart in ('n', 'NO','no', 'N'):
                        print("Thank You \n Visit Again")
                        break
                elif withdrawl != [100,200,600,800,1000]:
                    print("Invalid amount,Please re-try\n")
                    restart = ('Y')
                elif withdrawl==1:
                    withdrawl = float(input("Please enter Desired amount"))

            elif option == 3:
                Pay_in = float(input("Enter Pay In Amount"))
                balance = balance + Pay_in
                print("\n Your balance is Rupees",balance)
                restart = input("Would you like to go back?")
                if restart in ('n', 'NO','no', 'N'):
                    print("Thank You \n Visit Again")
                    break

            elif option == 4:
                print("Please Wait & Collect Your Card.....!!!\n")
                print("Thank You For Visiting Niks Bank")
                break
            else:
                print("Please Enter Correct Number. \n")
                restart = ('Y')
    elif pin != ("1234"):
        print("Incorrect Password")
        chances = chances - 1
        if chances == 0:
            print("Sorry Please Visit Nearest Branch")
            break
'''



#Nested for in for loop:
#pythogorean numbers :-
"""
from math import sqrt
n = int(input("Maximal Number?"))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**a
        c = int(sqrt(c_square))
        if((c_square - c**2) == 0):
            print(a, b, c)
"""


#For loop inside a while loop:
"""
Travelling = input("Yes or No:")
while Travelling == 'Yes':
    num = int(input("Number of people travelling:"))
    for num in range(1, num+1):
        Name = input("Name:")
        Age = input("Age:")
        Sex = input("Male or Female:")
        print(Name)
        print(Age)
        print(Sex)
    Travelling = input("Oops: forgot someone")
"""


#Patterns in python [diamond,pyramids, half- full, triangles,etc]:

#Pyramid
'''
def pattern(n):
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0, i+1):
            print("*", end="")
        print("\n")
pattern(5)
'''

#Inverse pyramid
'''
def pattern(n):
    k = 2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
pattern(5)
'''


#right Start pattern:
'''
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")
    for i in range(n,-1,-1):
        for j in range(n,i+1):
            print("*",end="")
        print("\r")
pattern(10)
'''




''''
# File Handling=
#Types of flies in python(image, test, executable, audio)
#2 types of files (either text or binary)

#Operations on files
#Create--read--update--delete

# 1open function
#example syntax =  open(filename.mode)


import os
file=open("filepath","w")  #'w' represents that we write the file
file.close()

import os
file=open("filepath", "r")  #'r' represents to read file.
print(file.read())
file.close()


import os
file=open("filepath", "r")  #'r' represents to read file.
print(file.read(5))   # here 5 gives the 1st five letters as output
file.close()


#to read only the first line.
import os
file=open("filepath", "r")  #'r' represents to read file.
print(file.readline())
file.close()


#To print all the lines in files.
import os
file=open("filepath", "r")  #'r' represents to read file.
print(file.readlines())    #prints all the lines in text file.
file.close()


#to print limited line.
import os
file=open("filepath", "r")  #'r' represents to read file.
print(file.readline(3))    #prints 3rd line only
file.close()


## Loop over a file object:
#file handling -- for loop
file=open("filepath", "r")
for line in file:
    print(file.readlines())
file.close()

#Python file write method:
#append and write[
# append = 'a' will append to the end of the file
# write = 'w' will overwrite any existing content]

#writing example
import os
file=open("filepath","w")
file.write("hello world")
file.write("hello world again!")
file.close()

# 2nd example:
import os
file=open("filepath","w")
file.write("Oops Overwritten")
file.close()

# 3rd example
import os
file=open("filepath","x") #here x give a new file
file.write("new file")
file.close()

##Delete a file in python:
#os.remove()

#1 del a file
import os
os.remove("abc.txt")

#check if file exists:
import os
if os.path.exists("abc.txt"):
   os.remove("abc.txt")
else:
  print("the file does not exist")

#deleting a folder:
import os
os.rmdir("myfolder") 
'''




### Decorator
#first class objects  &  inner function--->
""""
def function1(name):
    return f"Hello{name}"
def function2(name):
    return f"{name} , how are you?"
def function3(function4):
    return function4(' Dear learner')
print(function3(function1))
print(function3(function2))
"""



# Inner function (i.e function in function):
""""
def func():
    print("first function")
    def func1():
        print("first child function")
    def func2():
        print("second child function")

    func2()
    func1()
func()
"""

# 2nd example:
"""""
def func(n):
    def func1():
        return"Hello world"
    def func2():
        return "Python"
    if n==1:
        return func1
    else:
        return func2
a=func(1)
b=func(2)
print(a())
print(b())
"""

# Decorators in Python:
# [decorators are the design pattern to add new
# functionality to an existing object without modifying its structues.]
"""""
def function1(function):
    def wrapper():
        print("hello")
        function()
        print("Welcome to Python")
    return wrapper
def function2():
    print("Python")

function2 = function1(function2)
function2()
"""""


# Decorators in Python => arguments in decorator function:
""""
def function1(function):
    def wrapper(*args, **kwargs):
        function("hello")
        function(*args, **kwargs)
        print("welcome to python")
    return wrapper
@function1
def function2(name):
    print(f"{name}")

function2("nik")
"""

# function to return values from decorated function:
""""
def function1(function):
    def wrapper(*args, **kwargs):
        print("It worked")
    return wrapper

@function1
def function2(name):
    print(f"{name}")
function2("python")
"""


##Fancy Decorators:
# class decorators, stateful decorators, classes as decorators
"""
class Square:
    def __init__(self,side):
        self.side = side
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self,Value):
        if Value >= 0:
            self._side = Value
        else:
                print("error")
    @property
    def area(self):
        return self._side **2
    @classmethod
    def unit_square(cls):
        return cls(1)
s=Square(5)
print(s.side)
print(s.area)
"""



## Singleton class using class decorators

import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args,**kwargs)
        return wrapper.instance
    wrapper.instance=None
    return wrapper

@singleton
class one:
    pass

first = one()
second = one()

print(first is second)



##Multiple decorators:
#example
''''
import functools
def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num):
                value = func(*args,**kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(num=5)
def function(name):
    print(f"{name}")

function("NsVirus")
'''


## Lambda function
# i.e function that do not have any name (anonyomous)
#these functions we can create wherever needed
#we can take this function as input or an output

#lambda argument:expression
'''''
x= lambda a:a*a
x(3)
print(x)

###
def new(a):
    return a*a
new(3)
print(a)
'''


# Lambda within user defined functions
# Anonymous functions within user defined functions
#(unnamed user defined functions)
def new_func(x):
    return(lambda y:x+y)
t=new_func(3)
u=new_func(2)
print(t(4))
print(u(8))


#Using lambda functions within
# a) filter()  ; b) map()  ; c) reduce()


#a) filter()
# used to filter the given iterables(lists, sets, etc) with the help
# of another function passed as an argument to
# test all the elements to be true or false
my_list=[2,3,4,5,6,7,8]
new_list=list(filter(lambda a:(a/3==2), my_list))    #syntax= filter(function,iterables)
print(new_list)



#b) map() : applies a given function to all the iterables and returns a new list
my_list=[2,3,4,5,6,7,8]
new_list=list(map(lambda a:(a/3!=2), my_list))    #syntax= map(function,iterables)
print(new_list)



#c reduce() : applies some other function to a list of elements
# that are passed as a parameter to it and finally return a single value

from functools import reduce
a=reduce(lambda a,b:a+b, [23,21,45,98])   #reduce(function,sequence)
print(a)



### Solving algebric expressions using lambda
s=(lambda a:(a*a))
print(s(4))

#3x+4y
d=lambda x,y: 3*x+4*y
print(d(4,7))


#quadratic equations
# (a+b)^2
x=lambda a,b: (a+b)**2
print(x(3,4))


##Map-Reduce functions

#map(func,iterables)
def new(a):
    return a*a
x=map(new,[1,2,3,4])
print(list(x))


def new(a):
    return a*a
x=map(new,[1,2,3,4])
print(tuple(x))



#use filter within map
c=map(lambda x:x+x, filter(lambda x:(x>=4),[2,3,4,5]))
print(tuple(c))

#use map function within filter function
d=filter(lambda x:(x>=4), map(lambda x:x+x,[2,3,4,5,6]))
print(set(d))

#use map() and filter() within reduce()
r= reduce(lambda x,y:x+y, map(lambda x:x+x, filter(lambda x: (x<=4),[1,2,3,4,5,6,7])))
print(r)




### Generator
#generators are the functions that return traversable objects
#produce items one at a time and only when required
#are run along with for loops
5:46

