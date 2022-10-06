import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%*'

all_it = lower + upper + numbers + symbols

length = 16

password = ''.join(random.sample(all_it,length))

print('generate_password: ',password)

