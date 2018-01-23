# matplotlib output to be plotted inside the notebook
%matplotlib inline

# import libs
import pandas as pd
import matplotlib.pyplot as plt

# create dataframe
age = [18,18,20,23,21,19,19,19,22,22]
gender = ["M","M","F","M","M","F","F","F","F","M"]
churn = [True, True, False, False, False, False, True, False, False, True]
data = pd.DataFrame({'age': age, 'gender': gender, 'churn': churn})

# histogram 
data['age'].plot(kind='hist', title="age", bins=5)
plt.hist(data['age'].dropna())    # na in hist throws an error

# barchart
data['gender'].value_counts().plot(kind='barh', title="gender")
data['churn'].value_counts().plot(kind='barh', title="churn")

