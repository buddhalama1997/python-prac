# creating simple function

def myFunction():
    print("Hello Everyone!!")


# calling the myFunction()
myFunction()


# function for printing first name
def my_function(fname):
    print(fname + " Lama")

# invoking my_function
my_function("Buddha")

# Default parameter Value Function
def myFunc(country ="Nepal"):
    print("I am From " + country)

# replace the default value
myFunc("Germany")

# return default value
myFunc()

# function with multiple arguments
def multiArgument(firstname, lastname):
    print(firstname + " " + lastname)

# passing parameters in a function
multiArgument("Buddha","Lama")

#Function with Arbitary Arguments or number of argument is unknown

def my(*kids):
    print("The Youngest chid is "+ kids[-1])

my("Ram","Hari","Susan")