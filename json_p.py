import json

# some JSON <JavaScript Object Notation>

x = '{"name": "John", "age": 30, "city": "New York"}'

# parse x
y = json.loads(x)

# the reuslt is a python dictionary

print(type(x))
print(type(y))
#for i,j in y.items():
#    print(i, j)


# convert from python to json

# dictionary
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON
y = json.dumps(x)
print(x)
print(y)
