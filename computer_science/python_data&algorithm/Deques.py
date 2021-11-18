import itertools
from collections import deque

dp = deque('abc') # create deque (['a', 'b', 'c'])
dp.append('d') # adds the value 'd' to the right
print('dp is =', dp)
dp.appendleft('e') # add the value 'e' to the left
print('dp is =', dp)
dp.extend('eft')# add multiple items to the right
print('dp extend ', dp)
dp.pop()
print('dp pop() ', dp)
dp.popleft()
print('dp popleft() ', dp)

dp.rotate(1) # rotates all item 1 step to the righ
print('dp.rotate(1) ', dp)
dp.rotate(2) # rotates all item 2 step to the right
print('dp.rotate(2) ', dp)
print('list(itertools.islice(dp,3,9) ', list(itertools.islice(dp, 3, 9)))
print()

dp2 = deque([], maxlen=3)
for i in range(6):
    dp2.append(i)
    print('dp2 =', dp2)

    