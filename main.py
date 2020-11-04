import matplotlib.pyplot as plt
import numpy as np

def hamiltonian( spins, H ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  
  return energy
  
def magnetisation( spins ) : 
  mag = 0 
  # Your code to calculate the magnetisation goes here
  
  return mag
  
def ensemble_average( N, H, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the partition function goes here
  
  return numerator / Z
  
magnetisations = []
fields = np.linspace(-2,2,20)
for field in fields : magnetisations.append( ensemble_average(8, field, 5.0) )
plt.plot( fields, magnetisations, 'k-' )
plt.xlabel("magnetic field strength / J")
plt.ylabel("average magnetisation")
plt.savefig("average_magntisation.png")
