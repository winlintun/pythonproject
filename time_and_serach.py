import time
from typing import Callable, Any
from design_algorithm import (linear_search1, linear_search2, linear_search3)

def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float:
    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000

def print_times(v: Any, L: list) -> None:
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_item = (t2 - t1) * 1000
        
    while_time = time_it(linear_search1,L, v)
    for_time = time_it(linear_search2, L, v)
    sentinel_time = time_it(linear_search3, L, v)
    
    print("{0}\t {1:2.f}]t{2:.2f}\t{3:.2f}\t{4:.2f}".format(
        v, while_time, for_time, sentinel_time, index_item
    ))
    
L = list(range(101))
print_times(10, L)
# print_times(5000, L)
# print_times(10000, L)