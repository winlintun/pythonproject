# list to tuple

programming_language = ['Ruby and Rails', 'R', 'Java', 'Python', 'C++']

tuple_programming_language = tuple(programming_language)
print(tuple_programming_language)
print(type(tuple_programming_language))

# list nested for loop

first_name = ['Maung', 'U', 'Ko']
last_name = ['Ba Kaung', 'Myint Soe', 'Sai']
name = []
for f_name in first_name:
    for l_name in last_name:
        name.append(f_name+" "+l_name+'\n')
print(name)

# list method
print("""
lsit.append(itme)
list.extend(iterable)
list.insert(index, itme)
list.remove(item)
list.pop([index])
list.clear()
list.index(item [, start [, end]])
list.count(itme)
list.sort(key=None, reverse=False)
list.reverse()
list.copy()

""")

# list.append(itme)
things = ['first']
things.append('another thing')
print(things)

# list.extend(iterable)
things = ['first', 'another thing']
others = ['third', 'fourth']
things.extend(others)
print(things)
things.extend("another thing")
print(things)

# list.insert(index, item)
things = ['first', 'second', 'fourth']
print(things)
things.insert(2, 'third') # index န ပါတ် 2 ကနရောတွင် "third" က ိုထည ်မည်။
print(things)

# list.remove(itme)
my_list = ['first', 'second', 'first', 'second']
print(my_list)
my_list.remove('second')
print(my_list)

# list.pop([index])
things = ['first', 'second', 'third']
print(things)
second_item = things.pop(1)
print(second_item)
print(things)

# list.index(item [, start[, end]])
things = ['first', 'second', 'third']
print(things.index('second'))

things = ['first', 'second', 'third', 'fourth']
print(things)
print('index of third',things.index('third', 1, 3))


things = ['first', 'second', 'third', 'fourth']
#print('value error',things.index('fifth')) # value error


print()
print()
# list.sort(key=None, reverse=False)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

L = ['abc', 'ABC', 'aBe']
L.sort()
print(L)

my_list = ['abc', 'aBD', 'ABD', 'aBe']
# change sort order
my_list.sort(key=str.lower, reverse=True)
print(my_list)

# list.copy()
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)


fib = [1, 1, 2, 3, 5, 8]
fib.append(13)
print(fib)
fib += [89, 144]
print(fib)

fib.extend([21, 34, 55])

print(fib)

# assignment(=) del operators

fib[3] = 'whoops'
print(fib)

del fib[:5]
print(fib)

fib[1::2] = [-1, -1, -1]
print(fib)

# list of list

small_birds = ['hummingbrid', 'finch']
extinch_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carl_birds = [3, 'French hens', 2, 'turthedoves']
all_birds = [small_birds, extinch_birds, 'macaw', carl_birds]
print(all_birds)
print('index of [0]',all_birds[0])
print('index of [1]',all_birds[1])
print('index of [1][0]',all_birds[1][0])

# multiplication by an integer

print([1, 2, 3] * 6)

x = [3, 2, 1, 'blast off']
y = x
y[1] = 'Two'
print(x)

# change an item
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

# get a slice to extract items
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0:2]
test = marxes[::2]
print(test, type(test))
# start at the end and go left by 2:
marxes[::-1]
print(marxes)


the_list = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'melon']
print(the_list)
print("The last element in the list---->", the_list[-1])
print(the_list[2:5])
print(the_list[:4])
print(the_list[2:])

# combine list by using extend() or +=
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

# alternatively, you can use +=
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)
#append
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

# integer 2 square
squares = [num for num in range(1, 11)]
print(squares)

squares = [num**2 for num in range(1, 11)] # num ** 2 square
print(squares)

# change unicode
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print('the code',codes)

# list example
# looking through the list
the_list = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
for x in the_list:
    print(x, end=' ')

print()

# list comprehensions
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print('the list',number_list)

#ဒုတ ယနည််း- iterator နှင ် range() function က ု သံု်း၍ တည်ဆ ောက်သည်။

number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

number_list = list(range(1, 6))
print(number_list)

# pythonic way to build a list
number_list = [number for number in range(1, 6)]
print(number_list)

