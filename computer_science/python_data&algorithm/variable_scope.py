#gloabal scope here
a = 10
b = 20

def my_function():
    #local scope here
    global a
    a = 11
    b = 21

my_function()
print(a) # global change inner function a
print(b)

