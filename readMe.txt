Particle.py - Particle class containing methods to update the gravitational acceleration and advance the system, 
it also contains methods that claculate the energies and the momentum it requires numpy

Simualtion.py - main simulation file where instances of the class Particle are created, bodies are advanced and results are saved. 
To change the approximation method alter line 111 to the desired method. 
To change the total time ran for alter line 105

Analysis.py - Post-processing script to plot the orbits. Requires matplotlib.

Analysis2.py - Post-processing script to plot the fractional energy
anbd the fractional momentum change. Requires matplotlib.

Analysis3.py - Post-processing script to find the absolute difference in the po
position of the earth after a year. Requires the time in simulation line 105 to be a year Requires matplotlib.