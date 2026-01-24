'''Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2pi with a thousand entries. Follow the basic Python program structure, including a main program function'''

import numpy as np
from astropy.table import Table

def main():
    x = np.linspace(0, np.pi, 1000)
    sinx = np.sin(x)    
    #print(np.transpose((sinx, x)))

    data = Table([sinx, x], names=['sin(x)', 'x'])
    print(data)

if __name__ == "__main__":
    main()