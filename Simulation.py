import numpy as np
from Particle import Particle

import copy
"""  
This file is where instances of the class Particle are created and the values of the class parameters are set, each instance is then added to a list 
called bodies so that the code can loop over each of the planets. In this file the methods from Particle are called and ran for a pre-determined amount of times 
and the values of the class parameters are saved to an npy file.




"""

# All the data for the instances has been taken from https://ssd.jpl.nasa.gov/horizons/app.html#/, the data that the instances have been initialised with 
# was taken on the 4th of December 2022, the values of position and velocity have been multiplied by 1000 to convert to SI units and have been defined in a 
#numpy array with the default value of float

Sun = Particle(
    position = 1000*np.array([-1.357816195258359E+06, 5.200905793268393E+04, 3.120133869179762E+04], dtype = float),
    velocity= 1000*np.array([1.002210169459509E-03, 1.565573469570603E-02, 1.071318791633392E-04], dtype = float),
    acceleration= np.array([0,0,0], dtype = float),
    name="Sun",
    mass=1988500e24,
    kineticEnergy= 1.0,
    potentialEnergy=1.0,
    KtotalEnergy = 0,
    PtotalEnergy = 0

)



Earth = Particle(
    position=1000*np.array([4.546728642223073E+07, 1.398798611122774E+08,2.386761424028873E+04 ], dtype = float),
    velocity=1000*np.array([-2.872495143314737E+01, 9.320010671742638E+00, -1.273581081820296E-03], dtype = float),
    acceleration=np.array([0, 0, 0], dtype = float),
    name="Earth",
    mass=5.97219e24 ,
    kineticEnergy = 1.0,
    potentialEnergy = 1.0,
    KtotalEnergy = 0,
    PtotalEnergy = 0
   
 

)
   

    



  
Mars = Particle(
    position=1000*np.array([6.323285528848249E+07, 2.194420058839689E+08, 3.044834159864873E+06]), 
    velocity=1000*np.array([-2.232386819715174E+01,8.888265001021862E+00,7.343354496774612E-01]),
    acceleration=np.array([0, 0, 0]),
    name="Mars",
    mass=6.4171e23,
    kineticEnergy= 1.0,
    potentialEnergy=1.0,
    KtotalEnergy = 0,
    PtotalEnergy = 0
    
)



Saturn = Particle(
    position=1000*np.array([1.205544208531313E+09,-8.427502573535767E+08,-3.334489390102422E+07]), 
    velocity=1000*np.array([4.994018957261532E+00,7.899322738126773E+00,-3.367332481371630E-01]),
    acceleration=np.array([0, 0, 0]),
    name="Saturn",
    mass=5.6834e26,
    kineticEnergy= 1.0,
    potentialEnergy=1.0,
    KtotalEnergy = 0,
    PtotalEnergy = 0
    
    )

Jupiter = Particle(
    position=1000*np.array([7.287862698816487E+08,1.238640510115427E+08,-1.681876772934382E+07]), 
    velocity=1000*np.array([-2.339531922889663E+00, 1.349364477507025E+01 , -3.686118859435261E-03]),
    acceleration=np.array([0, 0, 0]),
    name="Jupiter",
    mass=1.89865e27,
    kineticEnergy= 1.0,
    potentialEnergy=1.0,
    KtotalEnergy = 0,
    PtotalEnergy = 0
    
    )


Bodies = [Sun, Earth, Mars, Jupiter, Saturn]  # this list is created to store the names of the bodies to that the code can loop over each body and so that the methods 
#are generalised for n bodies 





deltaT = 3600 *24  # This is the value of the time step between each iteration for calculating all the values which is set to one day in seconds
tend = 365 * 24 * 3600*(1) # This is the value of time at which the code will stop running the value outside the brackets is the amount of seconds in a year, it can be scaled by changing the value in the brakets 
Ttotal = int(tend/deltaT) # This determines how many iterations there will be 




method = "EulerCromer" 

if method == "Euler":
    filename = "my_test_E.npy"

elif method == "EulerCromer":
    filename = "my_test_EC.npy"

else:
    filename = "my_test_V.npy"



DataE = []
KineticEnergyList = []
PotentialEnergyList = []
MomentumList =[]


#These lists are created here so that the loop can append values to them during the for loop for the final total kinetic and potential energies and momentum 

"""this for loops runs for the amount of time determined in line 106 and calls the class methods defined in Particle it loops over each body in the bodies list for each 
call of the class methods, it has an if statement that appends the time and instances of the classes to a list for each iteration but the vlaue can be changed 
by changing the value after the modulus operatio, it creates a deepcopy for each body in the list  after the loop has finished the list is then saved as an npy file """

for i in range(0,Ttotal):
    for body in Bodies:
        body.updateGravitationalAcceleration(Bodies)

    for body in Bodies:
        body.update(deltaT, method, Bodies)

    for body in Bodies:
        body.CalcKinetic(Bodies)

    for body in Bodies:
        body.CalcPotential(Bodies)
    
    for body in Bodies:
        body.Calcmomentum(Bodies)
    
    """The following if statements save the kinetic energy, potential energy and momentum for each different approximation method 
    this is done so that total fractional energy chan ge can be plotted on the same graph for the three different methods """
    
    FinalKineticEnergy = Particle.TotalKinetic(Bodies)
    KineticEnergyList.append(FinalKineticEnergy)
    
    FinalPotentialEnergy = Particle.TotalPotential(Bodies)
    PotentialEnergyList.append(FinalPotentialEnergy)
        
    
    FinalMomentum = Particle.TotalMomentum(Bodies)
    MomentumList.append(FinalMomentum)

    


    if i %1 ==  0:
        temp_list = [deltaT*(i+1)]
        for Body in Bodies:
            temp_list.append(copy.deepcopy(Body))
            
        DataE.append(temp_list)
        

np.save(filename,DataE, allow_pickle = True) # this is the final npy file that has all the data for each body saved to it 


    

