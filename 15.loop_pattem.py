"""
start(*) loop
"""
#star_loop
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
print()
print()
#number_loop
num=1
for i in range(5):
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()

print()
print()
#trigal start loop
for i in range(5):
    for j in range(4-i):
        print(' ',end='')
    for k in range(i+1):
        print('*',end=' ')
    print()

