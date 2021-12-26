# Practice for local scope
# A varible is created inside the function and cannot be access ouside of the function
def myFunc():
    x= 300 #local scope
    print(x)

myFunc()

#Function inside Function
# THe local variable can be accessed from a fnction within a function

def func():
    x=300
    def myInnerFunc():
        print(x)
    myInnerFunc()

func()


# global scope
# A varible is created outside of the function and can be accessed by anyone

a = 200
def funct():
    print(a)
funct()

print(a)
