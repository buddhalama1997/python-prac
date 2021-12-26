class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Buddha",24)

print(p1.name)

print(p1.age)

p1.myFunc()