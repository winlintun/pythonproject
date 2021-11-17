# scenario  1

# number and string are immutable

def inc(num): # immutable can't change
    print("Inc ", num)
    num += 10
i = 100
inc(i)
inc(i)
print("i is: ", i)


# list & map mutable
# scenario 2
def append(lst): # reference value mutable change
    lst.append(100)

my_list = []

append(my_list)
append(my_list)
print("My_list ", my_list)

# scenario 3
def upate(lst): # create object and mutable change
    lst = [200, 200]

upate(my_list)

print("my_list update ", my_list)









print('------------------------')

my_var = 25
def my_method(v):
    print('v is ', v)
    v += 10

    return v
my_method(my_var)

print(my_var)
# object are immutable


# list
mylist = [1, 2, 3]

x = mylist
x.append(4)
print(mylist)
print()


# dic
my_dic = {'key': 'value'}

def m(d):

    d['key'] = 123

print(my_dic) # prints {'key': 'value'}


m(my_dic)

print(my_dic)