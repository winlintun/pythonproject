import sys

# get name of arrtibutes in sys module
print(dir(sys))

# only few entries show here
# get names of attributes for current module

print(dir())

# create a new varibale 'a'

a = 5
print(dir())

# delete / remove a name
del a
print(dir())