import numpy as np #import numpy to create arrays
from tabulate import tabulate #python built-in package to make tables
from astropy.table import Table #make tables using astropy

# Generate an array of x and y values
x = np.linspace(-2.0, 2.0, 10)  # Generate 10 values from -2 to +2 regularly spaced
y = x**2 #compute y-values from x-values using y = x^2

#Tables using tabulate
# Create a list of tuples containing x and y values
table_data = [(a, b) for a, b in zip(x, y)]

# Print the table using tabulate
table_headers = ["x", "y"]
python_table = tabulate(table_data, tablefmt="grid", headers=table_headers, floatfmt=".3f")

#Tables using astropy
# Create an Astropy Table
astropy_table = Table()         #create empty astropy table
astropy_table["x"] = x          #make axis with key "x" and values of X
astropy_table["y"] = y          #make axis with key "y" and values of X

# Format specifiers
astropy_table["x"].format = "{:.3f}"
astropy_table["y"].format = "{:.3f}"

#main program that will be exectued only when this file is run
def main():
    print(table_data) #quick look into the inside of table_data
    print(python_table) #show the python table
    print(astropy_table) #show the astropy table

if __name__=='__main__':
    main()



