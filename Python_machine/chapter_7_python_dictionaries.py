# dictionary

dictionary_name = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3",
}
print(dictionary_name)
# constructing a dictionary
empty_dict = {}
print(empty_dict)
d = dict(state='NY', city='New Yourk')
print(d)

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict,type(my_dict))
print()

thisdict = {
    "brand": 'honda',
    "model": "HRV",
    "year": 2017
}
print(thisdict, type(thisdict))
x = thisdict["model"]
print(x)
# they are same
x = thisdict.get('model')
print(x)

car_dict = {'brand': 'honda', 'model': 'HRV', 'year': 2017}
car_dict['year'] = 2018
print(car_dict)


# convert by using dict()
# list of two-item list
lo1 = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lo1))

lo2 = ['ab', 'cd', 'ef']
print(dict(lo2))

# order of keys
car_dict = {'brand': 'honda', 'model': 'HRV', 'year': 1964}
for x in car_dict:
    print(x,':', thisdict[x], )


# key add
dictionary_name = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3'
}
print(dictionary_name)

dictionary_name['key_4'] = 'vlaue_4'
print(dictionary_name)

# update()
dict_1={'key_1':'value_1', 'key_2':'value_2', 'key_3':'value_3'}
dict_2={'key_4':'value_4', 'key_5':'value_5', 'key_6':'value_6'}
dict_1.update(dict_2)
print(dict_1)


first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)
# they are same
first = {'a': 1, 'b': 2}
first['b'] = 'platypus'
print(first)

# del()
first = {'a': 1, 'b': 2}
del first['a']
print(first)

sale = {'apple': 2, 'orange': 3, 'grapes': 4}
print(sale.values())

# clear() all dele in dict
dict_1.clear()
print(dict_1)

dict_1 = {'key_1': 'value1', 'key_2': 'value_2'}
print('key_1' in dict_1)
print('key_5' in dict_1)


if 'model' in car_dict:
    print("Yes, 'mode' is one of the keys in the car_dict")

dict_1 = {'key_1':'value_1', 'key_2':'value_2', 'key_3':'value_3'}
print(dict_1['key_1'])

print(dict_1.get('key_2'))

print(dict_1['key_3'][0])

# upper()
print(dict_1['key_3'] [0].upper())

# subtract
my_dict = {'key1': 123, 'key2': 'aa'}
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict)
print()
print(my_dict.keys())
print(list(my_dict.keys()))

print(list(dict_1.values()))

# itmes()
print(list(dict_1.items()))
print(dict_1.items())
car_dict = {
    "brand": 'Ford',
    'model': 'Mustang',
    'year' : 1964
}
for x, y in car_dict.items():
    print(x, ":", y)


dict_1 = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3",
    "key_4": "value_4"
}

dict_2 = {"key_5": "value_5", "key_6": "value_6"}

#print('dict_1',dict_1,'\n','dict_2',dict_2)

dict_2 = dict_1.copy()
print(dict_1)
print(dict_2)

# new key assign
# create a new dictionary
d = {}

d['animal'] = 'Dog'
d['answer'] = 42
print(d)

# nested with dictionary
d = {'key1': {'nestkey': {'subnestkey': 'value'}}}
print('netsted key on dict',d)

# kee calling the keys
print(d['key1']['nestkey']['subnestkey'])


# sub dic
myfamily = {
    "child": {'name': 'Email', 'year': 2004},
    "child1": {'name': 'Tobias', 'year': 2007},
    "child2": {'name': 'Linus', 'year': 2011}
}
print(myfamily)


# dict method
d = {'key':1, 'key2': 2, 'key3': 3}
print(d.keys()) # this is key
print(d.values()) # this is value
print(d.items()) # show all key and value
print(isinstance(d, dict))

# add dict
dictionary1 = dict(state='NY', city='New York')
print(dictionary1)
# output key
print(dictionary1.keys())
# print value
print(dictionary1.values())
# itmes
print(dictionary1.items())

print(dictionary1['state'])
print()
# iterating through dict
dictionary1 = dict(stat='NY', city='New York')
for item in dictionary1:
    print(item)

print()
a = {'size': '10 feets', 'weight': '16 pounds'}
print('size' in a)
print('length' in a)
print(dir(a))
a = {}
a.update({'name': 'Dan Brown'})
print(a)
print(a.values())
a.clear()
print(a)
a = {'name': 'Skandar', 'age': 24, 'nam': 'Mg Mg'}
del a['name']
a.pop('age')
print(a)

# deep copy

a = {'name': 'Skandar', 'age': 24}
b = a
a['name'] = 'Jenet Jackson'
b['age'] = 16
print(a)
print(b)

# popitme() method
a.popitem()
print(a)
b = a.setdefault('name')
print(a)
print(b)


import collections
a = {'a': 'A', 'b': 'B'}
b = {'c': 'C', 'd': 'D'}
print('a and b are str +')
print()

chained_dict = collections.ChainMap(a, b)
print('Calling individual values from {}'.format(chained_dict))
print('Key: ')
for key in chained_dict.keys():
    print(key, end=' ')

print()
a.update(b)
print('a update b',a)
print('b is',b)
print('a and b are str +', a, b)


print("Key and values")
for key, val in chained_dict.items():
    print("{} = {}".format(key, val))