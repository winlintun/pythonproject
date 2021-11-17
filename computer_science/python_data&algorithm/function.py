def greeting(langauge):
    if langauge == 'eng':
        return 'hello world'
    elif langauge == 'fr':
        return 'Bonjour le monde'
    else: return 'Language not supported'

#print(greeting('eng'))

l = [greeting('eng'), greeting('fr'), greeting('ger')]

print(l[1])



def callf(f):
    lang = 'eng'
    return (f(lang))

print(callf(greeting))

print()

# Higher order functions

lst = [1, 2, 3, 4]

print(list(map(lambda x: x**3, lst)))
print(list(filter((lambda x: x<3), lst)))

words = str.split('The logest word in this sentence')
print(sorted(words, key=len))


sl = ['A', 'b', 'a', 'C', 'c']
print('sl.sort()', sl.sort())
print('sl : ', sl)
print(sl.sort(key=str.lower))

print(sl.sort())
print(sl)

alist = ['A', 'b', 'C', 'a', 'c', 'B']
alist.sort()
print(alist)
blist = [1, 2, 5, 7, 4, 4, 6]
blist.sort()
print(blist)
blist.reverse()
print(blist)
print()

items = [['rice', 2.4, 8], ['flour', 1.9, 5], ['corn', 4.7, 6]]
items.sort(key=lambda item: item[1])
print(items)
print("____________________________")
def iterTest(low, high):
    while low <= high:
        print(low)
        low = low + 1

def recurTest(low, high):
    if low <= high:
        print(low)
        recurTest (low+1, high)

def greet():
    print('Hello')
    greet()
greet()