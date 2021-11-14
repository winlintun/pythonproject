def say_hi(s):
    s = s + ' World'
    return s


Var = 'Hello'

say_hi(Var)

print(say_hi(Var))

def times(x, y):
    return x * y

times(2, 4)

x = times(2, 4)
print(x)

# variable number of arguments (*args)
print("***variable numberr of arguments (*args)")
def addition(*args):
        total = 0
        for i in args:
                total += 1
        return total
answer = addition(20, 10, 5, 1)

print('the *args is:',answer)

# variable length arguments (*args and **kwargs)
print("***variable length arguments (*args and **kwargs)")
def add(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])
# 3, 4, 5 are combined into args
# six and seven are combined into kwargs
add(1, 2, 3, 4, 5, six=6, seven=7)
print()
# omitting of args or kwargs is also possible
add(1, 2, three=3)



# accepting an arbitrary number of arguments
print("***accepting an arbitrary number of arguments")
def adder(num1, num2):
    sum = num1 + num2
    print("The sum of your numbers is %s" % sum)

adder(1, 2)
adder(-1, 2)


def example_function(arg1, arg2, *arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    for value in arg3:
        print("arg3 value:", value)
example_function(1, 2, 3, 4, 5)
print()
print()
def adder(num1, num2, *nums):
    sum = num1 + num2

    for num in nums:
        sum = sum + num
    print("type of *nums:",type(nums))
    print("The sum of your numbers is %d" % sum)
adder(1, 2, 3, 4, 5, 6)
print()
# accepting an arbitrary number of keyword arguments
print("***accepting an arbitrary number of keyword arguments")
def example_function(arg1, arg2, **kwargs):
    print("arg1:", arg1)
    print("arg2", arg2)
    for key, value in kwargs.items():
        print("arg3 key:", key,end=' ')
        print("arg3 value:", value)


    print("type of **kwargs:", type(kwargs))
example_function("a", "b")
example_function('a', 'b', value3='c', value4='d', value5='e')
print()
# forced keyword argument
print("***forced keyword argument")
def foo(a, b, *, c, d):
    print(a, b, c, d)
foo(1, 2, c=3, d=4)

print()
print("variable-length argument")
def my_func(*args, last):
    for arg in args:
        print(arg, end=' ')
    print('\n', last)
my_func(8, 9, 10, last=50)
print()
print("**Unpakcing into Arguments Asterisk(*)")
def add_one(a, b, c):
    print(a+1, b+1, c+1)
# list/ tuple unpacking, length must match
my_list = [4, 5, 6] # list or tuple
add_one(*my_list)
print()
print("asterisks(**) two argument")
# dic unpacking, keys and length must match
my_dict = {'a': 1, 'b': 2, 'c': 3}
add_one(**my_dict)
print()

print("Global and Local Variables")
# Global and local Variables
total = 0 # this is global variable.
def sum(arg1, arg2):
    total = arg1 + arg2 # total is local variable (inside the function)
    print("inside the function local total:", total)
    return total
sum(10, 20) # now you can call sum function
print("Outside the function global total:", total)
print()

# using main()
print("***using main()")



def summation(first, second):
    total = first + second
    return total


def main():
    outer_total = summation(10, 20) * 2
    print("Double the total is",str(outer_total))


if __name__ == '__main__':
    main()

print(f"First Module's Name: {__name__} ")
print()

def main():
    pass

if __name__ == '__main__':
    main()

print(type(main)) # main is function
print()


def main():
    print(f"Frist module's Name: {__name__}")

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    print("Run Directly")
else:
    print("Run From Import")


print("*******")
def outer_name(new_name):
    name = 'outer ' + new_name

    def inner_name():
        name = 'inner ' + new_name
    inner_name()
    return  name
print(outer_name('mgmg'))
print()



# Lambda Function
print("Lambda Function")
triple = lambda x: x * 3
print(triple)
print(triple(5))
print()

print("Sort Sequences of Data")
grades = [{'name': 'Jennifer', 'final': 95},
          {'name': 'David', 'final': 92},
          {'name': 'Aaron', 'final': 98}]

#print(grades)
print(sorted(grades, key=lambda x: x['name']))
print()
print(sorted(grades, key=lambda x: x['final'], reverse=True))
print()
# get highest final score
print(max(grades, key=lambda x: x['final']))
# get min final score
print(min(grades, key=lambda x: x['final']))

