import numpy as np
from Particle import Particle
from matplotlib import pyplot as plt
from Simulation import filename
from Simulation import KineticEnergyList
from Simulation import PotentialEnergyList
from Simulation import MomentumList
"""In this file the fractional change in the total energy (kinetic + potential) is being plotted and the fractional change in the momentum is being plotted. 
These are both values that should be conserved """


data = np.load(filename, allow_pickle=True)


niter  = len(data) # this sets up the value of how long the loop must run for by taking the length of the list

# the lines from 15 to 25 set up empty lists for the time, and positions of each body that data can be appended to 
t = []



for i in range(0,niter):
    time = data[i][0] # time is the the same in all 3 of the lists so can take it from any of the lists 
    t.append(time)
    

TotalEnergy = [i+j for i,j in zip(KineticEnergyList,PotentialEnergyList)]

Initial = TotalEnergy[0]
frac = []

for i in range(0, len(TotalEnergy)):
    frac_value = abs((TotalEnergy[i]- Initial)/Initial)
    frac.append(frac_value)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_ylabel(r'$|E(t)-E(0)|/E(0)$ ')
ax.set_xlabel(r'$Time$ (s)')
plt.plot(t, frac, label = "Fractional variation in total energy")

ax.legend()

plt.show()

initialM = MomentumList[0]
fracM = []

for i in range(0, len(MomentumList)):
    fracValueM = abs(MomentumList[i]- initialM)/initialM
    fracM.append(fracValueM)


data = np.load(filename, allow_pickle=True)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_ylabel(r'$|p(t)-p(0)|/p(0) $ ')
ax.set_xlabel(r'$Time$ (s)')
plt.plot(t, fracM, label = "Fractional variation of momentum")

ax.legend()
fig.tight_layout()
plt.show()



