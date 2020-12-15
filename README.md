# Understanding changes in the behaviour of the system II

Calculating how the average energy of the system changes with temperatures is an interesting theoretical exercise.  We cannot measure the energy directly, however, so we cannot perform a comparison between the behaviour of our model system of spins and a real physical system.

A quantity that we can measure is the average magnetisation.  Furthermore,  we can calculate the magnetisation of microstate ![](https://render.githubusercontent.com/render/math?math=x_j) using:

![](https://render.githubusercontent.com/render/math?math=M(\mathbf{x}_j)=\sum_{i=1}^Ns_i)

and the average magnetisation using:

![](https://render.githubusercontent.com/render/math?math=\langle\M\rangle=\frac{1}{Z}\sum_{j=1}^{M}M(\mathbf{x}_j)e^{-\beta\H(\mathbf{x}_j)})

where Z is the canonical partition function, ![](https://render.githubusercontent.com/render/math?math=\beta) is the inverse temperature and the sum runs over the M microstates, ![](https://render.githubusercontent.com/render/math?math=\mathbf{x}_j), that the system can adopt.  H, meanwhile, is one of the Hamiltonians that we learned how to compute during the first few of these exercises.  In this particular exercise we are going to use the Hamiltonian for a 2D Ising model in an external magnetic field, H.  Furthermore, we are going to describe the interaction of the spins using the mean field model so the Hamiltonian will be:

![](https://render.githubusercontent.com/render/math?math=E=-\sum_{i=1}^N\left[H-\frac{2D}{N}\sum_{j=1}^Ns_j\right]s_i)

with ![](https://render.githubusercontent.com/render/math?math=D=2) and ![](https://render.githubusercontent.com/render/math?math=N=8).

When you fill in the code in the cell on the left here the function `ensemble_average` should return the value of ![](https://render.githubusercontent.com/render/math?math=\langle\M\rangle) calculated using the formula above.  Within this function you will thus have a write a sum over all the possible microstates.  Notice, furthermore, that this function takes `N` (the number of spins), `H` (the magnetic field strength) and `T` (the temperature) as its input parameters. 

To compute ![](https://render.githubusercontent.com/render/math?math=\langle\M\rangle) you will need to compute the energy for each of the microstates that you generate.  In order to make the code more readable I have written functions called `hamiltonian` and `magnetisation` that will calculate the energy and the magnetisation respectively for microstates using the formulas above.  The function called `hamiltonian` takes the microscopic coordinates for all the spins and the magnetic field strength as its input parameters.  The function called magnetisation, meanwhile, only takes the spin coordinates as input.  These two functions will need to be called for each of the microstates that you generate in the function called ensemble_average.

I have written code that calls your `ensemble_average` function multiple times.  A graph showing how the ensemble average of the magnetisation changes as the strength of the magnetic field is changed and the temperature is held fixed at 5.0 will be plotted once the code has been completed.  
