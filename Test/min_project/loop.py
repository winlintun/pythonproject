larg = -1
print("Before", larg)

for i in [9, 41, 12, 3, 74, 15]:
    if i > larg:
        larg = i 
    print(larg, i)

print("After", larg)
    