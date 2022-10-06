class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)


import math
class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calcualte_distance(self, other_point):
        return math.sqrt((self.x - other_point.x ** 2 + \
                        self.y - other_point.y) ** 2)

# how to use it
p1 = Point()
p2 = Point()

p1.reset()
p2.move(5,0)

print(p2.calcualte_distance(p1))
print(p1.calcualte_distance(p2))
#assert (p2.calcualte_distance(p1) == p1.calcualte_distance(p2))
print()
print()


class Person:
    def set_default(self, name, age):
        self.name = name
        self.age = age

p1 = Person()
p2 = Person()
p1.set_default('Aye', 49)
p2.set_default('Lin', 12)

print(p1.name, p1.age)
print(p2.name, p2.age)

