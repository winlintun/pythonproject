import time
# generator function create an iterator of
# odd numbers between n and m

def oddGen(n, m):
    while n < m:
        yield n
        n += 2

# building a list of odd numbers between n and m

def oddLst(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

t1 = time.time()
sum(oddGen(1, 100000))
print("Time to sum an iterator: %f " % (time.time() - t1))


#geneter

def counter():
    yield 1
    yield 2
    yield 3
    yield 4

count = counter()

print('Count ', count)
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print("Count ", count)

for i in range(0, 5):
    print("I is ", i)

def custom_range(start, end):
    for i in range(start, end+1):
        yield i

for i in custom_range(0, 5):
    print("Custome range", i)


print()

def decent_to(num):
    return range(5, 0, -1)

for i in decent_to(5):
    print("i desend ", i)
print()

def decent_to(num):
    count = num
    while num >= 0:
        yield num
        num = num - 1

for i in decent_to(5):
    print("Yield I ", i )

print()

lst1 = [1, 2, 3, 4]

gen1 = (2 ** i for i in lst1)
print('gen1>>', gen1)
for x in gen1: print(x)
