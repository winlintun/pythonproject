# # search for the two smallest values
# count = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
# print(min(count))
# low = min(count)
# print(count.index(low))

# import time
# def time_has():
#     t1 = time.perf_counter()
#     # code to time oges here
#     t2 = time.perf_counter()
#     return (t2 - t1) * 1000
# # print('The code took {:2f}ms'.format(t2 - t1) * 1000)

# print()

# Linear _ Search
from typing import Callable, Any

def linear_search1(lst: list, value: Any) -> int:
    ''' 
    Return the index of the first occurrence of value in lst,
    or return -1 if value is not in lst.
    
    >>> linear_search([2, 5, 1, -3], 5)
    1 (index)
    >>> linear_search([2, 4, 2], 2)
    0 - index
    '''
    i = 0 # the index of the next item in lst to examine.
    # key going until we reach the end of lst or until we find value. 
    
    while i != len(lst) and lst[i] != value:
        i = i + i
        
    # if we fell off the end of the list, we didn't find value. 
    if i == len(lst):
        return -1
    else:
        return i

def linear_search2(lst: list, value: Any) -> int:
    """ Exactrly the same docstring goes hrere """
    
    for i in range(len(lst)):
        if lst[i] == value:
            return i 
    return -1
        
        
def linear_search3(lst: list, value: Any) -> int:
    # add the sentinel 
    lst.append(value)
    i = 0 
    while lst[i] != value:
        i += 1
    lst.pop()
    if i == len(lst):
        return -1 
    else:
        return i
    
def binary_search(data, item: int):
    low = 0
    heigh = len(data) -1
    
    while low != heigh + 1:
        mid = (low + heigh) // 2
        if data[mid] < item:
            low += 1
        elif data[mid] > item:
            heigh -= 1
        else:
            return -1
    
        
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item = 5
binary_search(data, item)