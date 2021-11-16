"""
print('How are you')
felling = input()
if felling.lower() == 'great':
    print("i feel great too.")
    
else:
    print("I hope the rest of your day is good")
    
print()
print("Hello world!")
print("What is your name?")
myName = input()
print("It is good to meet you,", myName)
print("The lenght of your name is:")
print(len(myName))
print9)
"""
print('My name is')
for i in range(5):
    print("Jimjmy five times({})".format(i))
    
a = 0

for i in range(101):
    a = a + i 
    
print(a)
print()

x = 'Python'
print(x[1]+x[4])

x = [2, 4]
x += [6, 8]
print(x[2]//x[0])

list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break