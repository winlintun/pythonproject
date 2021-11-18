import collections
from collections import Counter

c = Counter('greet')
print('c', c)
c = Counter(['a', 'a',  'b', 'c', 'c'])
print('c list>', c)
e = Counter({'a':1, 'b':2})
print('c dic>', c)
d = Counter(cats=4, dogs=7)
#d = {'cats':2}
print('c keyword>', c['pet'])
print()

print(list(c.elements()))

#c = Counter(['a', 'a',  'b', 'c', 'c'])
print('c.most_common(2) :', c.most_common(2))
print()

c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'c', 'd']
c.subtract(d)
print("c.subtrack(d): ", c)

c.update(d)
print('c :', c)

c.clear()
print("c.clea() ", c)

print("_______________________")
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'c', 'd'])

print('c :', c)
print('d :', d)
print("c + d :", c+d)
print("c - d :", c-d)

