import numpy as np

a = np.linspace(1,3,3)
print(a)
print(type(a))

b = np.array([1,2,3])


# IMPORTANT: doing x = b makes x a pointer of b

copyA = np.copy(a)
anotherCopyA = np.array(a)
print(copyA)


print(a+b)
print(a@b) # dot product

x = (np.append(a,b))
print(x)

y = np.array([a,b])
print(y)
dimentions = y.shape
print(dimentions) #rows, cols
ndim = y.ndim
print(ndim)

l = np.array([1,2,3,4,5,6])
print(l.reshape(3,2))
