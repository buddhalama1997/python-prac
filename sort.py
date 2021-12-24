friuts =["orange","mango","kiwi","pineapple", "banana"]
#friuts.sort() #ascending order
friuts.sort(reverse=True) #descending order 
print(friuts)

num =[100,50,65,82,23]
#ascending order
#num.sort()

#descending order
num.sort(reverse=True)
print(num)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
