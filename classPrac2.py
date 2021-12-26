# Create class Person
class Person:
    # create main method
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    # create a method for printing his name
    def myFunc(self):
        print("Hello my name is " + self.name)

# create a objects for setting name and age
p1 = Person("Buddha",24)

# printing name
print(p1.name)

# printing age
print(p1.age)

# calling for function
p1.myFunc()

# Modifying object parameters

p1.age ="25"

# deleting object properties
del p1.age

# deleting object
del p1

