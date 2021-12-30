import json

# python dictionary

x = {
    "name":"Buddha",
    "age" : 24,
    "city": "New York"
}

# convert to JSON:
y = json.dumps(x)

# Result is in a JSON String

print(y)