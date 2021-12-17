# list
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

# set
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

# Solution


from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)


d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)