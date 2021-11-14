
x = 2
y = 2
z = 3


print('x is id memory: ', id(x))
print()
print('y is id memory: ', id(y))
print()
print('z is id memory: ', id(z))

print(x is y)  # check if both point same memory location

print(y is z)

print(x is not y)  # check if both point separate memory location

print(y is not z)