import collections
from collections import deque

d = deque("hello")
print('d :', d)
d.append('4')
d.appendleft(5)
print("d.append('4',appendliet(5)) :", d)
# pop / remove
print("pop ", d.pop())
print("popleft()", d.popleft())
print("d ", d)

# clear
d.clear()
print("d ", d)

# extend
d.extend('456')
print("d ", d)
d.extend([1, 2, 3])
print("d ", d)

# rotate
d.rotate(-2)
print("d rotae(-1): ", d)
d.rotate(1)
print("d.rotate(1) ", d)


# maxlen

d = deque("hello", maxlen=5)
print("d ", d)
d.append(1)
print("d ", d)