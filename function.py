def printHello():
    print("Hello")
printHello()
print("enter")
print("enter")
def printHello(val):
    print("Hello", val)
printHello("World")
printHello("Python")
print("enter")
print("enter")
def sum(val1,val2):
    return val1+val2
print("Sum: ", sum(1,4))
print()
print()
list = [1048,1255,2125,1050,2506,1236,2010,1055]
maxnumber = list[0]
for x in list:
    if maxnumber < x :
        maxnumber = x
print("MAX number in array is",maxnumber)