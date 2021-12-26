# Create a class MyNumber
class MyNumbers:
    # defining iteration method
    def __iter__(self):
        self.a = 1
        return self
    # defining next method 
    def __next__(self):
        x = self.a
        self.a += 1
        return x

# Creating myclassmethod
myclass = MyNumbers()
# Calling iteration method
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))