################################################################################
# Variable types
################################################################################

str(0)        # convert into string
int('0')      # convert into integer
float(0)      # convert into float
bool(0)       # convert into boolean

# get type (str, int, float, bool, ...)
type("hello")       

################################################################################
# Dictionary (key - value pairs, keys need to be unique)
################################################################################

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe["germany"] = "berlin"

# New element
europe["hungary"] = "budapest"

# Remove australia
del(europe["australia"])

# Print europe
print(europe)

################################################################################
# Tupels (immutable lists)
################################################################################

point = (1, 2, 3)
x, y, z = point

################################################################################
# List vs numpy array
################################################################################

# default behavior
a = [1, 2, 3, 4, 5]
b = a + a
print(b)  # result [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# numpy
import numpy as np
a = np.array([1,2,3,4,5])
b = a + a
print(b) # result [ 2  4  6  8 10]
