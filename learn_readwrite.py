################################################################################
# read a text-file
################################################################################

file = open('data.txt', 'r')
print(file.read())
file.close()
print(file.closed)   # is file closed?

################################################################################
# read a text-file using numpy
################################################################################

# read numerical data
import numpy as np
data = np.loadtxt('input.csv', delimiter=',', skip=0)  

# mixed type data
import numpy as np
data = np.recfromcsv(file)

