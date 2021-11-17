greet = 'hello world'

print(greet[1])
print(greet[0:8])

for i in enumerate(greet[0:5]): print(i)

print(greet[:5] + ' wonderful' + greet[5:])
print(greet[5:])
x = '1 '; y = '2' ; z = '3'

print(x + y)
print(int(x) + int(y))

lst1 = [1, 2, 3]

lst2 = lst1

print('lst2 :', lst2)
lst2[1] = 4
print("Adding lst2[1] = 4")
print('lst1 :', lst1)
print()

items = [['rice', 2.4, 8], ['flour', 1.9, 5], ['corn', 4.7, 6]]

for item in items:
    #print(item)
    print('Product: %s Price: %.2f Quality: %i ' % (item[0], item[1], item[2]))

items[1][1] = items[1][1] * 1.2
print(items)

print(1.9 * 1.2)
print()

l = [2, 4, 8, 16]

print([i**3 for i in l])

for i in l:
    i **= 3
    print(i)

print()

def f1(x): return x*2
def f2(x): return x*4
lst = []

for i in range(16):
    lst.append(f1(f2(i)))
print(lst)
print([f1(x) for x in range(64) if x in [f2(j) for j in range(16)]])
print([f1(x) for x in range(10)])
print([f2(x) for x in range(10)])
print([f1(x) for x in range(10) if x in [f2(j) for j in range(10)]])
print()

list1 = [[1, 2, 3], [4, 5, 6]]

print([i * j for i in list1[0] for j in list1[1]])
print([x * y for x in list1[0] for y in list1[1]])
print()

words = 'here is a sentence'.split()
print([[word, len(word)] for word in words])
for word in words:
    print(word,len(word))

