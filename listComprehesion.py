friuts =["apple","banana","cherry","kiwi","mango"]

newList =[]

for x in friuts:
    if "a" in x:
        newList.append(x.upper())

list=[x if x !="banana" else "orange" for x in friuts]
print(list)

# shorter form

newLists = [x for x in friuts if "a" in x]

print(newLists)

new = [x for x in friuts if x !="apple"]

print(new)

friut = [x for x in friuts]

print(friut)

falful = [x for x in range(10)]

print(falful)

num = [x for x in range(10) if x < 5]
print(num)

upper = [x.upper() for x in friuts]
print(upper)