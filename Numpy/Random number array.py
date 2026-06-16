# Creating a random number array between 0 to 1
import numpy as np

var1 = np.random.rand(4) # for one dimensional array with 4 random numbers
print(var1) 

var2 = np.random.rand(3, 4) # for two dimensional array with 3 rows and 4 columns
print(var2)

var3 = np.random.rand(2, 3, 4) # for three dimensional array with 2 blocks, 3 rows and 4 columns
print(var3)