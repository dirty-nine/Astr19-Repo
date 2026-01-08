import numpy as np

i = 10
n_a = np.zeros(i, dtype=int)
print(n_a) # print 0 i times
print(type(n_a)) # prints the n_a's type: ndarray
print(type(n_a[0]))#prints type of first element in n_a, 0, which is int64 (not int for some reason)
