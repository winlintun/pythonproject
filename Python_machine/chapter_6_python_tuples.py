# constructing tuples
x = (1, 2, 3)
x = 1, 2, 3 # this is tuple
x = 2, # this is (,) tuple type
print(x, type(x))

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))


x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(x)
pet1 = ['doge', 'cat', 'parrot']
print(type(pet1))
pet2 = tuple(pet1)
print(pet2, type(pet2))

a = tuple(m for m in range(8))
print(a)
b = tuple(i**2 for i in range(10) if i > 4)
print(b)

# tuple as records
lax_coordinates = (33.9425, -118.408056)
print(lax_coordinates)
#data about tokyo
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8044)
print(city,year,pop,chg,area)


# tuple unpacking
x = ['pig', 'cow', 'horse']
a, b, c = x
print(a, b, c)
print('a',a,type(a))
print('b',b, type(b))
print('c',c, type(c))

print()
# excess items
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a,b,rest)

# prefix
a, *body, b, c = range(5)
print(a, body, b, c)

*head, b, c, d = range(5)
print(head, b, c, d)


# tuple unpacking
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)


# nested tuple
pets = ('dog', 'cat'), 'parrot'
print(pets)

# integer vs tuple with one element
x = (2)
print(x, type(x))

x = (2,)
print(x,type(x))

# variable tuple can assign
vehicle = ('Toyota', 'BMW', 'Benz')
a, b, c = vehicle
print(a, b, c)

# accessing tuple element

pets = ('dog', 'cat', 'parrot')
print(pets[1])
print(pets[-1])


# tuple slicing
l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])