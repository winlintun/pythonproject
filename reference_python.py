counter = 100
print(counter)

print('id: ', id(counter))
print('hex: ', hex(id(counter)))

max_num = counter
print(id(max_num))
max_num = 999
print(id(max_num))

print()
print()

# Counting reference
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

num = [1, 2, 3]
num_id = id(num)
print(ref_count(num_id)) # 1

ranks = num
print(ref_count(num_id)) # 2

ranks = None
print(ref_count(num_id)) # 1

num = None
print(ref_count(num_id)) # 0

