def outer():
    print("outer function")
    i = 2
    def inner():
        print("Inner functio", i)

    inner()
outer()
print()
print("____________________________")
print()

def counter():
    print("Counter Function")
    i = 1

    def inner():
        nonlocal i
        i = i + 1
        #print("inner i ", i)
        return i
    return inner


next_func = counter()
print("Next ", next_func())
print("Next ", next_func())
print("Next ", next_func())



"""

def counter():
    print("Counter Func")
    i = 1
    def next():
        nonlocal i 
        i = i + 1
        #print("Inner func ",i)
        return i
    return next
    
next_func = counter()
print("Next ",next_func())
print("Next ",next_func())


"""