#-------------------------------------------------------------------------------
# Name:        mutable and immutable
# Purpose:
#
# Author:      MNN-068
#
# Created:     24/05/2022
# Copyright:   (c) MNN-068 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

counter = 100
print(id(counter))
print(hex(id(counter)))

counter = 200
print(counter)
print(hex(id(counter)))
print()

rate = [1, 2, 3]
print(rate)
print(hex(id(rate)))
rate.append(4)
print(rate)
print(hex(id(rate)))

print()


l = [1, 2, 3]
h = [4, 5]

rank = (l, h)

h.append(6)
print(rank)