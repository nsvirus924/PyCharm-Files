#matplotlib

from matplotlib import pyplot as plt
plt.plot([1,2,3],[54,21,12])
plt.show()


#add lables to plot
x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('Info')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.show()


#add colur to plot
from matplotlib import style
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g',label='line two',linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)

plt.title('Epic Info')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.legend()
plt.grid(True,color='red')
plt.show()



#Bar graph in matplotlib
import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2],label="Example one")

plt.bar([2,4,6,8,10],[8,6,2,5,6],label="Example two",color='g')
plt.legend()
plt.xlabel("Bar number")
plt.ylabel("Bar height")
plt.title("Info")
plt.show()


# plot Histogram matplotlib
import matplotlib.pyplot as plt
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,80,75,65,54,44,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
#plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Histogram")
plt.legend()
plt.show()



#Scatter plot
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='skitcat',color='k')

plt.xlabel("x")
plt.ylabel("y")
plt.title('Scatter Plot')
plt.legend()
plt.show()



# area plot
import matplotlib.pyplot as plt
days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color='m',label='Sleeping',linewidth=5)
plt.plot([],[],color='c',label='Eating',linewidth=5)
plt.plot([],[],color='r',label='Working',linewidth=5)
plt.plot([],[],color='k',label='Playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])
plt.xlabel("x")
plt.ylabel("y")
plt.title('Area Plot')
plt.legend()
plt.show()



#Pie plot
import matplotlib.pyplot as plt

Slices = [7,2,2,13]
Activities = ['Sleeping','Eating','Working','Playing']
cols = ['m','c','r','b']
plt.pie(Slices,labels=Activities,colors=cols,startangle=90,shadow=True,explode=(0,0.3,0,0),autopct='%1.1f%%')
plt.title('Pie Plot')
plt.show()




#working with multiple plots
import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()