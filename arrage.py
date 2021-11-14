list = [1,5,2,7,8,9,200,155]
#first Room
print(list[0])
#9 will show
print(list[5])
#last room
print(list[7])
print("enter")
print("enter")
#Total Room
print("Total room is array is", len(list))
print("enter")
print("loop array")
t = (1,2,3)
for i in range(len(list)):
    print(list[i])
print("enter")
print("enter")
#sun array
list = [1,5,2,7,8,9,200,155]
x = 0
for i in range(len(list)):
    x = x + list[i]
    print("Total:", x)
print("enter")
print("enter")
list = [1048,1255,2125,1050,2506,1236,2010,1055]
maxnumber = list[0]
for x in list:
    if maxnumber < x:
        maxnumber = x
        print("Max number in array is", maxnumber)