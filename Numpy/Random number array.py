# Creating a random number array between 0 to 1
import numpy as np

var1 = np.random.rand(4) # for one dimensional array with 4 random numbers
print(var1) 

var2 = np.random.rand(3, 4) # for two dimensional array with 3 rows and 4 columns
print(var2)

var3 = np.random.rand(2, 3, 4) # for three dimensional array with 2 blocks, 3 rows and 4 columns
print(var3)

#Creating a random number array between 0 to 10
var4 = np.random.rand(4) * 10            
print(var4)

#Creating a random number array close to 0
var5 = np.random.randn(4)
print(var5)

#creating a random number array close to zero
var6 = np.random.randn(5, 6)
print(var6)

#crating a random number array between 0 and 10 with 3 rows and 4 columns
var8 = np.random.randint(0, 10, size=(3, 4))
print(var8)

#crating a random number array between 0 and 10 with 3 rows and 4 columns
var9 = np.random.randint(0, 10, 6).reshape(3, 2)
print(var9)