################################################################################
# Types
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

# Remove australia
del(europe["australia"])

# Print europe
print(europe)

################################################################################
# Pandas DataFrame 
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


### select columns

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


