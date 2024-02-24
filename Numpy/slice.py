import numpy as np  # numeric python

np1 = np.arange(0, 30, 2)
print(np1[5:])
print(np1[::3])


np2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np2)
print(np2[1, 2])
print(np2[0:2, 2])
