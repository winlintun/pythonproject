# rule 1 > can be stored in variable
# rule 2 > can be passed as parameter.
# rule 2 > can be returned from function

def get_another():
    print("Inovked get another")
    return hello

def invoke(func):
    print("Invoked called")
    func() # function as parameter


def hello():
    print("Hello called")

x = hello  # rule 1
x()
invoke(hello) # rule 2
get_another()()

print()
print("**********************************")

# lambda function

def square(x):
    return x * x
squ = lambda x: x*x
# squ = lambad (parameter): (return value)

print("Square :", square(3))
print("Lambda sQuare: ", squ(3))

print()



def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 85

func3 = lambda x,y=4: x+y

print(func3(2,3))


print(func(2))

print()

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#newList = list(map(lambda x: x+5, a))
newList = list(filter(lambda x: x%2 != 0, a))

print('a ', a)
print()
print("newList ", newList)