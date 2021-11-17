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

# lambda

def square(x):
    return x * x
squ = lambda x: x*x
# squ = lambad (parameter): (return value)

print("Square :", square(3))
print("Lambda sQuare: ", squ(3))