# Creting main class Person
class Person:
    def __init__ (self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)


# create a child class student inherite the property of Person Class

class Student(Person):
    pass

# create a object x and store the lname and fname

x = Student("Buddha","Lama")

# invoking the print name method
x.printname()