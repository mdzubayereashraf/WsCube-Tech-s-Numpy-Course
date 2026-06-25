import numpy as np 

arr1 = np.array([1,2,3,4])
arr2 = np.array([4,5,6,7])

additon = arr1 + arr2
subtruction = arr2 - arr1
print(additon)
print(subtruction)


#Statistical operations
print(np.mean(additon))
print(np.var(additon))
print(np.std(additon))
print(np.min(additon))
print(np.max(additon))

