# matplotlib output to be plotted inside the notebook
%matplotlib inline

# import libs
import pandas as pd
import matplotlib.pyplot as plt

# histogram
age = [18,18,20,23,21,19,19,19,22,22,19,20,24,23,20,20,21]
data = pd.DataFrame({'age': age})
data['age'].plot(kind='hist', title="age", bins=5)
