from collections import ChainMap

defaults = {'theme': 'Default', 'language': 'eng','showIndex': True, 'showFooter': True }

cm = ChainMap(defaults) # create a chainmap with the default configuration

cm2 = cm.new_child({'theme': 'bluesky'}) # create a nwe chainmap with a child that overides the parent

print('cm2["theme"] = ', cm2['theme']) # returns the overide theme

print('cm2.pop("theme") =', cm2.pop('theme')) # return and remove child theme value

print('cm2["theme"] = ', cm2['theme']) # returrn the default theme

cm2.maps[0] = {'theme': 'desert', 'showIndex': False} # add a 'root context' same as new_child

print('cm2["swhoIndex"] ', cm2["showIndex"])

# counter object
print("cm2.parents ", cm2.parents)



print()
print('---------------------------')
print()
from collections import Counter


c1 = Counter('anysequence')
c2 = Counter({"a":1, 'c': 1, 'e': 3})
c3 = Counter(a=1, c=1, e=3)
print('c1 >>', c1)


print()

ct = Counter() # create an empty counter by object
ct.update('abca') # populates the object

print('ct >>', ct)

ct.update({'a':3}) # update the 'a' count

print('ct upate >>', ct)

for item in ct: print("%s : %d " % (item, ct[item]))

print()

# Ordered dictionaries

ct.update({'a': -3, 'b': -2, 'd': 3, 'e': 2}) # prefrom update

print('ct >>', ct)
print("sofrted(ct.elements() >>>", sorted(ct.elements())) # return a sorted list from iterator

print('ct.most_common() >>', ct.most_common())

print('ct.subtract({"a":2}) >>>', ct.subtract({'a': 2}))

print('ct >>', ct)