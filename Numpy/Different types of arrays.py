# Different types of arrays in NumPy
import numpy as np  

#Zeroes array
a = np.zeros((5))
print(a)

#custom dimension of zeroes array
b = np.zeros((4,5))
print(b)

#Ones array
c = np.ones(4)
print(c)

#custom dimension of ones array
d = np.ones((3,5))
print(d)

#Empty array
e = np.empty(4)
print(e)

#custom dimension of empty array
f = np.empty((2,3))
print(f)

#Creating an array using arange() function
g = np.arange(10)
print(g)

#Creating a custom array using arange() 
h = np.arange(1, 10, 2)  # Start at 1, end before 10, step by 2
print(h)

#Creating 2 dimensional array using arange()
j = np.arange(1, 10).reshape(3, 3)  # Reshape to 3x3
print(j)

#Creating an array using linspace() function
i = np.linspace(0, 1, 5)  # Start at 0, end at 1, with 5 evenly spaced values
print(i)

#Creating an identical array using .eye() function
k = np.eye(4)  # Create a 4x4 identity matrix
print(k)


