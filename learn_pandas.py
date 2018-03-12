################################################################################
# Create Pandas DataFrame
################################################################################

### create DataFrame from dictionary

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)


### create DataFrame from csv file

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("cars.csv")

# Print out cars
print(cars)

# import data with tab as seperator and "?" as na value
data = pd.read_csv("data.csv", sep = "\t", na_values = ["?"])

################################################################################
# Select columns
################################################################################

# Print out country column as Pandas Series
cars["country"]

# Print out country column as Pandas DataFrame
cars[["country"]]

# Print out DataFrame with country and drives_right columns
cars[["country", "drives_right"]]

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])
