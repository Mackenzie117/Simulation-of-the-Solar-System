import numpy as np
class Particle:
    G = 6.67408e-11
               
            
        
     
    """ A class defining a particle 
    
    Parameters 
    -----------
    position, velocity and acceleration: Array
        These should all be numpy.arrays of length 3 and explicitly converted to type float.
        The value at index 0 should be the x coordinate, index 1 should be the y coordinate, and index 2 
        should be the z coordinate.
        
    name: string
        hold string with a label to identify the particle
    mass: integer
        the mass of the particle
    """
    "This is the 'dunder' method that initialises the object's state, which allocates values to attributes when an instance of the class is created "
    def __init__(    
    self,
    position=np.array([0, 0, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, -10, 0], dtype=float),
    name='Ball',
    mass=1.0,
    KE = 0,
    momentum = 0,
    kineticEnergy = 0,
    potentialEnergy = 0,
    KtotalEnergy = 0,
    PtotalEnergy = 0
    



    ):    
    
     self.position = np.array(position, dtype=float) 
     self.velocity = np.array(velocity, dtype=float)
     self.acceleration = np.array(acceleration, dtype=float)
        
     self.name = name 
     self.mass = mass
        
     self.kineticEnergy = kineticEnergy
     self.momentum = momentum 
     self.potentialEnergy = potentialEnergy
     self.KtotalEnergy = KtotalEnergy
     self.PtotalEnergy = PtotalEnergy

         
    
    
    
    "This is another 'dunder' method that converts the specified values into string that can be called and outputted "
    def __str__(self):
        
         return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
        self.name, self.mass,self.position, self.velocity, self.acceleration
    )
        
    "This method is what updates the gravitational acceleration due to the other bodies using the formula for grvaitational acceleration that takes self and Bodies as arguments "
    
    def updateGravitationalAcceleration(self, Bodies):
        self.acceleration = np.array([0,0,0], dtype=float) #initilises acceleration to be zero before each for loop so each loop starts fresh and doesn't add to acc from previous positions 
        for Body in Bodies: 
            if self.name != Body.name:   # This ensures that the code doesn't calculate the acceleration due to itself as this would give zero         
                m = Body.mass    # assigns the mass in the equation to the mass of the body, as this is the target mass 
                r_vec = self.position - Body.position # calculates the vector of the distance between the bodies 
                r = np.linalg.norm(r_vec)  # calculates the modulus of the distance between each body 
                self.acceleration += ((-self.G*m*r_vec)/(r**3))  # This finds the value of the acceleration using += to endure the acceleration is summed for each body in the list 
    
    def update(self, deltaT, method, Bodies):
        "This method uses the numerical approximations, Euler, EulerCromer and Verlet to update the position and the velocities of the particles in which there are if statements "
        "That dictate which mathmatical lines are ran based on the choice of the method"
        if method == "Euler": 
            self.position  = self.position + self.velocity * deltaT
            self.velocity = self.velocity + self.acceleration * deltaT   

        elif method == "EulerCromer":
             self.velocity += self.acceleration * deltaT
             self.position += self.velocity * deltaT

        else:
            old_Acceleration = self.acceleration
            self.position = self.position + self.velocity * deltaT + 0.5*self.acceleration*deltaT**2
            self.updateGravitationalAcceleration(Bodies)   # for the verlet method the next step acceleration must be calculated to find the velocity 
            self.velocity = self.velocity + 0.5*(self.acceleration+old_Acceleration)*deltaT




      

                
            



   


    def CalcKinetic(self, Bodies):
        "This method calculates the kinetic energy of a body and returns the value self.kineticEnergy, taking self and Bodies as parameters"
        self.kineticEnergy = 0
        v = np.linalg.norm(self.velocity)

        self.kineticEnergy = float(0.5 * self.mass*v**2)

        


    def CalcPotential(self, Bodies):
        """This method calculates the potential energy of a body and returns the value self.potentialEnergy, taking self and Bodies as parameters, for potential one must loop over 
        all the bodies in the list and sums the potential energy due to each body"""
        self.potentialEnergy = 0
        for Body in Bodies:
            if self.name != Body.name:
                m = Body.mass
                r = np.linalg.norm(self.position - Body.position)
                self.potentialEnergy += -(self.G*self.mass*Body.mass)/r # using the equation for potential energy 

        


    
    def Calcmomentum(self, Bodies):
        """This method calculates the momentum of a body, taking self and Bodies as parameters and returns self.momentum """
        v = self.velocity

        self.momentum = self.mass*v



    @staticmethod
    def TotalKinetic(Bodies):
        """This is a static method that takes bodies as a parameter. The purpose of this method is to loop through all the bodies and sum the kinetic energy
        that each body has returning the value of Kinetic_E"""
        Kinetic_E = 0 # initialises kinetic energy to 0 so that the kinetic energies aren't added to the values of the last run of the code 
        
        for Body in Bodies:
            Kinetic_E += Body.kineticEnergy

        

        return(Kinetic_E)


    @staticmethod    
    def TotalPotential(Bodies):
        """This is a static method that takes bodies as a parameter. The purpose of this method is to loop through all the bodies and sum the potential energy
        that each body has returning the value of Potential_E"""
        Potential_E = 0 # initialises potential energy to 0 so that the kinetic energies aren't added to the values of the last run of the code 
        
        for Body in Bodies:
            Potential_E += Body.potentialEnergy

        finalPotential_E = Potential_E *0.5 # this value must be halved as the potential energy for a body has been double counted 

        

        return(finalPotential_E)

    @staticmethod
    def TotalMomentum(Bodies):
        """This is a static method that takes bodies as a parameter. The purpose of this method is to loop through all the bodies and sum the momentum
        that each body has returning the value of FinalMomentum"""
        FinalMomentum= 0
      
        for Body in Bodies:
            FinalMomentum += Body.momentum 
        
        FinalMomentum = np.linalg.norm(FinalMomentum) # this line converts the momentum from a vector to a scalar value 

        return(FinalMomentum)



        



