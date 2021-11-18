import collections
from collections import namedtuple

# string
point = namedtuple("point", 'x y z')
newP = point(3, 4, 5)
print("newP = string: ", newP)

# list
point = namedtuple("point", ['x', 'y', 'z'])
newP = point(3, 4, 5)
print("newP = list: ", newP)

# dict
point = namedtuple("point", {'x':0, 'y':0, 'z':0})
newP = point(3, 4, 5)
print("newP = dict: ", newP)

#index
point = namedtuple("point", {'x':0, 'y':0, 'z':0})
newP = point(3, 4, 5)
print("newP = index: ", newP.x, newP.y, newP.z)
print("newP[0]:", newP[0])
#isdict()
print("newP.asdict():", newP._asdict())
print("newP._fields:", newP._fields)
print()

# change tuple
newP = newP._replace(x=6)
print("newP=newP._replace(x=6):", newP)

