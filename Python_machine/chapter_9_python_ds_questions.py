#1. 'in' operator
my_list = [1, 2, 3, 'a', 'b', 'c']
print('a' in my_list)

# how to list iterate
name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
z = zip(name, animal, age)
print('zip =', z)
for name, animal, age in z:
    print("%s the %s is %s" % (name, animal, age))
    print()
    print("{} the {} is {}".format(name, animal, age))

# 3 where to user list and dic
ids = [23, 1, 7, 9]
print(ids)

pets = {'dog': 2, 'cats': 1, 'fish': 5}
print(pets)


a = [1, 2, 3]
a.append(4)
print(a)
b = [1,2,3,4]
b.extend([5, 6])
print(b)

a, b = 1, 2 # string
print(id(a))
print(id(b))
c = [1, 2, 3] # list   same address
print(id(c))
print('id of 1',id(c[0]))
print('id or 2',id(c[1]))
print('id of 3',id(c[2]))


