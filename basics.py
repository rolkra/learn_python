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
# Operators
################################################################################

# comparsion operator
1 >= 0
0 <= 1
1 == 1
1 != 0
1 <> 0

# Exponent
2 ** 2    # 2^2

# boolean operator
True and True
True or False
not False

# boolean operator for np.array
a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])
np.logical_and(a < 4, b < 4)
np.logical_or(a < 4, b < 4)

################################################################################
# Control flow
################################################################################

# if, elif, else
a = 10
if a > 10 :
    print("a > 10")
elif a >= 5 :
    print("a between 5 and 10")
else :
    print("a < 5")

a = 10
b = True if a == 10 else False
print(b)

# while
a = 5
while a > 0 :
    print(a)
    a = a - 1

# for
a = [1,2,3,4,5]
for i in a :
    print(i)
    
a = [1,2,3,4,5]
for index, element in enumerate(a) :
    print("nr " + str(index) + " = " + str(element))
    
# for (dictionary)
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
for country, capital in europe.items() :
    print("the capital of ", country, " is ", capital)
        
################################################################################
# Function & Scope
################################################################################

# define a function
def double(x):
    """doubles x"""
    return x*2

double(2)

# global scope
name = "bruce"

def change_name() :
    global name
    name = "rick"

print(name)
change_name()
print(name)

# inner function (function inside a function)
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings concatenated with '!!!'."""
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    return (inner(word1), inner(word2), inner(word3))
print(three_shouts('a', 'b', 'c'))

################################################################################
# String
################################################################################
        
a = "Hello World"
a.upper()
a.lower()
len(a)

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
