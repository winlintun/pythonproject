def add(name="winlintun",password='1213'):
    print(name,password)
add()
print()
def color(aa):
    if aa == 'red': # if function
        return "That is red"
    elif aa == 'blue':
        return "That is blue"
    elif aa == 'yellow':
        return "That is yellow"
    else:
        return "Error input"
user_input = input("Enter Color (red,blue,yellow): ")
print(color(user_input))
print()

def var(list_d):

    for x in list_d: # loop function
        print(x)
var1 = ['a','b','c','d','e','f','g'] # list using []
var(var1)
print()
print()
# Special Argument
def ass(*args):
    print(args)
ass(1,2,'air','car',0.11,'A')

print()
def aes(a,b,c,*var):
    print("This is Parameter a: ",a)
    print("This is Parameter b: ",b)
    print("This is Parameter c: ",c)
    print("Tuple Argument: ",var)
aes(1,2,'air','car',0.11,"A") # tuple (*) asterisk
print()

def aaa(**kwargs):
    print(kwargs['one'],kwargs['two'],kwargs['three'])
aaa(one=1,two=2,three=5) # dictonary (**kwargs)

print()


def greet(username, age):
    print("Hello, I am ", username)
    print("I am",age)
positional_argument= greet("Danie",22)
print()
keyword_argument = greet(username="Daniel",age=22)
print()
def profile(*info):
    print(info)
arbitary_argument= profile("Daniel",22,"Male")