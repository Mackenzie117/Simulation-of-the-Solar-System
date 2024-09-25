import numpy as np
from Particle import Particle
from matplotlib import pyplot as plt
from Simulation import filename

"""In this file the x and y positions of the bodies are plotted, this can be done for any of the 3 approximation methods by changing the name of the file that is loaded into data"""

# load npy file
# the name of file name can be changed to load different data 
data = np.load(filename, allow_pickle=True)

niter  = len(data) # this sets up the value of how long the loop must run for by taking the length of the list

# the lines from 15 to 25 set up empty lists for the time, and positions of each body that data can be appended to 
t = []
x1 = []     
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []


for i in range(0,niter): # a loop is set up to loop from i = 0  to the amount of data in the list data 

    time = data[i][0]
    t.append(time)
#the lines 33 to 37 define the data values from the list data and assign them the names body1 and so on, essentially pulling the relavent data for each body from the data list each iteration 
    body1 = data[i][1]
    body2 = data[i][2]
    body3 = data[i][3]
    body4 = data[i][4]
    body5 = data[i][5]
#the lines 39 52 append the x and y values for each body for each time steps to the corresponding empty list 
    x1.append(body1.position[0])
    y1.append(body1.position[1])

    x2.append(body2.position[0])
    y2.append(body2.position[1])
    
    x3.append(body3.position[0])
    y3.append(body3.position[1])

    x4.append(body4.position[0])
    y4.append(body4.position[1])

    x5.append(body5.position[0])
    y5.append(body5.position[1])

# the lines 55 to 67 is the code for the plot of the graph where the values of x position is plotted against the values of y positions for each body
fig=plt.figure()
plt.rcParams['font.size'] = '18'
ax=fig.add_subplot(1,1,1)
ax.set_xlabel(r'$X position$ (m)')
ax.set_ylabel(r'$Y position$ (m)')

plt.plot(x1,y1, label = "Sun")
plt.plot(x2,y2, label = "Earth")
plt.plot(x3,y3, label = "Mars")
plt.plot(x4,y4, label = "Jupiter")
plt.plot(x5,y5, label = "Saturn")
ax.legend()

plt.show()