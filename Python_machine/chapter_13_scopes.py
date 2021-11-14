a_num = 10
print(dir())

def inner(): # function name is inner

    x = 4 # vairable x is define inside inner function
    print('x is ',x)

inner()

print()
y = 10

def inner():
    x = 4
    global y
    y = y + 1
    print("x is", x)
    print("inside the function y:", y)
print("y is",y)
inner()

print()
print("enclosed scope")
y = 10 # global scope

def outer(): # enclosing function
    z = 4

    def inner():
        x = 4
        print('x is',x)
        print("inside the function y:", y)

    print("y is", y)
    inner()
    print("z is", z)
outer()

print()
print("build in scope")

x = 5
def my_function():
    x = 10
    def inner():
        x = 15
        print("x is", x)
    inner()
my_function()