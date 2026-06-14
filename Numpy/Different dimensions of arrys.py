import numpy as np  

# Create a 1D array
a = np.array([1, 2, 3, 4, 5])
print(a)    
print(a.ndim)  # Number of dimensions
print(a.shape)  # Shape of the array
# Create a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)    
print(b.ndim)  # Number of dimensions
print(b.shape)  # Shape of the array
# Create a 3D array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)    
print(c.ndim)  # Number of dimensions
print(c.shape)  # Shape of the array

# Create a multidimensional array
d = np.array([1, 2, 3], ndmin=10)
print(d)
print(d.ndim)  # Number of dimensions
print(d.shape)  # Shape of the array
