s1 = {'ab', 3, 4, (5,6)}
s2 = {'ab', 7, (7, 6)}

print('s1 is ', s1)
print('s2 is ', s2)
print('s1 - s2 ', s1 - s2) # same as s1.differenec(s2)
print('s1.intersection(s2) ', s1.intersection(s2))

print('s1.union(s2) ', s1.union(s2))
print('ab' in s1)
print('ab' not in s1)

for element in s1: print(element)
print()
print('-----------------------')

# immutable sets

#print('s1.add(s2) ', s1.add(s2)) # TypeError

print('s1.add(frozenset(s2) ', s1.add(frozenset(s2)))
print('s1 ', s1)
print()

fs1 = frozenset(s1)
fs2 = frozenset(s2)

print("{fs1: 'fs1', fs2: 'fs2'} =>", {fs1: 'fs1', fs2: 'fs2'})

