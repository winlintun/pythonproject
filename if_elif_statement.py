
print("****Welcome Beer House*******")


Age = int(input("What is your age: "))

if Age >= 18:
    print("Yes")
    print("You can buy Beer")
else:
    print("You can't buy Beer")
    print("Hey, kid just go back home")


"""
allowed_user = ['bill', 'steve']
user_name = input("What is your login! : ")
if user_name in allowed_user:
    print("Access granted")
else:
    print("Access denied")
    """

x = int(input("What is the time: "))
if x <= 10:
    print("Good Morning")
elif x < 12:
    print("Soom time for lunch")
elif x <18:
    print("Good day")
elif x <22:
    print("Good evening")
else:
    print("Good night")