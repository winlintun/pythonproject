# set
my_set = {'apple', 'banana', 'cherry'}
print('type of set',my_set,type(my_set))

my_set2 = set(['one', 'two', 'three'])
print('type of set2',my_set2,type(my_set2))

# use set() instead
a = {} # empty dictionary
print(type(a))
a = set() # empty set
print(type(a))

my_set3 = set('aaaabbbccdddefff')
print(my_set3)

my_set = set()
my_set.add(43)
my_set.add(True)
my_set.add('hello')
print(my_set)

my_set.add(43)
print('set add same value',my_set)
# there are same
a = {1, 2, 3}
print('org a',a)
a.update([3,4,5,6])
print('update a', a)
for num in a:
    print(num, end=' ')
print()

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
print(drinks)

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)


# cheick if element is in set
my_set = {'apple', 'banana', 'cherry'}
if 'apple' in my_set:
    print('yes')

# remove element
print()

a = {1, 2 , 3, 4}
print(a.pop())
print(a)

print('a remove(3)', a.remove(3))
print(a)
print()

# discard
a = {1, 2, 3}
a.discard(2)
print(a)

a.discard('nonexistent item')
print(a)
a.clear()
print(a)

my_set = {'apple', 'banana', 'cherry'}
my_set.remove('apple')
print(my_set)

# reading data from a set (iterating)
#note: order is not important
my_set = {'apple', 'banana', 'cherry'}
for i in my_set:
    print(i)

# set opteration
odds = {1, 3, 5, 7, 9}
event = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7 ,11}
# union(): combline element from both sets
# hote that this set does not change the two set
u = odds.union(event)
print(u)

u = odds.union(event, primes)
print('3set', u)


# intersection
i = odds.intersection(event)
print(i)
i = odds.intersection(primes)
print(i)
i = event.intersection(primes)
print(i)

# difference of sets
set_A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_B = {1, 2, 3, 10, 11, 12}

diff_A = set_A.difference(set_B)
print(diff_A)

diff_B = set_B.difference(set_A)
print(diff_B)
