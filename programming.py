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

# nonlocal scope
def name(x):
    name = x
    def upper_name():
        nonlocal name   # uses scope outside a inner function 
        name = name.upper()
        return name
    return upper_name()
    
name('roland')

# return a function & closure (function remembers the state of its enclosing scope when called)
def echo(n):
    """Return the inner_echo function."""
    
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    return inner_echo  # return a function

twice = echo(2)    # remembers n = 2
thrice = echo(3)   # remembers n = 3

print(twice('hello'), thrice('hello'))  

# flexible arguments
def sum_all(*args):
    tmp = 0
    for val in args: 
        tmp += val
    return(tmp)
    
sum_all(1,2,3,4,5)

# keywords arguments
def report_status(**kwargs):
    """Print out the status of a movie character."""
    for key, value in kwargs.items():
        print(key + ": " + value)
report_status(name="luke", affiliation="jedi", status="missing")

# lambda function (anonymous function)
double = (lambda x: x * 2)
double(1)

################################################################################
# Error Handling
################################################################################

# try except
def square(x):
    try:
        y = x ** 2
    except: 
        print("x must be a number")
    return(y)
    
square(2)
square("hello world")

# raise an error message
if x < 0:
    raise ValueError("echo must be greater than 0")
