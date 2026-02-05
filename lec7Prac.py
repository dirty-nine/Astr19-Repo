import numpy as np
import matplotlib as plt
# %matplotlib inline
n = 100
x = np.linspace(-np.pi, np.pi, n)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.savefig('sinx.png', bbox_inches='tight', dpi=600)
plt.show()
