################################################################################
# read a text-file
################################################################################

file = open('data.txt', 'r')
print(file.read())
file.close()
print(file.closed)   # is file closed?

################################################################################
# numpy
################################################################################

# read numerical data
import numpy as np
data = np.loadtxt('input.csv', delimiter=',', skip=0)  

# mixed type data
import numpy as np
data = np.recfromcsv(file)

################################################################################
# pandas
################################################################################

import pandas as pd
file = 'titanic.csv'
df = pd.read_csv(file)
df.head()

# no header, first 5 rows
data = pd.read_csv(file, nrows=5, header=None)
