import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_magnetisation(self) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            self.assertTrue( magnetisation(spins)==sum(spins), "your function for calculating the magnetisation is not working correctly" )
            
    def test_ensemble_average(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        numer, pfunc = len(fields)*[0], len(fields)*[0]
        for i in range(2**8) :
            num, spins = i, 8*[0]
            for j in range(8) :
               spins[j] = np.floor( num / 2**(7-j) )
               num = num - spins[j]*2**(7-j)
               if spins[j]==0 : spins[j] = -1
            mag = sum(spins)
            for k in range(len(fields)) :
               eee = hamiltonian( spins, fields[k] )
               numer[k] = numer[k] + mag*np.exp( -eee / 5.0 )
               pfunc[k] = pfunc[k] + np.exp( -eee / 5.0 )
            for k in range(len(fields)) :
                self.assertTrue( np.abs( fields[k] - this_x[k])<1e-7, "The function for computing the ensemble average is wrong" )
                self.assertTrue( np.abs( numer[k]/pfunc[k] - this_y[k])<1e-7, "The function for computing the ensemble average is wrong" )
                
    def test_hamiltonian(self) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            meanspin = sumspins / len(spins)
            self.assertTrue( np.abs(hamiltonian( spins, 1)+(1+4*meanspin)*sumspins)<1e-7, "The function that you have written for the Hamiltonian does not calculate the correct energy" )
            self.assertTrue( np.abs(hamiltonian( spins, -1)+(-1+4*meanspin)*sumspins)<1e-7, "The function that you have written for the Hamiltonian does not calculate the correct energy" )
            self.assertTrue( np.abs(hamiltonian( spins, 0 )+(4*meanspin)*sumspins)<1e-7, "The function that you have written for the Hamiltonian does not calculate the correct energy" )
            self.assertTrue( np.abs(hamiltonian( spins, 2)+(2+4*meanspin)*sumspins)<1e-7, "The function that you have written for the Hamiltonian does not calculate the correct energy" )
