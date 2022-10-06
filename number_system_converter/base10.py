# base 2 formula
# binary = 2**n-1

from decimal_to_binary import binary_to_decimal


b = '1010101'

b_len = len(b)

binary = 0

# 2**4-1 + 2**3-1 + 2**2-1 + 2**1-1

for n in b:
    int_n = int(n)
    print(type(int_n),int_n)
    formula = 2**b_len-int_n





#print(binary)
#print('ans: ', binary_to_decimal(1010101))

a = 'hello world'
a.ascii_letter

