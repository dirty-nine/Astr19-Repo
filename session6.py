'''
Create a Jupyter Notebook where, in separate cells, you define functions that return sin(x) and cos(x).  Use Markdown cells to comment your Notebook, and describe what each function does. Create a third Python cell that will tabulate sin(x) and cos(x) using these previously defined functions vs. x, where x is tabulated between 0 and 2pi with a thousand entries. Write a fourth Python cell that will use a for loop to print out the first 10 values of x, sin(x), and cos(x) in columns
'''
#tip: use np.transpose() or astropy's Table() to tabulate
#tip: to make the data set with a given range and num entires + evenly spaced out, use np.linspace

#jupyter notebook: https://colab.research.google.com/drive/1M6YtMjsg2r0h6LriQ1qgAsFniWcQQc2A#scrollTo=9acb5395-b3d2-4ab4-83ab-42b687351a5f

#install dependencies
import numpy as np
from astropy.table import Table

#returns the sin of the argument in radians as type numpy.float64
def sin(x):
    return np.sin(x)

#returns the cos of the argument in radians as type numpy.float64
def cos(x):
    return np.cos(x)

# return the entire tabulated list of sin(x) and cos(x) vs. x where x is tabulated between 0 and 2pi with a thousand entries as a Table of columns sinx vs cosx, and x
def tabulatedData1():
    x = np.linspace(0, 2*(np.pi), 1000)
    sinx = sin(x)
    cosx = cos(x)
    dataTable = Table([np.transpose((sinx,cosx)), x], names=['sin(x) vs cos(x)', 'x'])
    return dataTable

# return the entire tabulated list of sin(x) and cos(x) vs. x where x is tabulated between 0 and 2pi with a thousand entries as a Table of columns sinx and cosx and x
def tabulatedData2():
    x = np.linspace(0, 2*np.pi, 1000)
    sinx = sin(x)
    cosx = cos(x)
    dataTable = Table([sinx, cosx, x], names = ["sin(x)", "cos(x)", "x"])
    return dataTable

# return the entire tabulated list of sin(x) and cos(x) vs. x where x is tabulated between 0 and 2pi with a thousand entries as a 2d numpy array of sinx, cosx, and x with 3 columns and 1000 rows
def tabulatedData3():
    x = np.linspace(0, 2*np.pi, 1000)
    sinx, cosx = sin(x), cos(x)
    dataTable = np.transpose((sinx,cosx,x))
    return dataTable

#print the first 10 entries the tabulated data
def printEntries():
    data = tabulatedData3()
    for i in range(0,10):
        print(data[i])

#code executes only if this python file is executed directly
if __name__ == '__main__':
    printEntries()