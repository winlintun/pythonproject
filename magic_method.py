#-------------------------------------------------------------------------------
# Name:        magic method
# Purpose:
#
# Author:      MNN-068
#
# Created:     24/05/2022
# Copyright:   (c) MNN-068 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Sport:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def get_name(self):
        return self.name

    def get_sport(self):
        return self.sport

first = Sport('john', 'Game of throunse')
print(first.get_name())
print(first.get_sport())

print('--------------')

class Sport:
    def set_name(self, name):
        self.name = name

    def set_sport(self, sport):
        self.sport = sport

    def get_name(self):
        return  self.name

    def get_sport(self):
        return self.sport

second = Sport()
second.set_name('Messi')
second.set_sport('Soccer')
print(second.get_name())
print(second.get_sport())
print("_-----------------------_")

# Components

# 1 Object Constructor and initaliser

class AbstractClass:
    def __new__(cls, a, b):
        print('calling magic method __new__')
        instance = super(AbstractClass, cls).__new__(cls)
        instance.__init__(a, b)

    def __init__(self, a, b):
        print("Calling magic method __init__")
        print("Initializing Instance ", a, b)

a = AbstractClass(2, 3)


dict1 = {1: 'XYZ'}
dict2 = {2: "LMN"}

class AddDict(dict):
    def __add__(self, dicts):
        self.update(dicts)
        return AddDict(self)
a = AddDict(dict1)
b = AddDict(dict2)

print(a + b)

print('-------------------------')

class String:
    def __init__(self, string):
        self.string = string

    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other

str1 = String('Hello')
print(str1 + ' world')

print('-------------------------')
print()

class World(str):
    ''' Class for world, defining comparison based on world lenght '''

    def __new__(cls, world):
        # Note that we have to use __new__. This is because str is an immutable
        # type, so we have to initiaize it early (at cration)
        if ' ' in world:
            print("Value contains space. Truncating to the first space.")
            world = world[:world.index(' ')] # world is now all chars before first space
        return str.__new__(cls, world)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

