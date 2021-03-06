################################################################################
# working directory & files
################################################################################

import os
wd = os.getcwd()
os.listdir(wd)

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

# tab seperated, comment, na values
data = pd.read_csv(file, sep='\t', comment='#', na_values=['NULL', '?'])

################################################################################
# pickle (binary data)
################################################################################

with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

################################################################################
# read excel file
################################################################################

import pandas as pd
file = 'import.xlsx'
xl = pd.ExcelFile(file)
print(xl.sheet_names)
df1 = xl.parse('sheet1')     # import sheet1 as a pandas dataframe
print(df1.head())

################################################################################
# read SAS file
################################################################################

from sas7bdat import SAS7BDAT
with SAS7BDAT('import.sas7bdat') as file:
    df_sas = file.to_data_frame()
print(df_sas.head)

