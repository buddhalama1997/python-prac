family =["Buddha","Suntali","Dawa","Hira"]

for x in family:
    print(x + ' is one of the family member.')

for i in range(len(family)):
    print(family[i]+" is one of the family member.")

#initizaling the value of x


x=0
# Implementation of while loop for getting the each element of the list.
while x < len(family):
    print (family[x]+ " is one of the family member.")
    x = x + 1

[print(x +" is one of the member of family.") for x in family]
