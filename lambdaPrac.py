# create a lamba function for addition
x = lambda a : a + 10

# return the vaue of lambda function
print(x(5))

#multiply argument a and b and return a result

y = lambda a,b : a*b
print(y(3,4))

# summarize the argument a,b, and c and return a result

z = lambda a, b, c : a + b + c
print(z(1,2,3))

# using lambda function
def myFunc(n):
    return lambda a: a*n

mydoubler = myFunc(2)

print(mydoubler(10))

mytrippler = myFunc(3)

print(mytrippler(10))

