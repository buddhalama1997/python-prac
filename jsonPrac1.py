import json

# some json

x = '{"name":"John", "age": 30, "city":"New York"}'

# parse x:
y = json.loads(x)

#result is in python dictionary
print(y["age"])


print(y)