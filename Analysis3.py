import numpy as np
from Particle import Particle



"This file calculates the absolute difference in the position of where the Earth will be in a years time and where the approximations predict the Earth will be."
 

EarthFinalPositionReal = np.array([4.625017439537078E+07,1.392111211047499E+08,2.322824967406690E+04], dtype=float) # The position of the Earth in a years time from 4th of December 

"These next few lines assign the values of the npy files to the relevant variables to have access to all of the npy files  "
dataE = np.load("my_test_E.npy", allow_pickle=True)
dataEC = np.load("my_test_EC.npy", allow_pickle=True)
dataV = np.load("my_test_V.npy", allow_pickle=True)
niter  = len(dataE)



  
#the lines 20 to 23 define the data values from the list data and assign them the names body1 and so on, essentially pulling the relavent data for each body from the data list each iteration 
body1E = dataE[niter-1][2]
body1EC = dataE[niter-1][2]
body1V = dataE[niter-1][2]

print(body1E)
percent_diffE = abs(body1E.position - EarthFinalPositionReal)
print ("The difference in x position of the earth from Euler method is given by: " , percent_diffE)


body1EC = dataEC[niter-1][2]
percent_diffEC = abs(body1EC.position - EarthFinalPositionReal)
print ("The difference in y position of the earth from Euler-Cromer method is given by: " ,  percent_diffEC)

body1V = dataV[niter-1][2]
percent_diffV = abs(body1V.position - EarthFinalPositionReal)
print ("The difference in z position of the earth from Verlet method is given by: " ,  percent_diffV)