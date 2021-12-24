list1 = ["a","b","c","d","e"]
list2 =[1,2,3,4,5]

list3 = list1 + list2

print(list3)

for x in list2:
    list1.append(x)

print(list1)

list1.extend(list2)
print(list1)

list2.reverse()

print(list2)