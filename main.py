import matplotlib.pyplot as plt
import numpy as np

def hamiltonian( spins, H ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  avspins = sum(spins)/len(spins) 
  for i in range(len(spins)) : energy = energy - (4*avspins+H)*spins[i] 
  return energy
  
def magnetisation( spins ) : 
  mag = 0 
  # Your code to calculate the magnetisation goes here
  mag = sum(spins)
  return mag
  
def ensemble_average( N, H, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the partition function goes here
  spins = np.zeros(N)
  for index in range(2**N) :
      for i in range(N) :
          spins[i] = np.floor( index / 2**(N-1-i) )
          index = index - spins[i]*(2**(N-1-i))
          if spins[i]==0 : spins[i] = -1
      energy = hamiltonian(spins, H)
      bweight = np.exp( -energy / T )
      numerator = numerator + magnetisation(spins)*bweight
      Z = Z + bweight
  return numerator / Z
  
magnetisations = []
fields = np.linspace(-2,2,20)
for field in fields : magnetisations.append( ensemble_average(8, field, 5.0) )
plt.plot( fields, magnetisations, 'k-' )
plt.xlabel("magnetic field strength / J")
plt.ylabel("average magnetisation")
plt.savefig("average_magntisation.png")
